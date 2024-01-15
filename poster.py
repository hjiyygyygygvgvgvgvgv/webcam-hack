import telebot
import sys
import os

try:
  
  chat_id = int(sys.argv[1])
  file = str(chat_id)+'.png'
  bot = telebot.TeleBot("6626505860:AAFMw3MogbqjMuiaN-3MN8xMZyo1gtfpaaI")
  img = open(file, 'rb')
  bot.send_photo(chat_id, img)
  os.remove(file)

except:
  pass
