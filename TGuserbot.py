from pyrogram import Client, filters, __version__ as pyrogram_version
from pyrogram.types import Message
import pyrogram
import random
import time
import re
import uuid
import socket
from datetime import datetime, timedelta
import pytz
import psutil
from sympy import sympify
from typing import List
import requests
import asyncio
from collections import defaultdict
from typing import List
import aiohttp
import os
import qrcode
import sympy
from sympy.parsing.sympy_parser import parse_expr
import wikipedia
from bs4 import BeautifulSoup
from pyrogram import emoji
from collections import defaultdict
import string 
from PIL import Image
import binascii
import subprocess
import numpy as np
import logging 
from threading import Thread
import math 
from sympy import latex, simplify
from sympy import symbols
from sympy import cos, sin, pi
import ctypes
import speedtest 

# Setup logging in a separate thread
def logging_thread():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('pyrogram')
    logger.setLevel(logging.WARNING)

    # Здесь можно добавить любую другую логику логирования, если это необходимо.

# Запуск потока логирования
thread = Thread(target=logging_thread)
thread.start()

# Путь к рабочей папке
folder_path = "C:/Userbot"

# Проверка и создание рабочей папки, если она не существует
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Создание инструкций на русском языке
instructions = """Для получения API ID и API HASH:
1. Перейдите на https://my.telegram.org/
2. Войдите и перейдите в инструменты разработчика API.
3. Создайте новое приложение и скопируйте API ID и API HASH.
4. Заполните значения при запуске программы.
"""

# Сохранение инструкций в файл
instructions_path = os.path.join(folder_path, 'instructions.txt')
with open(instructions_path, 'w') as file:
    file.write(instructions)

# Создание файла с благодарностью
thx_text = "Сыпасибо за пользование Userbot! "
thx_path = os.path.join(folder_path, 'Thx.txt')
with open(thx_path, 'w') as file:
    file.write(thx_text)

# Путь к файлу конфигурации
file_path = os.path.join(folder_path, 'config.txt')

# Проверка наличия файла и чтение API ID и API HASH
api_id = ""
api_hash = ""
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) >= 2:
            api_id = lines[0].strip()
            api_hash = lines[1].strip()

# Если API ID и API HASH не записаны, запросить пользователя
if not api_id or not api_hash:
    api_id = input("Введите ваш API ID: ")
    api_hash = input("Введите ваш API HASH: ")

    # Сохранение значений в файл
    with open(file_path, 'w') as file:
        file.write(api_id + "\n" + api_hash)

# Ваш токен для бота Pyrogram
app = Client("my_bot", api_id=api_id, api_hash=api_hash)
            
@app.on_message(filters.command("readall", prefixes=".") & filters.me)
async def read_all_messages(client, message):
    # Inform the user that the process has started.
    await message.edit("Обработка уведомлений...")
    
    async for dialog in app.get_dialogs():
        await app.read_chat_history(dialog.chat.id)
    
    # Edit the message after all chats have been marked as read.
    await message.edit("Все уведомления прочитаны!")

@app.on_message(filters.command("off", prefixes="."))
def turn_off_pc(client, message):
    os.system("shutdown /s /t 0")
    client.edit_message_text(message.chat.id, message.message_id, "Компьютер будет выключен.")
    
@app.on_message(filters.command("connet", prefixes="."))
def ipconfig_command(client, message):
    # Execute the 'ipconfig' command and decode the output from cp866 encoding to Unicode
    ipconfig_output = subprocess.check_output("ipconfig", shell=True).decode("cp866")
    
    # Create a formatted version of the IP configuration output
    formatted_output = """
⚙️ Network Configuration:

{}
""".format(ipconfig_output).strip()

    if message.reply_to_message:
        # Edit the original message with the formatted output
        client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.reply_to_message.message_id,
            text=formatted_output
        )
    else:
        # Send a new message with the formatted output
        sent_message = client.send_message(
            chat_id=message.chat.id,
            text=formatted_output
        )
    
@app.on_message(filters.command("res", prefixes="."))
def reboot_pc(client, message):
    os.system("shutdown /r /t 0")
    client.edit_message_text(message.chat.id, message.message_id, "Компьютер будет перезагружен.")  
        
@app.on_message(filters.command("leto", prefixes="."))
def count_down_to_summer(client, message: Message):
    summer_date = datetime(datetime.now().year, 6, 1, 0, 0, 0, tzinfo=pytz.utc)  # Время начала лета с информацией о смещении временной зоны (UTC)
    
    if datetime.now(tz=pytz.utc) > summer_date:
        summer_date = datetime(datetime.now().year + 1, 6, 1, 0, 0, 0, tzinfo=pytz.utc)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = summer_date - current_time
    total_days = time_difference.total_seconds() / (24*60*60)    
    total_seconds = time_difference.total_seconds()
    months = total_seconds // (30*24*60*60)
    total_seconds %= (30*24*60*60)
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if months == 0 and days == 0:
        time_left = "🎉 Лето уже началось! 🌞"
    else:
        time_left = f"⏳ До начала лета осталось: {int(total_days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"
    
    total_days = time_difference.total_seconds() / (24*60*60)

    try:
        message.edit(f"{time_left}")
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")

@app.on_message(filters.command("ng", prefixes="."))
def count_down_to_new_year(client, message: Message):
    new_year_date = datetime(datetime.now().year + 1, 1, 1, 0, 0, 0, tzinfo=pytz.utc)  # Время начала следующего года с информацией о смещении временной зоны (UTC)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = new_year_date - current_time
        
    total_seconds = time_difference.total_seconds()
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if days == 0:
        time_left = "🎉 C Новым Годом! 🎆"
    else:
        time_left = f"⏳ До Нового Года осталось: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"

    try:
        message.edit(time_left)
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")

@app.on_message(filters.command("womenday", prefixes="."))
def count_down_to_women_day(client, message: Message):
    women_day_date = datetime(datetime.now().year, 3, 8, 0, 0, 0, tzinfo=pytz.utc)  # Время 8 марта текущего года с информацией о смещении временной зоны (UTC)
    
    if datetime.now(tz=pytz.utc) > women_day_date:
        women_day_date = datetime(datetime.now().year + 1, 3, 8, 0, 0, 0, tzinfo=pytz.utc)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = women_day_date - current_time
        
    total_seconds = time_difference.total_seconds()
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if days == 0:
        time_left = "🎉 Праздник уже сегодня!"
    else:
        time_left = f"⏳ До 8 Марта осталось: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"

    try:
        message.edit(time_left)
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")


@app.on_message(filters.command("14feb", prefixes="."))
def count_down_to_valentines_day(client, message: Message):
    valentines_day_date = datetime(datetime.now().year, 2, 14, 0, 0, 0, tzinfo=pytz.utc)  # Время 14 февраля текущего года с информацией о смещении временной зоны (UTC)
    
    if datetime.now(tz=pytz.utc) > valentines_day_date:
        valentines_day_date = datetime(datetime.now().year + 1, 2, 14, 0, 0, 0, tzinfo=pytz.utc)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = valentines_day_date - current_time
        
    total_seconds = time_difference.total_seconds()
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if days == 0:
        time_left = "🎉 С Днём Святого Валентина! ❤️"
    else:
        time_left = f"⏳ До Дня Святого Валентина осталось: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"

    try:
        message.edit(time_left)
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")  

@app.on_message(filters.command("1sen", prefixes="."))
def count_down_to_students_day(client, message: Message):
    students_day_date = datetime(datetime.now().year, 9, 1, 0, 0, 0, tzinfo=pytz.utc)  # Время 1 сентября текущего года с информацией о смещении временной зоны (UTC)
    
    if datetime.now(tz=pytz.utc) > students_day_date:
        students_day_date = datetime(datetime.now().year + 1, 9, 1, 0, 0, 0, tzinfo=pytz.utc)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = students_day_date - current_time
        
    total_seconds = time_difference.total_seconds()
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if days == 0:
        time_left = "🎉 С Днём Знаний! 📚"
    else:
        time_left = f"⏳ До Дня Знаний осталось: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"

    try:
        message.edit(time_left)
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")  

@app.on_message(filters.command("23feb", prefixes="."))
def count_down_to_defender_day(client, message: Message):
    defender_day_date = datetime(datetime.now().year, 2, 23, 0, 0, 0, tzinfo=pytz.utc)  # Время 23 февраля текущего года с информацией о смещении временной зоны (UTC)
    
    if datetime.now(tz=pytz.utc) > defender_day_date:
        defender_day_date = datetime(datetime.now().year + 1, 2, 23, 0, 0, 0, tzinfo=pytz.utc)
    
    current_time = datetime.now(tz=pytz.utc)  # Текущее время с информацией о смещении временной зоны (UTC)
    time_difference = defender_day_date - current_time
        
    total_seconds = time_difference.total_seconds()
    days = total_seconds // (24*60*60)
    total_seconds %= (24*60*60)
    hours = total_seconds // 3600
    total_seconds %= 3600
    minutes = total_seconds // 60
    seconds = total_seconds % 60
        
    if days == 0:
        time_left = "🎉 С Днём защитника Отечества! 🎖️"
    else:
        time_left = f"⏳ До Дня защитника Отечества осталось: {int(days)} дней, {int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"

    try:
        message.edit(time_left)
    except Exception as e:
        print(f"Ошибка при обновлении сообщения: {e}")

#    РАНДОМ
#    РАНДОМ
#    РАНДОМ
#    РАНДОМ
#    РАНДОМ
def generate_random_rating(total_stars):
    return random.randint(1, total_stars)

def generate_stars(rating, total_stars):
    return '★' * rating + '☆' * (total_stars - rating)

def estimate(phrase_and_stars):
    responses = []
    for pair in phrase_and_stars:
        phrase, total_stars = pair
        
        ratings = [generate_random_rating(total_stars) for _ in range(len(phrase))]
        
        total_rating = sum(ratings)
        average_rating = total_rating // len(phrase)
        stars = generate_stars(average_rating, total_stars)
        response = f"{phrase}: {stars} {average_rating} звезд ({total_stars} лимит)"
        responses.append(response)
    
    return responses

# Обработка команды .est
@app.on_message(filters.command("est", prefixes="."))
def estimate_command(client, message):
    try:
        # Получаем фразу и общее количество звезд
        parts = message.text.split()[1:]
        phrase = ' '.join(parts[:-1])
        total_stars = int(parts[-1])
        
        responses = estimate([(phrase, total_stars)])
        response_text = '\n'.join(responses)
        
        message.edit_text(response_text)
    except Exception as e:
        message.edit_text(str(e))

@app.on_message(filters.command("ran", prefixes="."))
def random_number(client, message):
    try:
        command, *args = message.text.split()
        if len(args) < 2:
            message.edit_text("Пожалуйста, используйте команду в формате: .random <минимальное_значение> <максимальное_значение> [количество_повторений]")
            return

        min_num = int(args[0])
        max_num = int(args[1])
        repetitions = 1

        if len(args) > 2:
            repetitions = int(args[2])

        random_numbers = [str(random.randint(min_num, max_num)) for _ in range(repetitions)]
        result_text = f"\n" + "\n".join(random_numbers)
        message.edit_text(result_text)
    except (ValueError, TypeError):
        message.edit_text("Пожалуйста, используйте команду в формате: .random <минимальное_значение> <максимальное_значение> [количество_повторений]")
         
@app.on_message(filters.command("cir", prefixes="."))
async def circle(client, message: Message):
    values = message.text.split(" ")[1:]
    
    if len(values) < 2:
        await message.reply_text("❌ Укажите минимум 2 значения для колеса фортуны.")
        return

    total_values = len(values)
    probabilities = [1 / total_values] * total_values

    result = random.choices(values, probabilities)[0]
    await message.edit_text(f"🎡 Колесо фортуны выбрало: {result}")
 
@app.on_message(filters.command("ranru", prefixes="."))
async def random_ru(client, message: Message):
    try:
        count = int(message.text.split(" ")[1])
    except (IndexError, ValueError):
        await message.edit_text("Укажите кол-во повторения после команды.")
        return
        
    result = " ".join([random.choice("абвгдеёжзийклмнопрстуфхцчшщъыьэюя") for _ in range(count)])
    await message.edit_text(result)


@app.on_message(filters.command("ranen", prefixes="."))
async def random_en(client, message: Message):
    try:
        count = int(message.text.split(" ")[1])
    except (IndexError, ValueError):
        await message.edit_text("Укажите кол-во повторения после команды.")
        return
        
    result = " ".join([random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(count)])
    await message.edit_text(result)

@app.on_message(filters.command("reverse", prefixes="."))
def reverse_text(client, message: Message):
    text = message.text.split(" ", 1)
    if len(text) == 2:
        reversed_text = text[1][::-1]
        message.edit(f"{reversed_text}")
        
@app.on_message(filters.command("randate", prefixes="."))
def random_date(client, message: Message):
    try:
        # Разделить введенную команду на начальную и конечную дату
        date_range = message.text.split(" ")[1].split("-")
        
        # Преобразовать строковые даты в объекты datetime
        start_date = datetime.strptime(date_range[0], "%d.%m.%Y")
        end_date = datetime.strptime(date_range[1], "%d.%m.%Y")
        
        # Рассчитать диапазон в днях между начальной и конечной датами
        delta = (end_date - start_date).days
        
        if delta >= 0:
            # Сгенерировать случайное количество дней с учетом диапазона
            random_days = random.randint(0, delta)
            
            # Добавить случайное количество дней к начальной дате
            random_date = start_date + timedelta(days=random_days)
            
            # Отредактировать сообщение и вывести сгенерированную дату в формате "DD.MM.YYYY"
            message.edit(f"Случайная дата: {random_date.strftime('%d.%m.%Y')}")
        else:
            message.edit("Ошибка: Начальная дата должна быть раньше конечной даты.")
            
    except Exception as e:
        # Если возникает ошибка, отобразить сообщение об ошибке
        message.edit(f"Ошибка: {e}")    
#    Генератор
#    Генератор
#    Генератор
#    Генератор
#    Генератор
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = random.choice(["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com", "protonmail.com", "zoho.com", "mail.com", "yandex.com", "gmx.com", "inbox.com", "tutanota.com", "fastmail.com", "mail.ru", "live.com", "earthlink.net", "cox.net", "verizon.net", "att.net", "me.com", "aol.co.uk", "rocketmail.com", "sbcglobal.net", "ymail.com", "comcast.net", "juno.com", "optonline.net", "charter.net"])
    email = f"{username}@{domain}"
    return email

@app.on_message(filters.command("email", prefixes="."))
def gen_email(client, message):
    email = generate_email()
    
    # Отправка сгенерированной электронной почты без ответа на сообщение и без задержки
    client.send_message(message.chat.id, f"{email}")

    # Удаление сообщения с командой .genEmail
    message.delete()

def gen_russia():
    return random.randint(100000, 999999)

def gen_index(country):
    if country == "Россия":
        return gen_russia()
    else:
        return "Неверная страна"

def generate_index(client, message):
    country = "Россия"
    index = gen_index(country)
    client.send_message(message.chat.id, f"Страна: {country}\nИндекс: {index}")
    message.delete()

@app.on_message(filters.command("index", prefixes="."))
def generate_index_command(client, message):
    generate_index(client, message)
    
@app.on_message(filters.command("pas", prefixes="."))
def generate_password(client, message: Message):
    command = message.text.split(" ")
    if len(command) == 1:
        message.edit("Введите длину пароля после команды, например: .pas 12")
    elif len(command) == 2:
        try:
            length = int(command[1])
            if length > 0:
                password = "".join(random.choices("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()", k=length))
                message.delete()  # Удаляем сообщение с командой
                app.send_message(message.chat.id, f"Сгенерированный пароль: `{password}`")
            else:
                message.edit("Длина пароля должна быть больше 0")
        except ValueError:
            message.edit("Неверный формат длины")

@app.on_message(filters.command("ip", prefixes="."))
async def generate_ip(client, message):
    await message.delete()  # Удаляем сообщение с командой
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))  # Генерируем случайный IP-адрес
    await client.send_message(message.chat.id, ip) 
 
@app.on_message(filters.command("speedtest", prefixes="."))
async def speed_test(client, message):
    st = speedtest.Speedtest()
    
    # Получаем лучший сервер один раз и кэшируем его
    st.get_best_server()
    
    # Выполняем измерения скорости загрузки и выгрузки
    download_speed = await asyncio.to_thread(st.download) / 1024 / 1024
    upload_speed = await asyncio.to_thread(st.upload) / 1024 / 1024

    await message.edit_text(f"Скорость загрузки: {download_speed:.2f} Mb/s\nСкорость выгрузки: {upload_speed:.2f} Mb/s")
            
@app.on_message(filters.command("qr", prefixes="."))
async def generate_qr(client, message: Message):
    if len(message.text.split()) == 1:  # Проверяем, есть ли аргументы после команды
        await message.reply("Пожалуйста, укажите текст для создания QR-кода после команды .qr")
        return
    
    args = message.text.split(".qr ", 1)[1]  # Получаем все аргументы после ".qr "
    
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?data={args}&size=300x300"
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(qr_code_url) as resp:
                if resp.status == 200:
                    qr_code_filename = "qr_code.png"
                    with open(qr_code_filename, "wb") as f:
                        f.write(await resp.read())
                        
                    await message.delete(revoke=True)
                    await message.reply_photo(photo=qr_code_filename)  # Отвечаем сообщением с фото QR-кода
                    
                    os.remove(qr_code_filename)  # Удалить временный файл после отправки
                else:
                    await message.reply("Не удалось сгенерировать QR-код. Пожалуйста, попробуйте снова.")
    except Exception as e:
        print(e)
        await message.reply("Произошла ошибка при генерации QR-кода. Пожалуйста, попробуйте снова.")
        
def generate_mac_address():
    mac_chars = "0123456789ABCDEF"
    mac_address = ":".join("".join(random.choices(mac_chars, k=2)) for _ in range(6))
    return mac_address

@app.on_message(filters.command("MAC", prefixes="."))
async def generate_mac(client, message):
    mac = generate_mac_address()
    await message.delete()  # Удаляем сообщение с командой
    await client.send_message(message.chat.id, f"{mac}")


@app.on_message(filters.command("linkW", prefixes="."))
async def generate_link_w(client, message):
    number = message.text.split(" ", maxsplit=1)[1]
    if number.startswith("+"):
        number = number[1:]
        
    whatsapp_link = f"https://wa.me/{number}"
    await message.edit(f"WhatsApp Link: {whatsapp_link}")

@app.on_message(filters.command("linkSt", prefixes="."))
async def generate_link_st(client, message):
    args = message.text.split()[1:]
    steam_username = args[0]
    steam_link = f"https://steamcommunity.com/id/{steam_username}"
    await message.edit(f"Steam Link: {steam_link}")

@app.on_message(filters.command("linkT", prefixes="."))
async def generate_link_t(client, message):
    number = message.text.split(" ", maxsplit=1)[1]
    telegram_link = f"https://t.me/+{number}"
    await message.edit(f"Telegram Link: {telegram_link}")

@app.on_message(filters.command("linkVK", prefixes="."))
def generate_vk_link(client, message):
    if len(message.text.split()) == 2:
        username = message.text.split()[1]
        vk_link = f"https://vk.com/{username}"
        
        message.edit(f"Ссылка на профиль пользователя {username}: {vk_link}")
    else:
        message.edit("Некорректное использование команды. Пожалуйста, укажите юзернейм после команды.")

#    Кастом
#    Кастом
#    Кастом
#    Кастом
#    Кастом
@app.on_message(filters.command("typev1", prefixes='.') & filters.me)
def type(client_object, message: Message):
    input_text = message.text.split(".typev2 ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "✹"

    while edited_text != input_text:
        try:
            message.edit(edited_text + typing_symbol)
            time.sleep(0.05)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            message.edit(edited_text)
            time.sleep(0.05)
        except Exception as e:
            print(f"Error: {e}")
            break
        
@app.on_message(filters.command("dis", prefixes="."))
def solve_discriminant(_, message):
    try:
        args = message.text.split()[1:]
        a, b, c = map(float, args)

        # Вычисление дискриминанта
        discriminant = b**2 - 4*a*c
        discriminant_str = f"Дискриминант: {discriminant:.6g}"

        # Пошаговое решение
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            solution = f"x₁ = {x1:.6g}\nx₂ = {x2:.6g}"
            steps = f"x₁ = (-b + √D) / 2a = ({ -b:.6g} + {math.sqrt(discriminant):.6g}) / {2*a:.6g} = {x1:.6g}\nx₂ = (-b - √D) / 2a = ({ -b:.6g} - {math.sqrt(discriminant):.6g}) / {2*a:.6g} = {x2:.6g}"
            roots_message = "Два различных решения."
        elif discriminant == 0:
            x = -b / (2*a)
            solution = f"x = {x:.6g}"
            steps = f"x = -b / 2a = { -b:.6g} / {2*a:.6g} = {x:.6g}"
            roots_message = "Одно решение (кратный корень)."
        else:
            solution = "Нет решений."
            roots_message = "Нет решений."
            steps = ""

        # Редактируем исходное сообщение с командой
        message.edit_text(f"{discriminant_str}\n\n{steps}\n\n{roots_message}\n\nРешение:\n{solution}")

    except (ValueError, IndexError):
        message.reply_text("Неправильный ввод. Пожалуйста, введите команду в формате '.dis a b c'")

@app.on_message(filters.command("sin", prefixes="."))
def sin_value(client, message):
    value = float(message.text.split("sin", 1)[1])
    result = math.sin(math.radians(value))
    message.edit_text(f"sin({value}) = {result:.6f}")

@app.on_message(filters.command("cos", prefixes="."))
def cos_value(client, message):
    value = float(message.text.split("cos", 1)[1])
    result = math.cos(math.radians(value))
    message.edit_text(f"cos({value}) = {result:.6f}")

@app.on_message(filters.command("tan", prefixes="."))
def tan_value(client, message):
    value = float(message.text.split("tan", 1)[1])
    result = math.tan(math.radians(value))
    message.edit_text(f"tan({value}) = {result:.6f}")

@app.on_message(filters.command("cot", prefixes="."))
def cot_value(client, message):
    value = float(message.text.split("cot", 1)[1])
    result = 1 / math.tan(math.radians(value))
    message.edit_text(f"cot({value}) = {result:.6f}")

@app.on_message(filters.command("sec", prefixes="."))
def sec_value(client, message):
    value = float(message.text.split("sec", 1)[1])
    result = 1 / math.cos(math.radians(value))
    message.edit_text(f"sec({value}) = {result:.6f}")

@app.on_message(filters.command("csc", prefixes="."))
def csc_value(client, message):
    value = float(message.text.split("csc", 1)[1])
    result = 1 / math.sin(math.radians(value))
    message.edit_text(f"csc({value}) = {result:.6f}")
#    Работа с текстом
#    Работа с текстом
#    Работа с текстом
#    Работа с текстом
#    Работа с текстом 
@app.on_message(filters.command("IMT", prefixes='.') & filters.me)
def calculate_imt(client, message):
    # Разбиение сообщения на части
    parts = message.text.split()
    
    if len(parts) != 4:
        message.edit("Неверное количество аргументов. Используйте: .IMT <рост> <вес> <Пол>")
        return
    
    try:
        height = float(parts[1])
        weight = float(parts[2])
        
        # Расчёт ИМТ
        imt = weight / ((height / 100) ** 2)
        
        gender = parts[3].lower()
        
        # Проверка пола и вывод результата
        if gender == 'м':
            gender_text = "Мужчина"
        elif gender == 'ж':
            gender_text = "Женщина"
        else:
            message.edit("Неверно указан пол. Используйте 'М' для мужчин или 'Ж' для женщин")
            return
        
        message.edit(f"ИМТ: {imt:.2f}. Пол: {gender_text}")
        
    except ValueError:
        message.edit("Неверные аргументы. Рост и вес должны быть числами")
          
zodiac_signs = {
    1: "Овен", 2: "Телец", 3: "Близнецы", 4: "Рак", 5: "Лев", 
    6: "Дева", 7: "Весы", 8: "Скорпион", 9: "Стрелец", 10: "Козерог", 
    11: "Водолей", 12: "Рыбы"
}

def get_zodiac(day, month):
    return zodiac_signs[(month + 9) % 12 or 12]

def get_age(date):
    today = datetime.now()
    age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
    return age

def russian_weekday(day):
    days = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
    return days[day]

@app.on_message(filters.command("an", prefixes="."))
def analyze_date(client, message: Message):
    try:
        dates = message.text.split(" ")[1].split("-")
        date1 = datetime.strptime(dates[0], "%d.%m.%Y")
        date2 = datetime.strptime(dates[1], "%d.%m.%Y")
        
        age1 = get_age(date1)
        age2 = get_age(date2)
        
        zodiac1 = get_zodiac(date1.day, date1.month)
        zodiac2 = get_zodiac(date2.day, date2.month)
        
        age_difference = abs((date1 - date2).days)
        months_difference = abs((date1.year - date2.year) * 12 + date1.month - date2.month)
        
        day_of_week1 = russian_weekday(date1.weekday())
        day_of_week2 = russian_weekday(date2.weekday())
        
        result = (
            f"📅 <b>Первая дата:</b> {date1.strftime('%d.%m.%Y')} ({day_of_week1}):\n"
            f"🌟 <b>Знак Зодиака:</b> {zodiac1}\n"
            f"⏳ <b>Возраст:</b> {age1} лет\n\n"
            f"📅 <b>Вторая дата:</b> {date2.strftime('%d.%m.%Y')} ({day_of_week2}):\n"
            f"🌟 <b>Знак Зодиака:</b> {zodiac2}\n"
            f"⏳ <b>Возраст:</b> {age2} лет\n\n"
            f"⏰ <b>Первая дата старше на приблизительно {age_difference} дней ({months_difference} месяцев) ~ {abs(age1 - age2)} лет."
        )
        
        message.edit(result)
        
    except Exception as e:
        message.edit(f"Произошла ошибка: {e}")
        
@app.on_message(filters.command("switch", prefixes=".")) 
async def switch_letters(client, message):
    text = message.text.lower().split(" ", 1)[1]  # Получаем текст после команды
    switched_text = ""
    ru_to_en = {
        "й": "q", "ц": "w", "у": "e", "к": "r", "е": "t", "н": "y", "г": "u", "ш": "i", "щ": "o", "з": "p",
        "х": "[", "ъ": "]", "ф": "a", "ы": "s", "в": "d", "а": "f", "п": "g", "р": "h", "о": "j", "л": "k",
        "д": "l", "ж": ";", "э": "'", "я": "z", "ч": "x", "с": "c", "м": "v", "и": "b", "т": "n", "ь": "m",
        "б": ",", "ю": "."
    }
    en_to_ru = {v: k for k, v in ru_to_en.items()}
    
    for letter in text:
        if letter in ru_to_en:
            switched_text += ru_to_en[letter]
        elif letter in en_to_ru:
            switched_text += en_to_ru[letter]
        else:
            switched_text += letter
            
    await message.edit(switched_text)
    
@app.on_message(filters.command("utan", prefixes="."))
def analyze_message(client, message: Message):
    text = message.text.split(" ", 1)

    if len(text) == 2:
        message_text = text[1]
        
        num_characters = len(message_text)
        num_words = len(message_text.split())
        num_sentences = message_text.count(".") + message_text.count("!") + message_text.count("?")
        num_paragraphs = len(message_text.split("\n"))
        num_vowels = sum(1 for char in message_text if char.lower() in 'aeiouауоыиэяюёе')
        num_consonants = sum(1 for char in message_text if char.isalpha() and char.lower() not in 'aeiouауоыиэяюёе')
        num_spaces = message_text.count(" ")
        unique_words = list(set(message_text.split()))
        num_unique_words = len(unique_words)
        most_common_word = max(set(unique_words), key=message_text.split().count)
        
        num_alpha_chars = sum(1 for char in message_text if char.isalpha())
        num_uppercase = sum(1 for char in message_text if char.isupper())
        num_lowercase = sum(1 for char in message_text if char.islower())
        punctuation_marks = sum(1 for char in message_text if char in string.punctuation)
        num_digits = sum(1 for char in message_text if char.isdigit())
        unique_punctuation_marks = list(set(char for char in message_text if char in string.punctuation))

        sentences = re.split(r'[.!?]', message_text)
        sentences = [sentence for sentence in sentences if sentence]

        longest_sentence = max(sentences, key=len)
        shortest_sentence = min(sentences, key=len)

        analysis_result = f"**Ультра-анализ текста:**\n\n" \
                          f"🔠 <b>Количество символов:</b> {num_characters}\n" \
                          f"📝 <b>Количество слов:</b> {num_words}\n" \
                          f"🗣 <b>Количество предложений:</b> {num_sentences}\n" \
                          f"📃 <b>Количество абзацев:</b> {num_paragraphs}\n" \
                          f"🔤 <b>Количество гласных:</b> {num_vowels}\n" \
                          f"🔡 <b>Количество согласных:</b> {num_consonants}\n" \
                          f"⌨️ <b>Количество пробелов:</b> {num_spaces}\n" \
                          f"🔤 <b>Количество уникальных слов:</b> {num_unique_words}\n" \
                          f"🔡 <b>Самое часто встречающееся уникальное слово:</b> {most_common_word}\n" \
                          f"\n🔤 <b>Количество букв:</b> {num_alpha_chars}\n" \
                          f"🔠 <b>Количество заглавных букв:</b> {num_uppercase}\n" \
                          f"🔡 <b>Количество строчных букв:</b> {num_lowercase}\n" \
                          f"❗️ <b>Количество знаков препинания:</b> {punctuation_marks}\n" \
                          f"🔢 <b>Количество цифр:</b> {num_digits}\n" \
                          f"❓ <b>Знаки препинания:</b> {unique_punctuation_marks}\n" \
                          f"\n📈 <b>Самое длинное предложение:</b> {longest_sentence.strip()}\n" \
                          f"📉 <b>Самое короткое предложение:</b> {shortest_sentence.strip()}"

        message.edit(analysis_result)
        
@app.on_message(filters.command("textan", prefixes="."))
def analyze_message(client, message: Message):
    text = message.text.split(" ", 1)

    if len(text) == 2:
        message_text = text[1]
        num_characters = len(message_text)
        num_words = len(message_text.split())
        num_sentences = message_text.count(".") + message_text.count("!") + message_text.count("?")
        num_paragraphs = len(message_text.split("\n"))
        
        analysis_result = f"**Анализ текста:**\n\n"\
                          f"🔠 <b>Количество символов:</b> {num_characters}\n"\
                          f"📝 <b>Количество слов:</b> {num_words}\n"\
                          f"🗣 <b>Количество предложений:</b> {num_sentences}\n"\
                          f"📃 <b>Количество абзацев:</b> {num_paragraphs}"
        
        message.edit(analysis_result)
# Обработчик обеих команд для изменения текста в верхний и нижний регистр
@app.on_message(filters.command(["regup", "reglow"], prefixes="."))
async def change_text_case(client, message: Message):
    command = message.command[0]
    text = message.text.split(maxsplit=1)[1]
    
    if command == "regup":
        new_text = text.upper()
    elif command == "reglow":
        new_text = text.lower()

    await message.edit_text(new_text)

# Обработчик команды для инверсивного регистра
@app.on_message(filters.command("reginv", prefixes="."))
async def invert_text_case(client, message: Message):
    text = message.text.split(maxsplit=1)[1]
    
    inverted_text = "".join([char.lower() if char.isupper() else char.upper() for char in text])
    
    await message.edit_text(inverted_text)

# Обработчик команды для чередования регистров
@app.on_message(filters.command("regtoggle", prefixes="."))
async def toggle_text_case(client, message: Message):
    text = message.text.split(maxsplit=1)[1]
    
    toggled_text = "".join([char.upper() if (i % 2 == 0) else char.lower() for i, char in enumerate(text)])
    
    await message.edit_text(toggled_text)
    
# Обработчик команды для преобразования каждого слова в тексте с заглавной буквы
@app.on_message(filters.command("regtitle", prefixes="."))
async def title_case_words(client, message: Message):
    text = message.text.split(maxsplit=1)[1]
    
    title_text = " ".join(word.capitalize() for word in text.split())

    await message.edit_text(title_text)
 
 # Обработчик команды для случайного регистра каждой буквы в тексте
@app.on_message(filters.command("regrand", prefixes="."))
async def random_case_text(client, message: Message):
    text = message.text.split(maxsplit=1)[1]
    
    random_text = "".join(random.choice([char.upper(), char.lower()]) if char.isalpha() else char for char in text)

    await message.edit_text(random_text)

@app.on_message(filters.command("ticker", prefixes="."))
def shuffle_letters(client, message):
    words = message.text.split(" ")[1:]  # Исключаем команду ".ticker" из обработки
    result_words = []

    for word in words:
        if len(word) > 1:  # Для слов длиной меньше или равной 2 символам перемешивать не будем
            shuffled_word = list(word)
            random.shuffle(shuffled_word)
            word = "".join(shuffled_word)
        result_words.append(word)

    result_text = " ".join(result_words)
    message.edit(result_text)

@app.on_message(filters.command("icalc", prefixes="."))
async def name_calculation(client, message: Message):
    names = message.text.split()[1:]
    name1 = names[0]
    name2 = names[1]
    result = name1 + " + " + name2 + " = Любовь"
    
    animation = [
        "💖✨ Проводим расчеты... ✨💖",
        "💑💫 Магия любви начинает свое действие 💫💑",
        "💞🔮 Формируется истинная связь... 🔮💞",
        "❤️✨ Судьба воплотилась в любви... ✨❤️"
    ]
    
    compliments = [
        "💕 Нежность и любовь наполняют взаимоотношения с {name1} и {name2} 💕",
        "💑 В их имени таится магия, способная сокрушить сердца 💑",
        "💖 Эти имена обещают долгую сказку счастья и взаимопонимания 💖"
    ]
    
    try:
        await message.delete()  # Delete the command message
    except:
        pass
    
    response = await message.reply(animation[0])
    
    for frame in animation[1:]:
        await asyncio.sleep(3)
        if response:
            await response.edit(frame)
    
    compliment_1 = compliments[0].format(name1=name1, name2=name2)
    compliment_2 = f"💖 {name1} + {name2} = Любовь 💖"
    
    await asyncio.sleep(5)
    if response:
        await response.edit(compliment_1)
        await asyncio.sleep(5)
        await response.edit(compliment_2)

@app.on_message(filters.command("calc", prefixes="."))
async def calculate_expression(client, message):
    expression = message.text.split(" ", 1)[1]
    
    try:
        result = sympify(expression)
        
        result_steps = []  # Список для хранения шагов вычислений
        
        result_text = "Дано выражение: '{}'\n".format(expression)
        
        # Замена "^" на "**"
        expression = expression.replace("^", "**")
        
        while result.is_Add or result.is_Mul:
            if result.is_Add:
                add_expr = result.args
                add_sum = sum(add_expr)
                result_text += "{} = {}\n".format(add_expr[0] + add_expr[1], add_sum)
                result = add_sum
            elif result.is_Mul:
                mul_expr = result.args
                mul_res = mul_expr[0] * mul_expr[1]
                result_text += "{} = {}\n".format(mul_expr[0] * mul_expr[1], mul_res)
                result = mul_res
        
        result_evaluated = result.evalf().evalf(4)  # Итоговый результат
        
        await message.edit_text("\n".join([result_text, "🔍 Итоговый ответ: {}".format(result_evaluated)]))

    except Exception as e:
        await message.edit_text("Ошибка: {}".format(e))

@app.on_message(filters.command("love", prefixes="."))
def love_heart(client, message: Message):
    love_heart_art = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄░░░░▄▄▄░░░░▄▄▄░░░░░░
░░░▀████▀░░▄█████▄▄█████▄░░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░████████████████░░░
░░░░░██░░░▀██████████████▀░░░
░░░░▄██▄░░░░▀██████████▀░░░░░
░░░██████░░░░░▀██████▀░░░░░░░
░░░░░░░░░░░░░░░░▀██▀░░░░░░░░░
░░░░░░░░░░░░░▄▄░░░░░░░░░░░░░░
░░▀███░███▀▄█▀▀█▄░▀██▀░▀██▀░░
░░░░▀█▄█▀░▄█░░░░█▄░██░░░██░░░
░░░░░░█░░░██░░░░██░██░░░██░░░
░░░░░░█░░░░█▄░░▄█░░██░░░██░░░
░░░░▄███▄░░░▀██▀░░░░▀███▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
    message.edit(love_heart_art)

@app.on_message(filters.command("gor", prefixes="."))
def love_heart(client, message: Message):
    gor_art = """

▒▒▒▒▒▄██████████▄▒▒▒▒▒ 
▒▒▒▄██████████████▄▒▒▒ 
▒▒██████████████████▒▒ 
▒▐███▀▀▀▀▀██▀▀▀▀▀███▌▒ 
▒███▒▒▌■▐▒▒▒▒▌■▐▒▒███▒ 
▒▐██▄▒▀▀▀▒▒▒▒▀▀▀▒▄██▌▒ 
▒▒▀████▒▄▄▒▒▄▄▒████▀▒▒ 
▒▒▐███▒▒▒▀▒▒▀▒▒▒███▌▒▒ 
▒▒███▒▒▒▒▒▒▒▒▒▒▒▒███▒▒ 
▒▒▒██▒▒▀▀▀▀▀▀▀▀▒▒██▒▒▒ 
▒▒▒▐██▄▒▒▒▒▒▒▒▒▄██▌▒▒▒ 
▒▒▒▒▀████████████▀▒▒▒▒
"""
    message.edit(gor_art)

@app.on_message(filters.command("cat", prefixes="."))
def uno(client, message: Message):
    cat_art = """
░░░░░░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░░░░░
░░░░░░█░░▄▀▀▀▀▀▀▀▀▀▀▀▀▀▄░░█░░░░░
░░░░░░█░█░▀░░░░░▀░░▀░░░░█░█░░░░░
░░░░░░█░█░░░░░░░░▄▀▀▄░▀░█░█▄▀▀▄░
█▀▀█▄░█░█░░▀░░░░░█░░░▀▄▄█▄▀░░░█░
▀▄▄░▀██░█▄░▀░░░▄▄▀░░░░░░░░░░░░▀▄
░░▀█▄▄█░█░░░░▄░░█░░░▄█░░░▄░▄█░░█
░░░░░▀█░▀▄▀░░░░░█░██░▄░░▄░░▄░███
░░░░░▄█▄░░▀▀▀▀▀▀▀▀▄░░▀▀▀▀▀▀▀░▄▀░
░░░░█░░▄█▀█▀▀█▀▀▀▀▀▀█▀▀█▀█▀▀█░░░
░░░░▀▀▀▀░░▀▀▀░░░░░░░░▀▀▀░░▀▀░░░░
"""
    message.edit(cat_art)

@app.on_message(filters.command("diz", prefixes="."))
def uno(client, message: Message):
    diz_art = """
███████▄▄███████████▄
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓███░░░░░░░░░░░░█
██████▀░░░░░░░██████▀
░░░░░░░░░█░░░░█
░░░░░░░░░░█░░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░░▀▀
"""
    message.edit(diz_art)

@app.on_message(filters.command("fuck", prefixes="."))
def uno(client, message: Message):
    fuck_art = """
░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
░░░░░░░░░░░░░░█░░█░░░░░░░░░░
██████▄███▄████░░███▄░░░░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░
▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░
▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░
▓▓▓▓▓▓█████░░░░░░░░░██░░░░░
█████▀░░░░▀▀████████░░░░░░
"""
    message.edit(fuck_art)

@app.on_message(filters.command("dog", prefixes="."))
def uno(client, message: Message):
    dog_art = """
░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█ 
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█ 
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█ 
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌ 
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█ 
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌ 
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌ 
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█
"""
    message.edit(dog_art)
    
@app.on_message(filters.command("anon", prefixes="."))
def uno(client, message: Message):
    anon_art = """
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█ 
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█ 
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█ 
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█ 
███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█ 
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██ 
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██ 
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██ 
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███ 
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███ 
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████ 
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████ 
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████ 
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████ 
██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████ 
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████ 
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████ 
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
"""
    message.edit(anon_art)

@app.on_message(filters.command("uno", prefixes="."))
def uno(client, message: Message):
    uno_art = """
⣰⣾⣿⣿⣿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆
⣿⣿⣿⡿⠋⠄⡀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⣉⣉⣉⡉⠙⠻⣿⣿
⣿⣿⣿⣇⠔⠈⣿⣿⣿⣿⣿⡿⠛⢉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣦⡀⠹
⣿⣿⠃⠄⢠⣾⣿⣿⣿⠟⢁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⡟⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠋⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡿⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿⠗⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⡟
⣿⡿⠁⣼⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⠄⣠⣄⢰⣿⣿⣿⣿⣿⣿⣿⠃
⡿⠁⣼⣿⣿⣿⣿⣿⣿⣿⡇⠄⢀⡴⠚⢿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢠
⠃⢰⣿⣿⣿⣿⣿⣿⡿⣿⣿⠴⠋⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾
⢀⣿⣿⣿⣿⣿⣿⣿⠃⠈⠁⠄⠄⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⢀⣾⣿
⢸⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢶⣿⣿⣿⣿⣿⣿⣿⣿⠏⢀⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⠋⣠⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿⣿⣿⣿
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿⣿
⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢁⣴⣿⣿⣿⣿⠗⠄⠄⣿⣿
⣆⠈⠻⢿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣤⣾⣿⣿⣿⣿⣿⣇⠠⠺⣷⣿⣿
⣿⣿⣦⣄⣈⣉⣉⣉⣡⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⠉⠁⣀⣼⣿⣿⣿
⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣿⡿⠟
"""
    message.edit(uno_art)
    
@app.on_message(filters.command("alen", prefixes="."))
async def alphavit_en(_, message):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = alphabet.lower()
    result = ""
    chunk_size = 6  # количество букв в одной строке
    for i in range(0, len(alphabet), chunk_size):
        chunk = " ".join([f"{alphabet[j]}{alphabet_lower[j]}" for j in range(i, min(i + chunk_size, len(alphabet)))]).strip()
        result += chunk + "\n"
    await message.delete()
    await message.reply(result)

@app.on_message(filters.command("alru", prefixes="."))
async def alphavit_ru(_, message):
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    result = ""
    chunk_size = 6  # количество букв в одной строке
    for i in range(0, len(alphabet), chunk_size):
        chunk = " ".join([f"{alphabet[j]}{alphabet_lower[j]}" for j in range(i, min(i + chunk_size, len(alphabet)))]).strip()
        result += chunk + "\n"
    await message.delete()
    await message.reply(result)
        
@app.on_message(filters.command("tank", prefixes="."))
def uno(client, message: Message):
    tank_art = """
░░░░░░███████ ]▄▄▄▄▄▄▄▄▃ 
▂▄▅█████████▅▄▃▂ 
I███████████████████]. 
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤ 
"""
    message.edit(tank_art)
    
@app.on_message(filters.command("cake", prefixes="."))
def uno(client, message: Message):
    cake_art = """
┈┈┈☆☆☆☆☆☆☆☆☆┈┈┈
┈┈╭┻┻┻┻┻┻┻┻┻╮┈┈
┈┈┃╱╲╱╲╱╲╱╲╱┃┈┈
┈╭┻━━━━━━━━━┻╮┈
┈┃╱╲╱╲╱╲╱╲╱╲╱┃┈
┈┗━━━━━━━━━━━┛┈  
"""
    message.edit(cake_art)

@app.on_message(filters.command("loveyou", prefixes="."))
def uno(client, message: Message):
    loveyou_art = """
░███████░
░█╬╬╬╬╬█░
░██╬╬███░
░██╬╬███░
░██╬╬███░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬╬████░
░█╬╬╬╬██░
░█╬╬████░
░█╬╬╬╬╬█░
░███████░
░███████░
░███████░
░███████░
░███████░
░█╬╬█╬╬█░
░█╬╬█╬╬█░
░██╬╬╬██░
░██╬╬╬██░
░██╬╬╬██░
░███████░
░█╬╬╬╬╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬███╬█░
░█╬╬╬╬╬█░
░███████░
"""
    message.edit(loveyou_art)
    
wikipedia.set_lang("ru") 
# Обработчик команды /wiki
@app.on_message(filters.command("wiki", prefixes="."))
def wiki_command(client, message):
    query = " ".join(message.command[1:])
    results = получить_краткое_описание_wiki(query)
    client.send_message(message.chat.id, results)

# Функция для получения краткой информации из Википедии
def получить_краткое_описание_wiki(query):
    try:
        summary = wikipedia.summary(query, sentences=5)  # Увеличиваем количество предложений
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:15]  # Показать первые 15 вариантов
        return "Уточните ваш запрос, возможно вы имели в виду:\n" + "\n".join(options)
    except wikipedia.exceptions.PageError:
        return "По вашему запросу ничего не найдено."
    
    
# Функция для получения курса валюты в рублях через ЦБ РФ
def get_currency_rate(currency_code):
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "xml")
    valute_list = soup.find_all("Valute")
    for valute in valute_list:
        valute_code = valute.find("CharCode").text
        if valute_code == currency_code:
            rate = float(valute.find("Value").text.replace(",", ".")) / float(valute.find("Nominal").text)
            return rate
    return None


# Обработчик команды /cur
@app.on_message(filters.command("cur", prefixes="."))
def cur_command(client, message):
    currencies = {
        "USD": "<b>Доллар США</b>",
        "EUR": "<b>Евро</b>",
        "CNY": "<b>Китайский юань</b>",
        "JPY": "<b>Японский иен</b>",
        "PLN": "<b>Польский злоты</b>",
        "GBP": "<b>Фунт стерлингов Соединённого королевства</b>",
        "AUD": "<b>Австрийский доллар</b>",
        "BYN": "<b>Белорусский рубль</b>",
        "BRL": "<b>Бразильский реал</b>",
        "HKD": "<b>Гонконгский доллар</b>",
        "DKK": "<b>Датская крона</b>",
        "SEK": "<b>Шведские кроны</b>",
        "CZK": "<b>Чешские кроны</b>",
        "UZS": "<b>Узбекские сумы</b>",
        "TRY": "<b>Турецкие лиры</b>",
    }

    message_text = "<b>Курсы валют ЦБ РФ:</b>\n\n"
    for currency_code, currency_name in currencies.items():
        rate = get_currency_rate(currency_code)
        if rate:
            message_text += f"{currency_name}: `{rate}` руб\n"

    message.edit_text(message_text)

@app.on_message(filters.command("guideprem", prefixes="."))
def uno(client, message: Message):
    guide = """
<b><u>Гайд по покупке Премиум-подписке Телеграм:</u></b>
\n1. Переходим в бота @PremiumBot и запускаем бота.
2. Выбираете нужный себе тариф подписки и нажимаете на кнопку оплаты, затем на "Заплатить"
3. Вводите свои данные карты и оплачиваете покупку
\n\n<b><u>Отмена автопродления подписки:</u></b>
\n1. Заново нажимаете кнопку /start в боте (@PremiumBot)
2. Нажимаете команду /stop, после чего Вам придётся ответить на вопросы и потом отменится автопродление
\n\n<b><u>Подключение автопродления подписки:</u></b>
\n1. Заново нажимаете кнопку /start в боте (@PremiumBot)
2. Нажимаете команду /resume и включается автопродление подписки
"""
    message.edit(guide)

@app.on_message(filters.command("c", prefixes="."))
def encode_text(client, message):
    text = message.text.split(" ", 1)[1]
    binary_text = bin(int.from_bytes(text.encode('utf-8'), 'big'))[2:]
    message.delete()
    client.send_message(message.chat.id, f"{binary_text}")

@app.on_message(filters.command("dec", prefixes="."))
def decode_text(client, message):
    binary_text = message.text.split(" ", 1)[1]
    text = int(binary_text, 2).to_bytes((len(binary_text) + 7) // 8, 'big').decode('utf-8')
    message.delete()
    client.send_message(message.chat.id, f"{text}")


def convert_base(num, source_base, target_base):
    
    if source_base < 2 or target_base < 2 or source_base > 36 or target_base > 36:
        return "Ошибка: Неверное основание системы счисления"

    try:
        num_parts = num.split('.')
        integer_part = int(num_parts[0], source_base)
        converted_integer = ""

        while integer_part > 0:
            integer_part, remainder = divmod(integer_part, target_base)
            converted_integer = ("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")[remainder] + converted_integer

        if len(num_parts) == 1:
            return converted_integer
        else:
            fractional_part = num_parts[1]
            converted_fractional = ""
            fractional_length = len(fractional_part)
            for i, char in enumerate(fractional_part):
                power = i + 1
                converted_fractional += f'{int(char, source_base) * (source_base ** -power):.10f}'  # 10 знаков после точки

            return f"{converted_integer}.{converted_fractional}"
    except ValueError:
        return "Ошибка: Неверный формат числа"

@app.on_message(filters.command("ss", prefixes="."))
def convert_bases(client, message):
    command = re.findall(r'\b[0-9A-Z]+\b', message.text)

    if len(command) == 3:
        original_num = command[0].upper()
        source_base = int(command[1])
        target_base = int(command[2])

        response = f"Вы ввели: {' '.join(command)}\n\n"
        
        if re.match("^[0-9A-Z]+\.*[0-9A-Z]*$", original_num):
            converted_num = convert_base(original_num, source_base, target_base)
            response += f"**🔍 Решение:**\n\n"

            # Добавляем подробное решение
            original_num_dec = int(original_num, source_base)
            detailed_solution = f"{original_num} _{source_base} = "
            for i, char in enumerate(original_num):
                power = len(original_num) - i - 1
                if i > 0:
                    detailed_solution += " + "
                detailed_solution += f"{int(char, source_base)}∙{source_base}^{power}"

            detailed_solution += f" = {converted_num} _{target_base}"
            response += detailed_solution

        else:
            response += "Ошибка: Неверный формат числа"

        client.send_message(message.chat.id, response)

    else:
        client.send_message(message.chat.id, "Ошибка: Неверное количество аргументов. Пример использования: A21F 16 10")



#    Спам
#    Спам
#    Спам
#    Спам
#    Спам
@app.on_message(filters.command("sps", prefixes="."))
async def spams(client, message: Message):
    try:
        parts = message.text.split()[1:]
        repeat = parts[0]
        if not repeat.isdigit():
            await message.reply("Пожалуйста, укажите целое число повторений.")
            return
        repeat = int(repeat)
        
        text = " ".join(parts[1:])
        
        if len(text) == 0:
            await message.reply("Пожалуйста, введите текст для повторения.")
            return
        
        await message.delete()  # Удалить сообщение с командой
        
        repeated_text = (text + " ") * repeat
        for chunk in [repeated_text[i:i+4000] for i in range(0, len(repeated_text), 4000)]:
            await message.reply(chunk)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

@app.on_message(filters.command("spw", prefixes="."))
async def spamw(client, message: Message):
    try:
        parts = message.text.split()[1:]
        repeat = parts[0]
        if not repeat.isdigit():
            await message.reply("Пожалуйста, укажите целое число повторений.")
            return
        repeat = int(repeat)
        
        text = " ".join(parts[1:])
        
        if len(text) == 0:
            await message.reply("Пожалуйста, введите текст для повторения.")
            return
        
        await message.delete()  # Удалить сообщение с командой
        
        repeated_text = "\n".join([text for _ in range(repeat)])
        for chunk in [repeated_text[i:i+4000] for i in range(0, len(repeated_text), 4000)]:
            await message.reply(chunk)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
  
@app.on_message(filters.command("spwn", prefixes="."))
async def spamwn(client, message: Message):
    try:
        parts = message.text.split()[1:]
        repeat = parts[0]
        if not repeat.isdigit():
            await message.reply("Пожалуйста, укажите целое число повторений.")
            return
        repeat = int(repeat)
        
        text = " ".join(parts[1:])
        
        if len(text) == 0:
            await message.reply("Пожалуйста, введите текст для повторения.")
            return
        
        await message.delete()  # Удалить сообщение с командой
        
        repeated_text = "\n".join(f"{i+1}. {text}" for i in range(repeat))
        for chunk in [repeated_text[i:i+4000] for i in range(0, len(repeated_text), 4000)]:
            await message.reply(chunk)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

@app.on_message(filters.command("spm", prefixes="."))
async def spamm(client, message: Message):
    try:
        parts = message.text.split()[1:]
        repeat = parts[0]
        if not repeat.isdigit():
            await message.reply("Пожалуйста, укажите целое число повторений.")
            return
        repeat = int(repeat)
        
        phrases = " ".join(parts[1:]).split(";")
        
        if len(phrases) == 0:
            await message.reply("Пожалуйста, введите текст сообщений для повторения.")
            return
        
        await message.delete()  # Удалить сообщение с командой
        
        full_text = " ".join(phrases)

        for i in range(repeat):
            for chunk in [full_text[i:i+4000] for i in range(0, len(full_text), 4000)]:
                await message.reply(chunk)
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
        
@app.on_message(filters.command("spcal", prefixes="."))
async def spam_calculator(client, message):
    command = message.text.split(" ", 1)
    if len(command) == 2:
        try:
            expression, str_limit = command[1].rsplit(" ", 1)  # Разделяем операцию и лимит
            
            # Удалить сообщение с командой
            await message.delete()
            
            # Преобразование операции
            operation = expression.replace("плюс", "+")\
                                 .replace("минус", "-")\
                                 .replace("умножить", "*")\
                                 .replace("разделить", "/")

            limit = float(str_limit)

            num1, operator, num2 = None, None, None

            if "+" in operation:
                num1, num2 = map(float, operation.split("+"))
                operator = "+"
            elif "-" in operation:
                num1, num2 = map(float, operation.split("-"))
                operator = "-"
            elif "*" in operation:
                num1, num2 = map(float, operation.split("*"))
                operator = "*"
            elif "/" in operation:
                num1, num2 = map(float, operation.split("/"))
                operator = "/"
            else:
                raise ValueError("Invalid expression")

            result = num1

            while True:
                prev_result = result
                result = eval(f"{result} {operator} {num2}")
                
                # Отправить сообщение с результатом спам-вычисления
                await message.reply_text(f"{prev_result} {operator} {num2} = {result}")

                if operator == "/" and num2 == 0:
                    raise ZeroDivisionError("Деление на 0")

                if (result < limit and limit > 0) or (result > limit and limit < 0):
                    continue
                else:
                    break

        except (ValueError, ZeroDivisionError):
            await message.reply_text("Ошибка в формате выражения или делении на ноль. Используйте '.spamcalc <операция> <лимит>'.")
 
         
#    Telegram  
#    Telegram       
#    Telegram         
#    Telegram        
#    Telegram
@app.on_message(filters.command("id", prefixes="."))
def get_ids(client, message: Message):
    chat_id = message.chat.id
    user_id = None
    if message.chat.type == "private":
        user_id = message.from_user.id
    else:
        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
        else:
            message.edit("Эта команда работает только при ответе на сообщение")
    
    if user_id:
        message.edit(f"<b>User id:</b> `{user_id}`\n<b>Chat id:</b> `{chat_id}`")
        
@app.on_message(filters.command("myid", prefixes="."))
def get_my_id(client, message: Message):
    my_id = message.from_user.id
    chat_id = message.chat.id
    
    message.edit(f"<b>Your id:</b> `{my_id}`\n<b>Chat id:</b> `{chat_id}`")

def get_user_ipv4():
    return requests.get('https://api.ipify.org?format=json').json()['ip']

def get_user_ipv6():
    return requests.get('https://api64.ipify.org?format=json').json()['ip']

@app.on_message(filters.command("me", prefixes="."))
async def get_user_data(client, message: Message):
    user = message.from_user
    
    user_id = user.id
    username = user.username if user.username else "Отсутствует"
    phone_number = user.phone_number if user.phone_number else "Отсутствует"
    first_name = user.first_name
    last_name = user.last_name if user.last_name else "Отсутствует"
    
    user_data = f"👥 <b>Юзернейм:</b> @{username}\n"
    user_data += f"🆔 <b>ID:</b> `{user_id}`\n"
    user_data += f"📞 <b>Номер:</b> `{phone_number}`\n"
    user_data += f"👤 <b>Имя:</b> `{first_name}`\n"
    user_data += f"👥 <b>Фамилия:</b> `{last_name}`\n\n"
    
    ipv4 = get_user_ipv4()
    ipv6 = get_user_ipv6()
    user_data += f"IPv4: `{ipv4}`\n"
    user_data += f"IPv6: `{ipv6}`"
    
    await message.edit(user_data)

@app.on_message(filters.command("loc", prefixes="."))
def analyze_message(client, message: Message):
    # Получение информации о сети и устройстве
    network_info = ""

    # MAC адрес устройства
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

    # Имя хоста и IP адрес
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    # Форматирование информации о сети
    network_info += f"🖥️ <b>MAC Address:</b> `{mac_address}`\n"
    network_info += f"💻 <b>Host Name:</b> `{host_name}`\n"
    network_info += f"🌐 <b>Host IP Address:</b> `{host_ip}`\n"

    analysis_result = f"**Информация о сети и устройстве:**\n\n{network_info}"

    message.edit(analysis_result)
        
async def animate_timer(message, seconds):
    for _ in range(seconds, 0, -1):
        timer_str = "⏳" + "◉" * _ + "◯" * (seconds - _)
        await message.edit(f"Таймер: {timer_str}")
        await asyncio.sleep(1)

@app.on_message(filters.command("timer", prefixes="."))
async def set_timer(client, message: Message):
    try:
        parts = message.text.split()[1:]
        timer_str = parts[0]
        rest = " ".join(parts[1:])
        
        time_unit = timer_str[-1]
        time = int(timer_str[:-1])

        if time_unit == 'с':
            total_seconds = time
        elif time_unit == 'м':
            total_seconds = time * 60
        elif time_unit == 'ч':
            total_seconds = time * 3600
        else:
            await message.edit("Некорректно введено время. Используйте формат .timer (число)(с/м/ч) (текст) (повторения)")
            return

        await message.edit(f"Таймер установлен на {time}{time_unit}.")
        await asyncio.create_task(animate_timer(message, total_seconds))

        num_repeats = 1
        if rest:
            rest_parts = rest.rsplit(" ", 1)
            text = rest_parts[0]
            num_repeats = int(rest_parts[-1]) if len(rest_parts) > 1 else num_repeats
            for _ in range(num_repeats):
                await message.reply(text)

    except (ValueError, IndexError):
        await message.edit("Некорректно введены аргументы. Пожалуйста, используйте команду в формате: .timer (число)(с/м/ч) (текст) (повторения)")

#    Для чатов  
#    Для чатов       
#    Для чатов        
#    Для чатов        
#    Для чатов 
@app.on_message(filters.command("pin", prefixes="."))
async def pin_message(client, message):
    replied_message = message.reply_to_message
    
    if replied_message:
        await replied_message.pin()
        await message.delete()

@app.on_message(filters.command("unpin", prefixes="."))
async def unpin_message(client, message):
    replied_message = message.reply_to_message
    
    if replied_message:
        await replied_message.unpin()
        await message.delete()

@app.on_message(filters.command("unpinall", prefixes="."))
async def unpin_all_chat_messages(client, message):
    chat_id = message.chat.id
    await client.unpin_all_chat_messages(chat_id)
    
@app.on_message(filters.command("parseor", prefixes="."))
def parse_channel_members(client, message):
    args = message.text.split(" ")
    
    if len(args) < 2:
        client.send_message(message.chat.id, "Пожалуйста, укажите ID канала в команде.")
        return
    
    try:
        channel_username = args[1]
        members = client.get_chat_members(channel_username)
        
        member_list = []
        for member in members:
            user = member.user
            phone_number = user.phone_number if user.phone_number else "Нет"
            member_info = (
                f"<b>ID:</b> {user.id}\n"
                f"<b>Имя пользователя:</b> @{user.username}\n"
                f"<b>👤 Имя:</b> {user.first_name}\n"
                f"<b>👥 Фамилия:</b> {user.last_name}\n"
                f"<b>📞 Телефон:</b> {phone_number}\n"
                f"<b>🔖 Роль:</b> {member.status}"
            )
            member_list.append(member_info)
        
        chunk_size = 40
        for i in range(0, len(member_list), chunk_size):
            chunk = member_list[i:i + chunk_size]
            response = "\n\n".join(chunk)
            while len(response) > 4096: # Если длина сообщения больше 4096 символов
                client.send_message(message.chat.id, response[:4096])
                response = response[4096:]
            client.send_message(message.chat.id, response)
            time.sleep(2) # Перерыв в 2  секунд между отправкой
            
    except pyrogram.errors.exceptions.bad_request_400.ChannelInvalid:
        client.send_message(message.chat.id, "Недействительное имя канала. Пожалуйста, укажите правильное имя канала.")
    
    except pyrogram.errors.exceptions.bad_request_400.UserNotParticipant:
        client.send_message(message.chat.id, "Вы не являетесь участником указанного канала.")
        
@app.on_message(filters.command("all", prefixes="."))
def all_members(client, message):
    # Удаляем сообщение с командой
    message.delete()
    
    # Получаем список участников чата
    chat_id = message.chat.id
    members = client.get_chat_members(chat_id)
    
    # Формируем сообщения с упоминаниями участников
    mention_text = ", ".join([f"@{member.user.username}" for member in members])
    
    # Делим сообщение на части, если оно слишком длинное
    while mention_text:
        if len(mention_text) > 4096:
            split_index = mention_text.rfind(',', 0, 4096)
            part = mention_text[:split_index+1]
            mention_text = mention_text[split_index+1:]
        else:
            part = mention_text
            mention_text = ""
        
        message.reply_text(part)

@app.on_message(filters.command("parse", prefixes="."))
def parse_members(client, message):
    args = message.text.split(" ")
    
    if len(args) < 2:
        client.send_message(message.chat.id, "Пожалуйста, укажите ID чата в команде.")
        return
    
    try:
        chat_id = int(args[1])
        chat = client.get_chat(chat_id)
        members = chat.get_members()
        
        member_list = []
        for member in members:
            user = member.user
            phone_number = user.phone_number if user.phone_number else "NONE"
            member_info = (
                f"<b>ID:</b> `{user.id}`\n"
                f"<b>Username:</b> @{user.username}\n"
                f"<b>👤 Имя:</b> `{user.first_name}`\n"
                f"<b>👥 Фамилия:</b> `{user.last_name}`\n"
                f"<b>📞 Телефон:</b> `{phone_number}`\n"
                f"<b>🔖 Роль:</b> `{member.status}`"
            )
            member_list.append(member_info)
        
        for i in range(0, len(member_list), 5):
            chunk = member_list[i:i + 5]
            response = "\n\n".join(chunk)
            client.send_message(message.chat.id, response)
            
    except ValueError:
        client.send_message(message.chat.id, "Неправильный ID чата. Пожалуйста, укажите действительный ID чата.")
        
@app.on_message(filters.command("chat", prefixes="."))
def chat_analyze(client, message: Message):
    if message.chat.type == "private":
        message.edit_text("❌ Эта команда работает только в группах и каналах, а не в личных сообщениях.")
        return
    
    chat_id = message.chat.id
    chat_title = message.chat.title
    chat_type = message.chat.type
    
    if chat_id > 0:  # Если chat_id принадлежит пользователю
        message.edit_text("❌ Невозможно выполнить анализ чата, так как этот ID принадлежит пользователю, а не чату.")
        return
    
    chat_members_count = client.get_chat_members_count(chat_id)
    
    # Получение истории сообщений чата
    messages = client.get_chat_history(chat_id)
    
    # Словарь для подсчета количества сообщений пользователя
    user_message_count = defaultdict(int)
    
    for msg in messages:
        if msg.from_user and msg.from_user.username:
            user_message_count[msg.from_user.username] += 1
    
    # Сортировка пользователей по количеству сообщений
    top_users = sorted(user_message_count.items(), key=lambda x: x[1], reverse=True)[:10]
    
    # Общее количество сообщений
    total_messages = sum(user_message_count.values())
    
    # Формирование текста для вывода
    reply_text = f"🔍 <b>Анализ Чата:</b>\n\n" \
                 f"<b>Чат:</b>\n" \
                 f"🆔 <b>ID Чата:</b> `{chat_id}`\n" \
                 f"📜 <b>Название Чата:</b> `{chat_title}`\n" \
                 f"📌 <b>Тип Чата:</b> {chat_type}\n" \
                 f"👥 <b>Количество Участников:</b> {chat_members_count}\n\n" \
                 f"—————————\n\n" \
                 f"<b>Сообщения чата:</b>\n" \
                 f"📜 <b>Общее количество сообщений:<b> {total_messages}\n" \
                 f"🌟 <b>Топ 10 активных участников по количеству сообщений:<b>"
    
    for index, (username, message_count) in enumerate(top_users, start=1):
        reply_text += f"\n{index}. @{username} — {message_count} сообщений"
    
    message.edit_text(reply_text, parse_mode=None)


#    Игры
#    Игры
#    Игры
#    Игры
#    Игры
@app.on_message(filters.command("dice1", prefixes="."))
async def roll_the_dice(client, message):
    await message.delete()

    user_choice = random.randint(1, 6)
    bot_choice = random.randint(1, 6)

    if user_choice > bot_choice:
        result = "Вы выиграли!"
    elif user_choice < bot_choice:
        result = "Вы проиграли!"
    else:
        result = "Ничья!"

    await message.reply(f"Ваш бросок: <b>{user_choice}</b>\nБросок бота: <b>{bot_choice}</b>\n{result}")
@app.on_message(filters.command("dice2", prefixes="."))
async def roll_dice(client, message):
    await message.delete()

    try:
        num_of_dice = int(message.text.split(" ")[1])
    except (IndexError, ValueError):
        await message.reply("Неправильный формат! Используйте .dice2 [количество кубиков]")
        return

    results = [random.randint(1, 6) for _ in range(num_of_dice)]

    await message.reply(f"Вы бросили {num_of_dice} кубик(а/ов)!\nРезультаты: {', '.join(str(result) for result in results)}\nСумма: {sum(results)}")
@app.on_message(filters.command("coin", prefixes="."))
async def flip_coin(client, message):
    await message.delete()

    try:
        user_prediction = message.text.split(" ")[1].upper()
        if user_prediction not in ["О", "Р"]:
            raise ValueError("Неверное предположение! Используйте 'О' для Орла или 'Р' для Решки")
    except (IndexError, ValueError) as e:
        await message.reply(str(e) + "\nПравильный формат: .flipcoin (О/Р)")
        return

    result = random.choice(["О", "Р"])

    if user_prediction == result:
        await message.reply(f"Ваше предсказание: <b>{user_prediction}</b>\nРезультат: <b>{result}</b>\nПоздравляю, вы угадали!")
    else:
        await message.reply(f"Ваше предсказание: <b>{user_prediction}</b>\nРезультат: <b>{result}</b>\nК сожалению, вы не угадали. Попробуйте еще раз!")
@app.on_message(filters.command("KNB", prefixes="."))
async def play_game(client, message):
    await message.delete()

    game_choice = random.choice(["К", "Б", "Н"])
    user_choice = random.choice(["К", "Б", "Н"])

    result = ""
    if game_choice == user_choice:
        result = "Ничья!"
    elif game_choice == "К" and user_choice == "Н":
        result = "Вы проиграли! Камень побеждает ножницы."
    elif game_choice == "Б" and user_choice == "К":
        result = "Вы проиграли! Бумага побеждает камень."
    elif game_choice == "Н" and user_choice == "Б":
        result = "Вы проиграли! Ножницы побеждают бумагу."
    else:
        result = "Вы выиграли!"

    await message.reply(f"<b>Выбор компьютера:</b> {game_choice}\n<b>Ваш выбор:</b> {user_choice}\n<b>Результат:</b> {result}")

last_number_to_guess = None

@app.on_message(filters.command("ugchis", prefixes="."))
async def number_guessing_game(client, message):
    global last_number_to_guess

    try:
        # Получаем диапазон и вариант ответа из сообщения пользователя
        range_start, range_end, answer = map(int, message.text.split()[1:])
        
        if last_number_to_guess is None:
            number_to_guess = random.randint(range_start, range_end)
        else:
            number_to_guess = last_number_to_guess

        if answer < range_start or answer > range_end:
            await message.edit_text(f"Вариант ответа должен быть в пределах диапазона [{range_start}, {range_end}]")
            return

        user_guess = answer

        if user_guess == number_to_guess:
            await message.edit_text("Поздравляю! Вы угадали!")
            last_number_to_guess = None  # Сбрасываем число для угадывания
        else:
            await message.edit_text(f"Неверно. Число было: {number_to_guess}")
    except (IndexError, ValueError):
        await message.edit_text("Неправильный формат сообщения. Используйте .ugchis (начало диапазона) (конец диапазона) (вариант ответа), например, .ugchis 1 10 4")
            
# Логирование информации об аккаунте
def log_user_data(user, chat, text, outgoing=True):
    user_info = f"@{user.username}" if user.username else f"ID {user.id}"
    action = "Вы отправили сообщение" if outgoing else f"Вам пришло сообщение от {user_info}"
    chat_info = f"в чате '{chat.title}'" if chat else "в личном чате"
    logging.info(f"{action} {user_info} {chat_info}: {text}")

# Получение информации об аккаунте Telegram
def handle_user_data(client, message):
    log_user_data(message.from_user, message.chat, message.text)

@app.on_message(filters.me)
def wrapper_handle_user_data(client, message):
    handle_user_data(client, message)

# Логирование личных сообщений
@app.on_message(filters.private & filters.text)
def log_private_messages(client, message):
    action = "Вы отправили сообщение" if message.outgoing else f"Вам пришло сообщение от @{message.from_user.username}"
    logging.info(f"{action}: {message.text}")


# Логирование вступлений в группы
@app.on_message(filters.new_chat_members)
def log_group_joins(client, message):
    user_ids = ", ".join(f"@{member.username}" if member.username else f"ID {member.id}" for member in message.new_chat_members)
    logging.info(f"Новые участники {user_ids} вступили в группу {message.chat.title}")
    
app.run()
