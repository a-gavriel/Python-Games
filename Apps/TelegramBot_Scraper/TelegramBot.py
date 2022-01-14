#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import scraper

bot_token = input("Please input bot token:")
if len(bot_token) < 5:
  print("Token error")
  exit()


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')



def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""

    

    if (update.message.text.lower() == "start thread"):
      scraper.create_thread(update.message.reply_text)

    elif (update.message.text.lower().find("timeout ") >= 0):
      scraper.change_timeout(update.message.text , update.message.reply_text)

    elif (update.message.text.lower() == "exit thread"):
      scraper.thread_running = False

    elif (update.message.text.lower() == "test"):
      scraper.del_blacklist()
      update.message.reply_text("Testing status: "+str(scraper.viagogo_test_blacklist))

    elif (update.message.text.lower() == "status"):
      result_list, results_log = scraper.check_pages()
      update.message.reply_text(str(results_log))
      
    else:
      update.message.reply_text("Command not found, message received:\n" + update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(bot_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

    scraper.thread_running = False
    print("reached end.")


if __name__ == '__main__':
    main()