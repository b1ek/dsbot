import discord
from datetime import date, datetime
from difflib import SequenceMatcher as perc

"""CONFIG"""
token = "ODIzMjM5MDk0NzI4NTIzNzg2.YFd7Jw.C0xK7GqZ_0hELtPqegdY-N-7v-0"
prefix = 'Бот, '
respect_admin = True
# EMOJIS
emoj1 = '😁'
emoj2 = '♥'
emoj3 = '👎'
"""END OF CONFIG"""

print('Script initialized')

"""
КОМАНДЫ БОТА

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


@client.event
async def on_ready(): # when log in
    print('Login successful! You logged in as {0.user}'.format(client)) # to console



@client.event
async def on_message(message):

    memes = client.get_channel(memeid) # get memes channel
    if message.channel == memes: # if message channel is memes channel
        if message.attachments != []: # if message contain attachments
            await message.add_reaction(emoji=emoj1) # react with :+1:
            await message.add_reaction(emoji=emoj2) # heart
            await message.add_reaction(emoji=emoj3) # :-1:

        else: # ELSE:
            if message.author.guild_permissions.administrator != True: # if author is not administrator:
                await message.delete() # delete his fucking message without attachments
                await message.author.send('К сожалению, в канал <#826670875839168523> вам можно отправлять только картинки, =(') # DM him

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
                    else:
                        return


    if message.startswith(prefix): # command parser
        cm = message.contents # load message
        cmd = cm.split(str(prefix)) # remove message prefix
    else: # else
        return # do nothing
    

client.run('ODIzMjM5MDk0NzI4NTIzNzg2.YFd7Jw.C0xK7GqZ_0hELtPqegdY-N-7v-0')