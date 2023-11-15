import configparser
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Read the token from the config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Get the bot token
TOKEN = config['TelegramBot']['token']




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def read_messages(update: Update, context: CallbackContext) -> None:
    # using @abualiexpress as group chat ID
    group_chat_id = -100123456789  # Use a negative sign for group chat IDs

    # Get the last 10 messages from the group
    messages = context.bot.get_chat_history(chat_id=group_chat_id, limit=10)

    for message in messages:
        await update.message.reply_text(f"{message.from_user.username}: {message.text}")


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(read_messages)
    
    application.run_polling()

if __name__ == '__main__':
    main()
