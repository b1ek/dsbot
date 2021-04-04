# LogLib by BlackLightHack
# creeperywime@gmail.com
# +79940067828
# blek!#9906
# Released under GNU license
# https://discord.gg/JXZ8Vw5fBq

from datetime import date, datetime
from sys import exit
import os # нафиг не нужно
 

now = datetime.now() # получаем текущее время, но это котреж
logfilename = str(''.join((str("{}.{}.{}-{}.{}".format(now.day, now.month, now.year, now.hour, now.minute)), ".log"))) # Из кортежа получаю нужное время и дату, Указываю имя файлу лога
fdh = open(logfilename, "tw", encoding="utf-8") # открыть файл
 
 
def logTimeUpdate():
    now = datetime.now() # Получить текущее время и дату
    global logtime # глобальной
    logtime = str("[{}:{}:{}] ".format(now.hour, now.minute, now.second)) # Задать переменную времени
 
 
def write(obj): 
    logTimeUpdate() # Обновляем время в логе
    tup = logtime, ": ", obj # [10:16:42]: ""(но это кортеж!)
    wrie = ''.join(tup) # переобразовываем из кортежа в string
    fdh.write(wrie) # Записать в файл


def info(obj):
    logTimeUpdate()
    tup = logtime, '[INFO]: ', obj
    wrie = ''.join(tup) 
    fdh.write(wrie)


def warn(obj):
    logTimeUpdate()
    tup = logtime, '[WARN]: ', obj
    wrie = ''.join(tup) 
    fdh.write(wrie)


def error(obj):
    logTimeUpdate()
    tup = logtime, '[ERROR]: ', obj
    wrie = ''.join(tup) 
    fdh.write(wrie)


def debug(obj):
    logTimeUpdate()
    tup = logtime, '[DEBUG]: ', obj
    wrie = ''.join(tup) 
    fdh.write(wrie)

write("[INFO]: [LogLib] Loglib is running")