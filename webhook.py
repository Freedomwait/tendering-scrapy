from larkbot import LarkBot

def main():
    # use your
    WEBHOOK_SECRET = ""
    bot = LarkBot(secret=WEBHOOK_SECRET)
    bot.send(content="well done! please check your email ~")

if __name__ == '__main__':
    main()

