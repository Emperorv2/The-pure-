import os
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters
from utils import log_message
from database import save_to_db

# Initialize bot
bot = Bot(token=os.getenv("7926932377:AAFE1XjTljwJqLQHcu_6mZ0JYp1i2GtnxuA"))
dispatcher = Dispatcher(bot, None, use_context=True)

def handler(event, context):
    try:
        update = Update.de_json(event.get("body"), bot)
        dispatcher.process_update(update)
        return {"statusCode": 200, "body": "OK"}
    except Exception as e:
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

# Register handlers
def text_handler(update, context):
    user_id = update.message.from_user.id
    text = update.message.text
    save_to_db(user_id, text)  # Save to cloud DB
    update.message.reply_text(f"Logged: {text}")

dispatcher.add_handler(MessageHandler(Filters.text, text_handler))