import discord
from discord.ext import commands

from discord.utils import get

class Moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name='kick',help='Kicks people')
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')
  
  @commands.command(name='ban',help='Bans people')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')