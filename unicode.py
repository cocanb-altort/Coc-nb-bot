import discord
from discord.ext import commands

from unicodedata import *
import unicodedata

bot = commands.Bot(command_prefix='c.', description='A bot for members of the Cocánb')

class Unicode(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @bot.command(name='tochar', help='Converts unicode codepoint to character')
  async def tochar(self, ctx, codepoint):
    response = chr(int(codepoint, 16))
    await ctx.send('```' + response + '```')

  @bot.command(name='tocode', help='Converts character to unicode codepoint')
  async def tocode(self, ctx, *, character):
    if len(character) == 3 and character[0] == '`' and character [2] == '`':
      character = character[1]
    elif len(character) == 7 and character [0:3] == '```' and character [4:7] == '```':
      character = character[3]
    else: 
      character = character
    response = hex(ord(character))
    response = response[2:]
    if len (response) == 1:
      response = '000' + response
    elif len (response) == 2:
      response = '00' + response
    elif len (response) == 3:
      response = '0' + response
    else:
      pass
    code = '`U+' + response + '`'
    await ctx.send(code.upper())
  
  @bot.command(name='todesc', help='Converts unicode codepoint to description')
  async def todesc(self, ctx, codepoint):
    char=chr(int(codepoint, 16))
    try:
      await ctx.send(unicodedata.name(char))
    except:
      await ctx.send('<no description>')
    
  @bot.command(name='unicode', help='Sends full unicode chart\n\nSupported file formats: .zip, .rar, .tar.gz or .jar file')
  async def unicode(self, ctx, format:str='zip'):
    if format == 'zip' or format == '.zip':
      with open("Resources/Full Unicode Charts/Full Unicode Chart.zip", "rb") as file:
          await ctx.send("Full Unicode Chart.zip", file=discord.File(file, "Full Unicode Chart.zip"))
    elif format == 'rar' or format == '.rar':
      with open("Resources/Full Unicode Charts/Full Unicode Chart.rar", "rb") as file:
          await ctx.send("Full Unicode Chart.rar", file=discord.File(file, "Full Unicode Chart.rar"))
    elif format == '.tar.gz' or format == 'tar.gz' or format == 'targz' or format == 'gz' or format == '.gz':
      with open("Resources/Full Unicode Charts/Full Unicode Chart.tar.gz", "rb") as file:
          await ctx.send("Full Unicode Chart.tar.gz", file=discord.File(file, "Full Unicode Chart.tar.gz"))
    elif format == 'jar' or format == '.jar':
      with open ("Resources/Full Unicode Charts/Full Unicode Chart.jar", "rb") as file:
        await ctx.send("Full Unicode Chart.jar", file=discord.File(file, "Full Unicode Chart.jar"))
    else:
      await ctx.send("Invalid format")