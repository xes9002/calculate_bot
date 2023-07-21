from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def calc_btn():
    keyboards = InlineKeyboardMarkup(row_width=4)
    keyboards.add(
        InlineKeyboardButton('©️', callback_data='C'),
        InlineKeyboardButton('🔙', callback_data='<'),
        InlineKeyboardButton('%', callback_data='%'),
        InlineKeyboardButton('➗', callback_data='/')
    )
    keyboards.add(
        InlineKeyboardButton('7️⃣', callback_data='7'),
        InlineKeyboardButton('8️⃣', callback_data='8'),
        InlineKeyboardButton('9️⃣', callback_data='9'),
        InlineKeyboardButton('✖️', callback_data='*')
    )
    keyboards.add(
        InlineKeyboardButton('4️⃣', callback_data='4'),
        InlineKeyboardButton('5️⃣', callback_data='5'),
        InlineKeyboardButton('6️⃣', callback_data='6'),
        InlineKeyboardButton('➖', callback_data='-')
    )
    keyboards.add(
        InlineKeyboardButton('1️⃣', callback_data='1'),
        InlineKeyboardButton('2️⃣', callback_data='2'),
        InlineKeyboardButton('3️⃣', callback_data='3'),
        InlineKeyboardButton('➕', callback_data='+')
    )
    keyboards.add(
        InlineKeyboardButton('.', callback_data='.'),
        InlineKeyboardButton('0️⃣', callback_data='0'),
        InlineKeyboardButton('**', callback_data='**'),
        InlineKeyboardButton('🟰', callback_data='=')
    )
    return keyboards
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def calc_btn():
    btn = InlineKeyboardMarkup(row_width=4)
    btn.add(
        InlineKeyboardButton('©️', callback_data='clear'),
        InlineKeyboardButton('🔙', callback_data='back'),
        InlineKeyboardButton('%', callback_data='equ:%'),
        InlineKeyboardButton('➗', callback_data='equ:/')
    )
    btn.add(
        InlineKeyboardButton('7️⃣', callback_data='num:7'),
        InlineKeyboardButton('8️⃣', callback_data='num:8'),
        InlineKeyboardButton('9️⃣', callback_data='num:9'),
        InlineKeyboardButton('✖️', callback_data='equ:*')
    )
    btn.add(
        InlineKeyboardButton('4️⃣', callback_data='num:4'),
        InlineKeyboardButton('5️⃣', callback_data='num:5'),
        InlineKeyboardButton('6️⃣', callback_data='num:6'),
        InlineKeyboardButton('➖', callback_data='equ:-')
    )
    btn.add(
        InlineKeyboardButton('1️⃣', callback_data='num:1'),
        InlineKeyboardButton('2️⃣', callback_data='num:2'),
        InlineKeyboardButton('3️⃣', callback_data='num:3'),
        InlineKeyboardButton('➕', callback_data='equ:+')
    )
    btn.add(
        InlineKeyboardButton(',', callback_data=','),
        InlineKeyboardButton('0️⃣', callback_data='num:0'),
        InlineKeyboardButton('', callback_data='equ:'),
        InlineKeyboardButton('🟰', callback_data='result')
    )
    return btn

