import os
token = os.environ['TELEGRAM_TOKEN']

PORT = int(os.environ['PORT'])
HEROKU_APP_NAME = os.environ.['HEROKU_APP_NAME']
updater.start_webhook(listen="0.0.0.0",
                              port= PORT
                              url_path = TELEGRAM_TOKEN)
updater.bot.set_webhook(url = 'https://{}.herokuapp.com/'.format(HEROKU_APP_NAME))

from telegram.ext import Updater
updater = Updater(token, use_context=True)

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#getting started
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
from telegram.ext import CommandHandler
updater.dispatcher.add_handler(CommandHandler('start', start))

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
from telegram.ext import MessageHandler, Filters
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

#faculty details: '/faculty'
def faculty(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2',
    text="*FE Faculty*\nHOD: Dr\. Ajazul Haque \- __\+91 8793791366__\n")
updater.dispatcher.add_handler(CommandHandler('faculty', faculty))

#testing inline-keyboard
from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def assignments(update, context):
    keyboard = [[InlineKeyboardButton("Chemistry", url='www.google.com', callback_data='1'),
                 InlineKeyboardButton("Graphics", callback_data='2'),
                 InlineKeyboardButton("PCE", callback_data='5')],

                [InlineKeyboardButton("Physics Practice Sets", callback_data='3'),
                 InlineKeyboardButton("Mathematics Tutorials", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
updater.dispatcher.add_handler(CommandHandler('assignments', assignments))

def experiments(update, context):
    keyboard = [[InlineKeyboardButton("Physics", url='www.google.com', callback_data='1'),
                 InlineKeyboardButton("Chemistry", callback_data='2'),
                 InlineKeyboardButton("C Programming", callback_data='5')],

                [InlineKeyboardButton("Graphics AutoCAD", callback_data='3'),
                 InlineKeyboardButton("Mathematics Tutorials", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)
updater.dispatcher.add_handler(CommandHandler('experiments', experiments))

def timetable(update, context):
    keyboard = [InlineKeyboardButton("A", url='www.google.com', callback_data='1'),
                 InlineKeyboardButton("B", callback_data='2'),
                 InlineKeyboardButton("C", callback_data='3')]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Select your decision:', reply_markup=reply_markup)
updater.dispatcher.add_handler(CommandHandler('timetable', timetable))  

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
updater.dispatcher.add_error_handler(error)

updater.start_polling()
