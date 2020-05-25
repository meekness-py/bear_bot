import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print('>> Bot is online <<')

@bot.event
async def on_memder_join(member):
    channel = bot.get_channel(714487045136842803)
    await channel.send(F'{member} 歡迎新成員~!')

@bot.event
async def on_memder_remove(member):
    channel = bot.get_channel(714487045136842803)
    await channel.send(F'{member} 可惜已離開我們...')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} (ms)')
    
bot.run('NzE0NDUxNzczNDIyODI5Njcw.Xsu4gg.LZ4njGmblA53ogK6Gjg9IVVJv9w')