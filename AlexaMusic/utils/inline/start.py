from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from AlexaMusic import app




def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="<اوامر التشغيل>",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="<الاعدادات>", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافه البوت لمجموعتك",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="<اوامر التشغيل>", callback_data="settings_back_helper"
            ), 
            InlineKeyboardButton(
                text="<طريقه التفعيل>", callback_data="help_callback hb6"
             )
        ],
        [
            InlineKeyboardButton(
                text="<مطور البوت>", user_id=OWNER
            ), 
            InlineKeyboardButton(
                text="<مطور السورس>", url=f"https://t.me/ah_2_v"
            )
        ],
        [ 
            InlineKeyboardButton(
                text="<قناة السورس>", url=f"https://t.me/ah07v"
             )
        ],
        [
            InlineKeyboardButton(
                text="اللغة ↩️", callback_data="LG"
            )
        ],
     ]
    return buttons
