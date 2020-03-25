import os

from telegram.ext import Updater

from telegram.ext import CommandHandler

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

#getting started
def start(update, context):
    text_start = 'Hello\! I\'m mycrowbot\.\nHope you\'re doing good\!\n'\
                    'Check /about to know what I can do'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_start)

def about(update, context):
    text_about = '*/* represents a command\. You can see the entire command list anytime using /help\n'\
                'I can, at this moment, retrieve: /assignments,'\
                '/experiments, /timetable and /faculty details for FE at VIVA Institute of Technology\n'\
                'There is a /library with select books that you can access\.\n'\
                'I also have a list of /events that you can plan to attend\.\n'\
                'More features are being planned\. If you have an idea, you should definitely drop a text at @faraazb'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_about)

def help(update, context):
    text_help = 'Commands:\n/assignments\-Links to all subject assignments\n'\
                '/experiments\-Links to all subject manuals/experiments\n'\
                '/timetable\-Links to time\-table\n'\
                '/faculty\-Retreives faculty contacts\n'\
                '/library\-Links to selected books\n/help\-Shows help message\n'\
                '/events\-Shows ongoing and scheduled events'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_help)


#faculty details: '/faculty'
def faculty(update, context):
    text_faculty = '*FE Faculty*\n__Engineering Physics__\nHOD: _Dr\. Ajazul Haque_ \- \+91 9764287046\n'\
                    '_Deepak R\. Dubey_\n\n__Engineering Mathematics__\n'\
                    '_Jayesh C\. Jain_ \- \+91 9768949708\n'\
                    '_Shiksha Singh_ \- \+91 8692068028\n'\
                    '_Ramashankar R\. Prajapati_\n\n__Engineering Chemistry__\n'\
                    '_Shwetali K\. Churi_\n'\
                    '_Manju R\. Mishra_\n\n__Engineering Graphics__\n'\
                    '_Manojkumar Yadav_ \- \+91 8080201383\n\n__C Programming__\n'\
                    '_Bhavika Thakur_\n\n__Engineering Mechanics__\n'\
                    '_Sushil Sharma_\n\n__Basic Electrical Engineering__\n'\
                    '_Sunil P\. Suknale_\n\n__Proffesional Communication Ethics__\n'\
                    '_Prashant R\. Pawar_\n'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_faculty)

from telegram.ext import CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def assignments(update, context):
    keyboard_assgn = [[InlineKeyboardButton("Chemistry", url='https://drive.google.com/open?id=13dSGDPSp5pzFh9s3qKyiwYxDovfuN7y5', callback_data='1'),
                 InlineKeyboardButton("Graphics", url='https://drive.google.com/open?id=1ka9ydjoId6-0l6-sip8uyJ4IPhv90UfT', callback_data='2'),
                 InlineKeyboardButton("PCE", url='https://drive.google.com/open?id=1Z-iuKGfvVW90e17L0NTq34dE6k5X_vgK', callback_data='3')],

                [InlineKeyboardButton("Physics Practice Sets", url='https://drive.google.com/open?id=128qWEkLlQ6jm24FNZDU1fqqUm4wUFXK7', callback_data='4'),
                 InlineKeyboardButton("Mathematics Tutorials", url='https://drive.google.com/open?id=1lRTxg-Ezc7UDdoPvZnkQisW00gktz23y', callback_data='5')]]

    reply_markup_assgn = InlineKeyboardMarkup(keyboard_assgn)

    update.message.reply_text('Please choose:', reply_markup=reply_markup_assgn)

def experiments(update, context):
    keyboard_exp = [[InlineKeyboardButton("Physics", url='https://drive.google.com/open?id=1gW2-IjdLjWqwQ45XRpXwci2pBDWYrL44', callback_data='1'),
                 InlineKeyboardButton("Chemistry", url='https://drive.google.com/open?id=15IamaiZ4Pv5tznuEx9ymadLnp1WPkjgF', callback_data='2'),
                 InlineKeyboardButton("C Programming",url='https://drive.google.com/open?id=1Al-5U_ArNXGKpVWnixFtEc5kdV1UQxie', callback_data='3')],

                [InlineKeyboardButton("Graphics' Term Sheets", url='https://drive.google.com/open?id=1FXJylY1qxQYn_oD5nr-e6M32DkFXyyhl', callback_data='4'),
                 InlineKeyboardButton("Mathematics Tutorials", url='https://drive.google.com/open?id=1M1U5VDHh0lydbcdTf0nozxpbtSXDKCgA', callback_data='5')],
                 [InlineKeyboardButton("Workshop", url='https://drive.google.com/open?id=1wdDWAKD5CocluY5WjlmEQAuDX9VfXiW_', callback_data='6')]]

    reply_markup_exp = InlineKeyboardMarkup(keyboard_exp)

    update.message.reply_text('Please choose:', reply_markup=reply_markup_exp)

# A problem existed with the buttons in timetable and library, always use squared
# backets outside button formatting brackets
SENDTT = range(1)
DIVA, DIVB, DIVC = range(3)
def timetable(update, context):
    keyboard_tt = [[InlineKeyboardButton("A", callback_data=str(DIVA)),
                 InlineKeyboardButton("B", callback_data=str(DIVB)),
                 InlineKeyboardButton("C", callback_data=str(DIVC))]]

    reply_markup_tt = InlineKeyboardMarkup(keyboard_tt)
    update.message.reply_text('Select your division:', reply_markup=reply_markup_tt)
    return SENDTT

def sendtt(update, context):
    # div = update.callback_query.data
    tt_ida = 'AgACAgUAAxkBAAJXmF56Be49xvY6xOFhxp9RGoWeQeKbAALSqTEb8nrRV2l0H6OvI7V4RbElMwAEAQADAgADeAAD0wMFAAEYBA'
    # if div == 'DIVA':
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=tt_ida)
    # elif div == 'DIVB':
    #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=divb)
    # elif div == 'DIVC':
    #     context.bot.send_photo(chat_id=update.effective_chat.id, photo=divc)
def sendttb(update, context):
    tt_idb = 'AgACAgUAAxkBAAJXm156CFyKUA_2PQABgleZYwABSAvNaFEAAlWpMRtEb9FXtfHrtLm2HgVpPxszAAQBAAMCAAN4AAPRjwUAARgE'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=tt_idb)
def sendttc(update, context):
    tt_idc = 'AgACAgUAAxkBAAJXnl56CHTXUHRzCwsbg4MaviY4G1D0AALTqTEb8nrRV-iGInpDsN0Oc7YlMwAEAQADAgADeAAD1vkEAAEYBA'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=tt_idc)

def library(update, context):
    keyboard_lib = [[InlineKeyboardButton("Library", url='https://drive.google.com/open?id=1eMTP1gAc53ctZC5Rz8OhUIVVj60ESRN9')]]
    reply_markup_lib = InlineKeyboardMarkup(keyboard_lib)
    update.message.reply_text('Under development, only links to GD rn:', reply_markup=reply_markup_lib)


def cancelmain(update, context):
    # This is used to cancel any arbitrary operation midway
    text_cancel = 'No problem!'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_cancel)



EVENTM, TYPINGN, TYPINGD, DELETING = range(4)
LIST, ADD, DELETE, CANCEL = range(4)
event_manager = [506490090]

from telegram.ext import (ConversationHandler, MessageHandler, Filters)

def events(update, context):
    user_id = update.effective_user.id
    # if user_id not in event_manager:
    #     lis_event(update, context)
    # else:
    keyboard = [[InlineKeyboardButton("List Events", callback_data=str(LIST))],
                    [InlineKeyboardButton("Add Event", callback_data=str(ADD))],
                    [InlineKeyboardButton("Delete Event", callback_data=str(DELETE))],
                    [InlineKeyboardButton("Cancel", callback_data=str(CANCEL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
    return EVENTM
    # query = update.callback_query
    # logger.info("This is your buttons callback_data:{}".format(query.data))

from database import DBHelper
db = DBHelper()

def add_event(update, context):
    # text_start = 'Hello\! I\'m mycrowbot\.\nHope you\'re doing good\!\n'\
    #                 'Check /help to know what I can do'
    # context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=text_start)
    add_instructions = 'To add an event, send me the event details in the following format:\n'\
                    'First, send me the name as one message, then send the description as another\n'\
                    'To cancel this operation, send /cancel\n'\
                    'Example:'\

    format_name =   'Crowbot Hackathon'\

    format_desc =   '19th March 2002, 8:00AM\n'\
                    'Venue: Lab 2, Somebuildingname, Andheri West\n'\
                    'https://www\.google\.com/maps\n'\
                    'Entry Fee: Rs\. 000\n'\
                    'Other info:You can add any field, just insert it in a new line\.\n'\

    query = update.callback_query
    context.bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, parse_mode='MarkdownV2', text=add_instructions)
    # context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=add_instructions)
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=format_name)
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=format_desc)
    return TYPINGN

def del_event(update, context):
    del_instructions = 'Send me the *exact* name of the event to be deleted'
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text=del_instructions)
    return DELETING

def lis_event(update, context):
    # text = " ".join(context.args)
    query = update.callback_query
    text2s = 'These are the events:\n\n'
    evitem_descriptions = db.get_evitem_description()
    evitem_names = db.get_evitem_name()
    if len(evitem_names) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text='No ongoing or scheduled events\!')
    else:
        for i in range(len(evitem_names)):
            text2s = (text2s + '▫️' + evitem_names[i] + '\n' + evitem_descriptions[i] + '\n\n')
        # [[[[for name in evitem_names:
        #     for description in evitem_descriptions:
        #         text2s = (text2s + '▫️' + name + '\n' + description + '\n\n')
        # if item not in evitems:
        #     context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', text='No ongoing events\!')
        # else:
        # for item in evitems:
        #     text2s = (text2s + '▫️' + item + '\n\n')
        # text_start = 'Hello this is list']]]] ---depricated
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='MarkdownV2', disable_web_page_preview=True, text=text2s)

def cancelev(update, context):
    query = update.callback_query
    bot = context.bot
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="No problem!"
    )

# event_name = 'Hello'
def typingn(update, context):
    # global  event_name
    event_name = update.message.text
    # event_id = update.effective_message.message_id
    # context.bot.send_message(chat_id=update.effective_chat.id, text=event_name)
    db.add_evitem_name(event_name)
    # context.bot.send_message(chat_id=update.effective_chat.id, text='Event successfully added!')
    return TYPINGD

def typingd(update, context):
    event_desc = update.message.text
    event_desc_edit = event_desc.replace(".", "\.")
    event_desc_edit = event_desc_edit.replace("(", "\(")
    event_desc_edit = event_desc_edit.replace(")", "\)")
    event_desc_edit = event_desc_edit.replace("!", "\!")
    # context.bot.send_message(chat_id=update.effective_chat.id, text=event_desc_edit)
    db.add_evitem_description(event_desc_edit)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Event successfully added!')

def deleting(update, context):
    event_name = update.message.text
    db.delete_item(event_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Event successfully deleted!')

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    token = os.environ['TELEGRAM_TOKEN']

    updater = Updater(token, use_context=True)

    PORT = int(os.environ['PORT'])
    HEROKU_APP_NAME = os.environ['HEROKU_APP_NAME']
    updater.start_webhook(listen="0.0.0.0",
                                  port= PORT)
    updater.bot.set_webhook(url = 'https://{}.herokuapp.com/'.format(HEROKU_APP_NAME))
    # adding handlers...
    updater.dispatcher.add_error_handler(error)

    db.setup()

    updater.dispatcher.add_handler(CommandHandler('start', start))

    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.dispatcher.add_handler(CommandHandler('about', about))

    updater.dispatcher.add_handler(CommandHandler('faculty', faculty))

    updater.dispatcher.add_handler(CommandHandler('assignments', assignments))

    updater.dispatcher.add_handler(CommandHandler('experiments', experiments))

    # updater.dispatcher.add_handler(CommandHandler('timetable', timetable))

    updater.dispatcher.add_handler(CommandHandler('library', library))

    updater.dispatcher.add_handler(CommandHandler('cancel', cancelmain))

    # updater.dispatcher.add_handler(CommandHandler('events', events)) ----moved to conversationhandler


    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('events', events), CommandHandler('timetable', timetable)],

            states={
                EVENTM: [CallbackQueryHandler(lis_event, pattern='^' + str(LIST) + '$'),
                    CallbackQueryHandler(add_event, pattern='^' + str(ADD) + '$'),
                    CallbackQueryHandler(del_event, pattern='^' + str(DELETE) + '$'),
                    CallbackQueryHandler(cancelev, pattern='^' + str(CANCEL) + '$')],
                TYPINGN: [MessageHandler(Filters.text, typingn)],
                TYPINGD: [MessageHandler(Filters.text, typingd)],
                DELETING: [MessageHandler(Filters.text, deleting)],
                SENDTT: [CallbackQueryHandler(sendtt, pattern='^' + str(DIVA) + '$'),
                    CallbackQueryHandler(sendttb, pattern='^' + str(DIVB) + '$'),
                    CallbackQueryHandler(sendttc, pattern='^' + str(DIVC) + '$')]
            },
            fallbacks=[CommandHandler('events', events)]
        )
    updater.dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
