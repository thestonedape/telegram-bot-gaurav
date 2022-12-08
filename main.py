
from telegram.ext import *
import Responses as R 

KEY = bot('APIKEY')





print("The RSCOE AR Bot has now been started...")

def start_command(update, context):
    update.message.reply_text('Type something random to Begin with!')

def help_command(update, context):
    update.message.reply_text('If you need help, contact the creator of this bot: Gaurav :gaurav31308@#jspmrscoe.edu.in')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)
def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp= updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()    
