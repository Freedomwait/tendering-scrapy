import smtplib

from string import Template

from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# BOTPDACDVSBQUMUJ

# user your  email config and data
MY_ADDRESS = 'TODO'
PASSWORD = 'TODO'
TASK_CODE = '2022_12_12_1'
file_list = [f'out/data{TASK_CODE}.csv']


def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def main():
    names, emails = get_contacts('contacts.txt')  # read contacts
    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the message body for our sake
        print(message)

        # setup the parameters of the message
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "任务执行成功，请查收附件"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # 添加附件
        for file_name in file_list:
            print("file_name", file_name)
            # 构造附件
            xlsxpart = MIMEApplication(open(file_name, 'rb').read())
            # filename表示邮件中显示的附件名
            xlsxpart.add_header('Content-Disposition',
                                'attachment', filename='%s' % file_name)
            msg.attach(xlsxpart)

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
