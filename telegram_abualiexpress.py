import configparser
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Read the token from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the bot token
TOKEN = config['TelegramBot']['token']

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Use /read to get the latest messages from the group.')

def read_messages(update: Update, context: CallbackContext) -> None:
    # Replace 'your_group_chat_id' with your actual group chat ID
    group_chat_id = -100123456789  # Use a negative sign for group chat IDs

    # Get the last 10 messages from the group
    messages = context.bot.get_chat_history(chat_id=group_chat_id, limit=10)

    for message in messages:
        update.message.reply_text(f"{message.from_user.username}: {message.text}")

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("read", read_messages))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
