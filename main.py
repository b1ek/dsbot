# ========================== #
# Written & tested by blek!  #
#   creeperywime@gmail.com   #
#        blek!#7359          #
# Released under MIT license #
# ========================== #
import discord
from datetime import date, datetime
from difflib import SequenceMatcher as perc
import config
import sqlite3

"""CONFIG"""
token = config.token
prefix = config.prefix
respect_admin = config.respect_admin
emoj1 = config.emoj1
emoj2 = config.emoj2
emoj3 = config.emoj3
badwords = config.badwords
pause = config.pause
"""END OF CONFIG"""

print('Script initialized')

"""
КОМАНДЫ БОТА

'', 

Бот, команды
Бот, помощь
Бот, помощь по командам
Бот, список команд
Бот, какие у тебя есть команды?
Бот, дай мне список команд
Бот, хелп
Бот, какие у тебя команды
Бот, какие у тебя команды?

print(perc(lambda x: x == " ", "!помощь", "!по мощь").ratio())

"""

memeid = 826670875839168523 # meme channel id
client = discord.Client() # init discord
now = datetime.now() # получим время
LOGname = str(''.join((str("Mineland log {}d {}m {}y-{}h.{}m".format(now.day, now.month, now.year, now.hour, now.minute)), ".log"))) # собрать название файла лога

def upd_config():
    import config

async def log(log):
    logchannel = client.get_channel(828593536035061810)
    await logchannel.send(log)

@client.event
async def on_ready(): # when log in
    print('Login successful! You logged in as {0.user}'.format(client)) # to console

@client.event
async def on_message(message):


    if message.content.startswith(prefix): # command parser

        await log('Найдена команда: "{0.content}", от {0.author}'.format(message))
        cm = message.content # load message
        cmd = cm.split(str(prefix)) # remove message prefix

        if perc(lambda x: x == " ", cmd, 'обнови конфиг').ratio() > 0.8:
            if message.author.guild_permissions.administrator:
                if config.pause: return
                upd_config()
                await log(f'Обновлен конифг по просьбе {message.author}')
                await message.delete()
                return
            else:
                await message.delete()


        elif perc(lambda x: x == " ", cmd, 'помощь').ratio() < 0.8:
            if config.pause: return
            await message.author.send('> **ПОМОЩЬ ПО КОМАНДАМ**\n\nПока что пуста, =(')
            return

        elif perc(lambda x: x == " ", cmd, 'pause yourself').ratio() < 0.9:
            pause = True
        await log('Команда не распознана, поэтому отправлю ему в лс сообщение что она не распознана.')
        await message.author.send('Ваша команда не распознана! Используйте `Бот, команды`, чтобы посмотреть список команд!')
    
    if config.pause: return
    else: pass

    mmsg = str(message.content)
    msg = ''.join(sorted(set(mmsg), key=mmsg.index))

    global smislperc
    smislperc = perc(lambda x: x == " ", msg, 'смысола нет').ratio()

    if message.author == client.user: return
    if smislperc < 0.5366672776333333333:

        for i in badwords:

            smislperc = perc(lambda x: x == " ", msg, i).ratio()

            if smislperc > 0.5366672776333333333:
                break

            else:
                pass


    if smislperc > 0.5366672776333333333:
        await log(f'Найден предатель который говорит что в названии нету смысла! Его сообщение: **{message.content}**, предатель: **{message.author}**. %: **{round(smislperc * 100)}**')
        await message.delete()

    
    memes = client.get_channel(memeid) # get memes channel
    if message.channel == memes: # if message channel is memes channel
        if message.author.bot: return
        if message.attachments != []: # if message contain attachments
            await message.add_reaction(emoji=emoj1) # react with :+1:
            await message.add_reaction(emoji=emoj2) # heart
            await message.add_reaction(emoji=emoj3) # :-1:
            await log('В мемах найден МЕМ, добавляю к нему кнопки.')

        else: # ELSE:
            if message.author.guild_permissions.administrator != True: # if author is not administrator:
                await message.delete() # delete his fucking message without attachments
                await message.author.send('К сожалению, в канал <#826670875839168523> вам можно отправлять только картинки, =(') # DM him
                await log('В мемах найден ПРЕДАТЕЛЬ который не МЕМ. Удаляю его.')

            else: # if author has admin perm:
                if respect_admin:
                    msg = message.content
                    spl =  msg.split('==')
                    try:
                        spl[1]
                    except IndexError:
                        await message.add_reaction(emoji=emoj1) # react with :+1:
                        await message.add_reaction(emoji=emoj2) # heart
                        await message.add_reaction(emoji=emoj3) # :-1:
                        await log('В сообщениях найден АДМИН ПРЕДАТЕЛЬ который не МЕМ. Поскольку админы уважаются, добавляю к нему кнопки.')
                    else:
                        await log('В сообщениях найден АДМИН ПРЕДАТЕЛЬ который не МЕМ. Поскольку админы уважаются, а он попросил кнопок не добавлять, я не буду.')
                        return
                else:
                    await log('В сообщениях найден АДМИН ПРЕДАТЕЛЬ который не МЕМ. Поскольку админы НЕ уважаются, удаляю его.')
                    message.delete()


    else: # else
        return # do nothing



client.run('ODIzMjM5MDk0NzI4NTIzNzg2.YFd7Jw.bIXDYCBLbAgzD_PxKBbwxKJUaTM')