import discord
from discord.ext import commands

from discord_components import DiscordComponents, ComponentsBot, Button, SelectOption, Select

from unicodedata import *
import unicodedata

import clipboard

import docx2txt

import textwrap

bot = commands.Bot(command_prefix='c.', description='A bot for members of the Cocánb')

DiscordComponents(bot)

class Unicode(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @bot.command(name='tochar', help='Converts unicode codepoints to characters')
  async def tochar(self, ctx, *, codepoint):
    codepoints = codepoint.split(' ')
    responses = list()
    for i in range(len(codepoints)):
      i_dec = int(codepoints[i],16)
      response = chr(i_dec)
      ''' for surrogate chars (failed)
      else:
        my_text = docx2txt.process("Resources/surrogate chars.docx")
        surrogate_char_list = my_text.split("\n")
        response = surrogate_char_list[i_dec-55296]
      '''
      responses.append(response)
    responses = ''.join(responses)
    await ctx.send('`' + responses + '`')

    embed=discord.Embed(title="Hold to copy then delete the final ←",description=responses+'←')
    
    await ctx.send(embed=embed)
    '''
    components = [Button(label="Copy (WIP)", custom_id="button1")])
    while True:
      interaction = await self.bot.wait_for("button_click")
      await interaction.send(content = "Copied to clipboard (WIP)", ephemeral = True)
    '''

  
  @bot.command(name='tocode', help='Converts character to unicode codepoint')
  async def tocode (self, ctx, *, character):
    characters = list(character)
    responses = list()
    for i in range(len(characters)):
      if len(characters[i]) == 3 and  characters[i][0] == '`' and characters[i][2] == '`':
        characters[i] = characters[i][1]
      elif len(character) == 7 and characters[i][0:3] == '```' and characters[i][4:7] == '```':
        characters[i] = characters[i][3]
      else: 
        characters[i] = characters[i]
      response = hex(ord(characters[i]))
      response = response[2:]
      if len (response) == 1:
        response = '000' + response
      elif len (response) == 2:
        response = '00' + response
      elif len (response) == 3:
        response = '0' + response
      elif len (response) == 5:
        response = '0' + response
      else:
        pass
      code = response
      response = code.upper()
      responses.append(response)
    responses = ' '.join(responses)
    responses_extra = textwrap.wrap(responses, 1994)
    for i in responses_extra:
      await ctx.send ('```'+i+'```')
  
  
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