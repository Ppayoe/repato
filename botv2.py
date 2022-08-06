import sys
import time
import os
try:
    import telepot
    from telepot.loop import MessageLoop

except ImportError:
    print('%s telepot isn\'t installed, installing now.')
    os.system('pip install telepot')
    print('%s telepot has been installed.')
    os.system('cls')
    import telepot
    from telepot.loop import MessageLoop
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'] != '/start':
            for x in range (10):
                bot.sendMessage(chat_id, msg['text'])

TOKEN = "5402313096:AAE13eEFO5ujk_H9M1jyNUe5vGpqemRcOrk"#sys.argv[1]  # get token from command-line

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)