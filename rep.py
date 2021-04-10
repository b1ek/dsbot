import discord
from difflib import SequenceMatcher as perc
from time import time as time
import sqlite3
import config
import atexit

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

async def on_message(message):

    global toxperc
    toxperc = perc(lambda x: x == " ", msg, 'позер').ratio()
    msg = message.content()

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
        user[1] += -0.025
    
    if user[1] > -0.156669 and user[1] < -0.3 and user[4] > 1:
        await message.author.send(config.msg1leveltoxic)
        user[4] = 1
    
    if user[1] > -0.301 and user[1] < -0.6 and user[4] > 2:
        await message.author.send(config.msg2leveltoxic)
        user[4] = 2
    
    if user[1] > -0.601 and user[1] < -0.9 and user[4] > 3:
        await message.author.send(config.msg3leveltoxic)
        user[4] = 3

    if user[1] > -0.9 and user[4] > 4:
        await message.author.send(config.msg4leveltoxic)
        user[4] = 3

    if user[1] > 1:
        await message.author.send(config.msgTOXBAN)
        message.author.ban(
            reason=f'NeverBot: Система поиска токсиков посчитала этого пользователя слишком токсичным и забанила его. Репутация пользователя на момент бана: {user[1]}'
            )

def attexit():
    db.close()
    print('SystemExit!!!')

atexit.register(attexit)