import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='c.', description='A bot for members of the Cocánb')

class Acknowledgements(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @bot.command (name='reclist', help='Sends a list of recommended servers')
  async def recommended(self, ctx):
    if ctx.guild.id == 793153755544813598:
      pass
    else:
      await ctx.send ('https://docs.google.com/document/d/1_FyyY8d9SavNzU7AHD5q6FuBLW4Wr3CkRgfXhXfckRA/edit?usp=drivesdk')
  
  @bot.command (name='server', help='Sends a link to the Cocánb server')
  async def server(self, ctx):
    await ctx.send ('https://discord.gg/nc5xRG3xKC')
  
  @bot.command (name='keyboard', help='Sends a file to download the Cocánb keyboard (Windows)\n\nHow to download keyboard (Windows 10):\nStep 1. Download the file below\nStep 2. Unzip the file\nStep 3. Run \"setup.exe\" and follow required steps\nStep 4. Go to Settings > Time & Language > Language > Add preferred language\nStep 5. Download English (Canada) keyboard\nStep 6. After the download has finished, click on English (Canada) in the preferred languages list and select \"Options\"\nStep 7. Click \"Add a keyboard\" and choose \"Cocánb Keyboard\"\n\nNote: if you downloaded the older version of the keyboard, you have to go to Settings > Add or remove programs and search \"Cocánb\" and delete the old keyboard.\nIf this still doesn\'t work, try again but this time go to File Explorer and delete the source file for the keyboard.')
  async def keyboard(self, ctx):
    with open("cocaanb.rar", "rb") as file:
      await ctx.send("How to download keyboard (Windows 10):\nStep 1. Download the file below\nStep 2. Unzip the file\nStep 3. Run \"setup.exe\" and follow required steps\nStep 4. Go to Settings > Time & Language > Language > Add preferred language\nStep 5. Download English (Canada) keyboard\nStep 6. After the download has finished, click on English (Canada) in the preferred languages list and select \"Options\"\nStep 7. Click \"Add a keyboard\" and choose \"Cocánb Keyboard\"\n\nNote: if you downloaded the older version of the keyboard, you have to go to Settings > Add or remove programs and search \"Cocánb\" and delete the old keyboard.\nIf this still doesn\'t work, try again but this time go to File Explorer and delete the source file for the keyboard.", file=discord.File(file, "Cocánb Keyboard"))
  
  @bot.command (name='bot', help='Sends a link to add this bot')
  async def bot(self, ctx):
    await ctx.send ('https://discord.com/api/oauth2/authorize?client_id=801983327023398912&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D801983327023398912%26permissions%3D8%26redirect_uri%3Dhttps%253A%252F%252Fdiscord.com%252Fapi%252Foauth2%252Fauthorize%253Fclient_id%253D801983&scope=bot')