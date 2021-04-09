import discord
from difflib import SequenceMatcher as perc
from time import time as time
import sqlite3
import config

db = sqlite3.connect('users.db')
sql = db.cursor()
sql.execute('''CREATE TABLE IF NOT EXISTS users (
    id BIGINT,
    rep REAL
    lbadwrd BIGINT
    lword BIGINT,
    usermsg INT)''')
db.commit()

def match(one, two):
    return perc(lambda x: x == " ", ine, two).ratio()


class Database(object):
    def query(userid):
        sql.execute(f"""SELECT * FROM users WHERE id = ({userid})""")
        ans = sql.fetchone()
        return ans
    
    def edit(userid, rep, lbadwrd, lword, usermsg):
        sql.execute(f'''SELECT * FROM users WHERE id = ({userid})''')
        req = sql.fetchone()
        if req == None:
            sql.execute(f"""INSERT INTO users(id, rep, lbadwrd, lword) VALUES ({userid}, {rep}, {lbadwrd}, {lword})""")
            db.commit()
            req = sql.fetchall()
        else:
            o = float(rep) + float(req[1])
            sql.execute(f'''UPDATE users
                        SET rep = {o}
                            lbadwrd = {lbadwrd}
                            lword = {lword}
                            usermsg = {usermsg}
                        WHERE
                            id = {userid};''')
            db.commit()
        sql.execute(f'''SELECT * FROM users WHERE id = ({userid})''')
        req = sql.fetchone()
        print(req)
    
    def change(userid, rep):
        sql.execute(f'''SELECT * FROM users WHERE id = ({userid})''')
        currnt = sql.fetchone()
    
    def export():
        sql.execute(f'''SELECT * FROM users''')
        return sql.fetchall()
    
    def rem(userid):
        sql.execute(f'''DELETE * FROM users WHERE id = ({userid})''')
    
    def sqlcmd(cmd):
        sql.execute(cmd)

class Reputation(object):

    async def rep_processor(msg, userdb, message):
        
        global toxperc
        toxperc = perc(lambda x: x == " ", msg, 'позер').ratio()

        if message.author == client.user: return
        if toxperc < 0.33333333333333:

            for i in smislwords:

                toxperc = perc(lambda x: x == " ", msg, i).ratio()

                if toxperc > 0.33333333333333:
                    break

                else:
                    pass
        
        user = Database.query(message.author.id)
        user[3] = time()

        # if toxperc > 0.2331:
        #     user[2] = time()
        
        lastbadword = time() - user[2]

        if lastbadword > 5000 and toxperc < 0.33333333333333:
            user[1] += 0.01
        else: pass


        if lastbadword > 10:
            user[1] += 0.025565 / float(f'-{lastbadword}')
        else:
            user[1] += -0.001
        
        if user[1] > -0.156669 and user[1] < -0.3 and user[4] > 1:
            await message.author.send('''
            ---    Важное уведомление    ---
            
            **Уведомление системы поиска токсиков**
            
            В последнее время вы заметили за вами токсичную активность. Если вы не
            прекратите, вам будет выдана пожизненная блокировка аккаунта.

            Ваша токсичная активность низкая. Если вы прекратите токсичить, она снизится.

            Это сообщение было отправлено автоматически. Если вы считаете это ложным срабатыванием, свяжитесь с командой разработки бота.

            *`С уважением, команда поддержки NeveRest. Хорошего дня`*
            ''')
            user[4] = 1
        
        if user[1] > -0.301 and user[1] < -0.6 and user[4] > 2:
            await message.author.send('''
            ---    Важное уведомление    ---
            
            **Уведомление системы поиска токсиков**
            
            В последнее время вы заметили за вами токсичную активность. Если вы не
            прекратите, вам будет выдана пожизненная блокировка аккаунта. Мы уже отправляли
            вам сообщение, но вы проигнорировали его. Не делайте так больше

            Ваша токсичная активность повышенная. Если вы прекратите токсичить, она снизится.

            Это сообщение было отправлено автоматически. Если вы считаете это ложным срабатыванием, свяжитесь с командой разработки бота.

            *`С уважением, команда поддержки NeveRest. Хорошего дня`*
            ''')
            user[4] = 2
        
        if user[1] > -0.601 and user[1] < -0.9 and user[4] > 3:
            await message.author.send('''
            ---    Важное уведомление    ---
            
            **Уведомление системы поиска токсиков**
            
            В последнее время вы заметили за вами токсичную активность. Если вы не
            прекратите, вам будет выдана пожизненная блокировка аккаунта. Вы уже
            проигнорировали 2 предупреждения, **после следущего вам будет выдан бан.**

            Ваша токсичная активность высока. Если вы прекратите токсичить, она снизится.

            Это сообщение было отправлено автоматически. Если вы считаете это ложным срабатыванием, свяжитесь с командой разработки бота.

            *`С уважением, команда поддержки NeveRest. Хорошего дня`*
            ''')
            user[4] = 3

        if user[1] > -0.9 and user[4] > 4:
            await message.author.send('''
            > **КРИТИЧЕСКОЕ УВЕДОМЛЕНИЕ**
            
            **Уведомление системы поиска токсиков**

            Ваш уровень поведения критический. Вы слишком много токсичите, прекратите или вы будете забанены немедленно.
            Прямо сейчас прекратите токсично себя вести по отношению к другим игрокам.

            Ваша токсичная активность крайне высокая.

            Это сообщение было отправлено автоматически. Если вы считаете это ложным срабатыванием, свяжитесь с командой разработки бота.

            *`С уважением, команда поддержки NeveRest. Хорошего дня`*
            ''')
            user[4] = 3

        if user[1] > 1:
            await message.author.send('''
            > **КРИТИЧЕСКОЕ УВЕДОМЛЕНИЕ**
            
            **Уведомление системы поиска токсиков**
            **Ваш аккаунт был заблокирован**

            К сожалению, мы неоднократно предупреждали вас о вашей токсичной активности, и вы успешно проигнорировали все предупреждения.
            Мы очень сожалеем, но мы вынуждены забанить вас в целях сохранения имиджа сервера. Вы можете подать аппеляцию, связавшись с
            коммьюнити менеджером: <@469783042999844864> или <@447438817209614337>

            Это сообщение было отправлено автоматически. Если вы считаете это ложным срабатыванием, свяжитесь с командой разработки бота.

            *`С уважением, команда поддержки NeveRest. Хорошего дня`*
            ''')
            message.author.ban(
                reason=f'NeverBot: Система поиска токсиков посчитала этого пользователя слишком токсичным и забанила его. Репутация пользователя на момент бана: {user[1]}'
                )


print(Database.query(3124678561))