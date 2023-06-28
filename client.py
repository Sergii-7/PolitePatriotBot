from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json
import string

b1 = KeyboardButton('/news')
b2 = KeyboardButton('/donation')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b1).insert(b2)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    mess = f'Hello, {message.from_user.first_name} {message.from_user.last_name}!'
    try:
        await bot.send_message(message.from_user.id, mess, reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('спілкування з ботом через особисте повідомлення,\
        напиши йому:\nhttps://t.me/PolitePatriotBot')

@dp.message_handler(commands=['news'])
async def menu_commands(message: types.Message):
    new_en = 'https://t.me/ukraine_now_eng'
    new = 'https://t.me/u_now_ua'
    await bot.send_message(message.from_user.id, new_en)
    await bot.send_message(message.from_user.id, new)

@dp.message_handler(commands=['donation'])
async def menu_commands(message: types.Message):
    help_en = '''The National Bank of Ukraine praised the decision to open a special fundraiser for the collection of coins to support the Healthy Forces of Ukraine.
Requisites of the official special account: UA843000010000000047330992708
Rahunok is multi-currency, it is used for transferring funds to international partners and donors - in foreign currencies (US dollars, euros, British pounds), and in Ukrainian business and citizens - in national currencies.
Support the Ukrainian Army!
Glory to Ukraine! 🇺🇦'''
    help_ua = '''Національний банк України ухвалив рішення відкрити спеціальний рахунок для збору коштів на підтримку Збройних Сил України.
Реквізити офіційного спеціального рахунку: UA843000010000000047330992708
Рахунок – мультивалютний, він створений та відкритий як для переказу коштів від міжнародних партнерів та донорів – у іноземній валюті (долари США, євро, британські фунти), так і від українського бізнесу та громадян – у національній валюті.
Підтримуємо Українську Армію! 
Слава Україні! 🇺🇦'''
    await bot.send_message(message.from_user.id, help_en)
    await bot.send_message(message.from_user.id, help_ua)

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(menu_commands, commands=['news'])
    dp.register_message_handler(menu_commands, commands=['donation'])


@dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('censorship.json')))) != set():
        await message.reply('Матюки в чаті заборонені!')
        await message.delete()
    elif {i.lower().translate(str.maketrans('','',string.punctuation)) for i in message.text.split(' ')}\
            .intersection(set(json.load(open('cens_english.json')))) != set():
        await message.reply('Profanity is prohibited in the chat!')
        await message.delete()
    elif message.text.lower() == 'ukr':
        await message.answer('🇺🇦 понад усе!')
    elif message.text.lower()[0:13] == 'слава україні' or message.text.lower()[0:13] == 'слава украине':
        await message.answer('Героям Слава!')
    elif message.text.lower()[0:8] == 'слава 🇺🇦':
        await message.answer('Героям Слава!')
    elif message.text.lower()[0:11] == 'слава нації':
        await message.answer('Смерь ворогам!')
    elif message.text.lower()[0:13] == 'руський кораб' or message.text.lower()[0:12] =='руский кораб' \
            or message.text.lower()[0:13] == 'русcкий кораб':
        await message.answer('Іди геть!')

    for n in message.text.split(' '):
        if n.lower()[0:6] == 'привіт' or n.lower() == 'привет':
            await message.reply('Hello!')
            break
        elif n.lower()[0:7] == 'доброго':
            await message.reply('Hello!')
            break
        elif n.lower()[0:5] == 'hello':
            await message.reply('Hello!')
            break
        elif n.lower() == 'hi' or n.lower() == 'hi!' or n.lower() == 'hi)' \
                or n.lower() == 'hi:)':
            await message.reply('Hello!')
            break
        elif n.lower() == '🇺🇦' or n.lower()[0:7] == 'ukraine' or n.lower()[0:7] == 'украина'\
                or n.lower()[0:7] == 'україна':
            await message.answer('🇺🇦 понад усе!')
            break

        elif n == 'россия' or n == 'росия'  or n == 'росія' or n == 'расія' or n == 'росєя' or n == 'расєя':
            await message.reply('Так вірно! Ця країна пишеться з маленької літери')
            break
        elif n == 'Россия' or n == 'Рассия':
            await message.reply('Неправильна назва! Треба расєя чи рашка чи лаптістан')
            break
        elif n.lower() == 'братья':
            await message.reply('https://www.youtube.com/watch?v=QJvOlSXBHVs')
            break
        elif n.lower() == 'путин' or n.lower() == 'путін' or n.lower() == 'путлер':
            await message.reply('путін - Ху*ло!')
            break
        for i in n:
            rus = ['ы', 'ё', 'ъ', 'э']
            if i.lower() in rus:
                await message.reply('Вибачте, але я цю мову не розумію!')
        break

def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)
