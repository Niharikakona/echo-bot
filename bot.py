import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def hello(update, context):
    update.message.reply_text('Hello niha')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    if update.message.text =="age":
        update.message.reply_text("20")
    else:
        update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""

    updater = Updater("1581640003:AAHg6UiHEyoYuDtGHJszsOCR6ChWJl2Kr0U", use_context=True)

    
    dp = updater.dispatcher

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("hello", hello))

    
    dp.add_handler(CommandHandler("help", help))


    dp.add_handler(MessageHandler(Filters.text, echo))

    
    dp.add_error_handler(error)

    
    updater.start_webhook(listen="0.0.0.0",port=PORT,url_path="1581640003:AAHg6UiHEyoYuDtGHJszsOCR6ChWJl2Kr0U")
    
    updater.bot.set_webhook("https://tubelight-echo-bot.herokuapp.com/" + "1581640003:AAHg6UiHEyoYuDtGHJszsOCR6ChWJl2Kr0U")

    
    updater.idle()


if __name__ == '__main__':
    main()