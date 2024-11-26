# from infoconnect.conf.db import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_PORT, DB_USER
import mysql.connector
import csv


DB_HOST = '101.200.77.202'
DB_USER = 'infoconnect'
DB_PORT = '3306'
DB_PASSWORD = 'noNaanKAlnX8h1mx'
DB_DATABASE = 'infoConnect'


class ExcelExport:
    def __init__(self):
        self.connect = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            port=DB_PORT,
            password=DB_PASSWORD,
            database=DB_DATABASE,
        )
        self.cur = self.connect.cursor(buffered=True)
        pass

    def export_to_csv(self, table):
        self.cur.execute("""
            DESC notice_result
        """)

        header = []
        for item in self.cur:
            header.append(item)


        self.cur.execute("""
        SELECT * FROM notice_result
        """)

        file = open('example.csv', 'w', encoding="UTF8")
        writer = csv.writer(file)

        data = []
        for item in self.cur:
            data.append(item)

        writer.writerow(header)
        writer.writerow(data)

        file.close()

        # with open('example.csv', 'w', encoding="UTF8") as file:

    def close(self):
        self.cur.close()
        self.connect.close()
        pass


e = ExcelExport()
e.export_to_csv('notice_result')
e.close()
