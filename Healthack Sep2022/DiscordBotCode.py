tkn = "MTAYMDM2NDA2MjQzMDg1OTI3NQ.GeyCrH.dExukOlUmYzdCuukdxu-xA7gV-15RPLVTBczwc"
import mysql.connector as mycon
import discord as dis
import random as r
bridge = mycon.connect(host='localhost',user='root',password='root@26')
cur = bridge.cursor()
client = dis.Client(intents=dis.Intents.default())
cur.execute('use hippo;')
def createAcc(name):
    if len(name.split()) != 1:
        n = ""
        for i in name.split():
            n = n + i + "_"
        exe = "create table "+n[:-5]+" (persona char(6) not null, age int );"
        cur.execute(exe)
        bridge.commit()
       
    else:
        exe = "create table "+name[:-5]+" (persona char(6) not null, age int, iden char(1) );"
        
        cur.execute(exe)
        bridge.commit()




















@client.event
async def on_ready():
    print("Hippo online!")
@client.event
async def on_message(msg):
    m = msg.content.lower()
    if msg.author == client.user:
        return
    if m.startswith("h.hello"):
        name = str(msg.author)
        cur.execute('show tables;')
        l = []
        for i in cur.fetchall():
            l.append(i[0])
        if name[:-5].lower() not in l:
            createAcc(name)
            await msg.author.send("Please take this quick personality test >_<\nhttps://www.16personalities.com/free-personality-test")
            embed = dis.Embed(title='Success! :white_check_mark:',
                              description=f"{msg.author.mention}'s Account created!",
                              color=0x32CD32)
            await msg.channel.send(embed=embed)
        else:
            embed = dis.Embed(title='Hold up... :raised_hand:',
                              description="You already have an account!",
                              color=0x32CD32)
        await msg.channel.send(embed=embed)
    if m.startswith("h.setup"):
        l = m.split()
        exe = f"insert into hippo values ({l[1]},{l[2]});"
        cur.execute(exe)
        bridge.commit()




client.run(tkn)









