import discord
from difflib import SequenceMatcher as perc
import config

client = discord.Client() # init discord


def Main():
    while True:
        @client.event
        async def on_message(message):

            print('cmdpars')

            if message.content.startswith(prefix): # command parser

                await log('Найдена команда: "{0.content}", от {0.author}'.format(message))
                cm = message.content # load message
                cmd = cm.split(str(prefix)) # remove message prefix

                if perc(lambda x: x == " ", cmd, 'обнови конфиг').ratio() > 0.8:
                    if message.author.guild_permissions.administrator:
                        upd_config()
                        await log(f'Обновлен конифг по просьбе {message.author}')
                        await message.delete()
                        return
                    else:
                        await message.delete()


                elif perc(lambda x: x == " ", cmd, 'помощь').ratio() < 0.8:
                    await message.author.send('> **ПОМОЩЬ ПО КОМАНДАМ**\n\nПока что пуста, =(')
                    return

                else:
                    await log('Команда не распознана, поэтому отправлю ему в лс сообщение что она не распознана.')
                    await message.author.send('Ваша команда не распознана! Используйте `Бот, команды`, чтобы посмотреть список команд!')
                    return

            else:
                return
