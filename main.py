# from telegram.ext import Updater, CommandHandler
#
# def satrt_command(update,context):
#     print(update)
#     print(update.message.text)
#     print(update.message.from_user)
#     update.message.reply_text(text="Siz /start kamandasini kiritdingiz!")
#     context.bot.send_message(chat_id="1302588424", text="ikkinchi xabar")
#
# def main():
#     updater = Updater("1448697325:AAHGXAnxe-b8Ik4TURvmFVws483gRYkHk4k")
#     dispatcher = updater.dispatcher
#
#     dispatcher.add_handler(CommandHandler('start', satrt_command))
#
#     updater.start_polling()
#     updater.idle()
# if __name__ == '__main__':
#     main()


from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, ConversationHandler
from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, ChatAction
)
# from vazifa_3 import car_video

CHANNEL_ID = -1001261519461
GLOBAL_LIKE = 0
GLOBAL_DISLIKE = 0
GLOBAL_OK_HAND = 0
GLOBAL_CLAP = 0


def start_handler(update, context):
    context.bot.send_photo(
        chat_id=CHANNEL_ID,
        photo=open("image\\dodge1.jpg", "rb"),
        caption="Dodge Challenger Photo",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="👍", callback_data="like"),
                 InlineKeyboardButton(text="👎", callback_data="dislike"),
                 InlineKeyboardButton(text="👌", callback_data="ok_hand"),
                 InlineKeyboardButton(text="👏", callback_data="clap")],
                [InlineKeyboardButton(text="Video", callback_data="video")]
            ]
        )
    )
    update.message.reply_text(text="Xabar jo'natildi!")


def message_handler(update, context):
    pass


def inline_handler(update, context):
    global GLOBAL_LIKE, GLOBAL_DISLIKE, GLOBAL_CLAP, GLOBAL_OK_HAND
    query = update.callback_query
    # chat_id = query.message.chat_id
    # message_id = query.message.message_id
    print(query.data)
    if query.data == "like":
        if context.user_data.get('choice') == "dislike":
            GLOBAL_DISLIKE -= 1
        if context.user_data.get('choice') == "clap":
            GLOBAL_CLAP -= 1
        if context.user_data.get('choice') == "ok_hand":
            GLOBAL_OK_HAND -= 1
        if context.user_data.get('choice') != "like":
            GLOBAL_LIKE += 1
        context.user_data["choice"] = "like"

    if query.data == "dislike":
        if context.user_data.get('choice') == "like":
            GLOBAL_LIKE -= 1
        if context.user_data.get('choice') == "clap":
            GLOBAL_CLAP -= 1
        if context.user_data.get('choice') == "ok_hand":
            GLOBAL_OK_HAND -= 1
        if context.user_data.get('choice') != "dislike":
            GLOBAL_DISLIKE += 1
        context.user_data["choice"] = "dislike"

    if query.data == "ok_hand":
        if context.user_data.get('choice') == "dislike":
            GLOBAL_DISLIKE -= 1
        if context.user_data.get('choice') == "like":
            GLOBAL_LIKE -= 1
        if context.user_data.get('choice') == "clap":
            GLOBAL_CLAP -= 1
        if context.user_data.get('choice') != "ok_hand":
            GLOBAL_OK_HAND += 1
        context.user_data['choice'] = "ok_hand"

    if query.data == "clap":
        if context.user_data.get('choice') == "dislike":
            GLOBAL_DISLIKE -= 1
        if context.user_data.get('choice') == "like":
            GLOBAL_LIKE -= 1
        if context.user_data.get('choice') == "ok_hand":
            GLOBAL_OK_HAND -= 1
        if context.user_data.get('choice') != "clap":
            GLOBAL_CLAP += 1

        context.user_data['choice'] = "clap"

    if query.data == "video":
        print("hello")
        context.bot.send_video(
            chat_id=CHANNEL_ID,
            video=open("video\\drift.mp4", "rb"),
            caption="Dodge Challenger Drift",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="👍", callback_data="like"),
                     InlineKeyboardButton(text="👎", callback_data="dislike"),
                     InlineKeyboardButton(text="👌", callback_data="ok_hand"),
                     InlineKeyboardButton(text="👏", callback_data="clap")]
                ]
            )
        )

    try:
        context.bot.edit_message_reply_markup(
            chat_id=CHANNEL_ID,
            message_id=query.message.message_id,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text=f"👍{GLOBAL_LIKE}", callback_data=f"like"),
                     InlineKeyboardButton(text=f"👎{GLOBAL_DISLIKE}", callback_data=f"dislike"),
                     InlineKeyboardButton(text=f"👌{GLOBAL_OK_HAND}", callback_data=f"ok_hand"),
                     InlineKeyboardButton(text=f"👏{GLOBAL_CLAP}", callback_data=f"clap")]
                ]
            )
        )
    except Exception as e:
        print(e)

        # context.bot.answer_callback_query(
        #     show_alert=True, callback_query_id=query.id,
        #     text="Salom Brat"
        # )


def main():
    updater = Updater("1866496825:AAEshv8g8onXqtKGe2ZDbBKg8eNw8WwjjLg")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

