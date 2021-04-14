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
    rep REAL,
    lbadwrd BIGINT,
    lword BIGINT,
    warned INT)''') # warned = уровень предупреждения
db.commit()

client = discord.Client()

def match(one, two):
    return perc(lambda x: x == " ", ine, two).ratio()


class Database(object):
    def query(userid):
        sql.execute(f"""SELECT * FROM users WHERE id = ({userid})""")
        ans = sql.fetchone()
        if ans != tuple:
            Database.edit(userid, 0, 0, 0, 0)
            sql.execute(f"""SELECT * FROM users WHERE id = ({userid})""")
            ans = sql.fetchone()
        return ans
    
    def edit(userid, rep, lbadwrd, lword, warned):
        sql.execute(f'''SELECT * FROM users WHERE id = ({userid})''')
        req = sql.fetchone()
        if req == None:
            sql.execute(f"""INSERT INTO users(id, rep, lbadwrd, lword, warned) VALUES ({userid}, {rep}, {lbadwrd}, {lword}, {warned})""")
            db.commit()
            req = sql.fetchall()
        else:
            o = float(rep) + float(req[1])
            sql.execute(f'''UPDATE users
                        SET rep = {o},
                            lbadwrd = {lbadwrd},
                            lword = {lword},
                            warned = {warned}
                        WHERE
                            id = {userid};''')
            db.commit()
        sql.execute(f'''SELECT * FROM users WHERE id = ({userid})''')
        req = sql.fetchone()
        print(req)
    
    def close():
        db.close()
    
    def open():
        db = sqlite3.connect('users.db')
    
    def export():
        sql.execute(f'''SELECT * FROM users''')
        return sql.fetchall()
    
    def rem(userid):
        sql.execute(f'''DELETE * FROM users WHERE id = ({userid})''')
    
    def sqlcmd(cmd):
        sql.execute(cmd)

async def repproc(message):
    msg = ''.join(sorted(set(message.content), key=message.content.index))
    print(msg)
    global toxperc
    toxperc = perc(lambda x: x == " ", msg, 'позер').ratio()

    if message.author == client.user: return
    if message.channel == discord.abc.PrivateChannel: return

    
    if toxperc > 0.725:
        for i in config.badwords:
            toxperc = perc(lambda x: x == " ", msg, i).ratio()

            if toxperc > 0.725:
                print(i)
                print(toxperc)
                break

            else:
                pass
    
    user = list(Database.query(message.author.id))
    print(user)

    
    # if toxperc > 0.2331:
    #     user[2] = time()

    # formulas
    if toxperc > 0.725:
        #print(user[2]-time(), ' =|= ', -0.1/user[2]-time())
        user[2] = time()
        if time > 1618368743.931187: user[1] += -0.1/user[2]-time()
    else:
        user[1] += 0.025

    # notifications
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
        user[4] = 4

    if float(user[1]) < -0.99999999999999999:
        print(user[1])
        await message.author.send(config.msgTOXBAN)
        await message.author.ban(reason=f'NeverBot: Система поиска токсиков посчитала этого пользователя слишком токсичным и забанила его. Репутация пользователя на момент бана: {user[1]}')

    Database.edit(user[0], user[1], user[2], user[3], user[4])
    return 'exit'

def attexit():
    db.close()
    print('SystemExit!!!')

atexit.register(attexit)