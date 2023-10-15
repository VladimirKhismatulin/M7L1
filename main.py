import discord
import random
import os
from discord.ext import commands
from discord import Attachment

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я бот этого сервера!')


@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) != 0:
        for attachment in ctx.message.attachments:
            await attachment.save(f"images\{attachment.filename}")
            await ctx.send(f"Сохранено как {attachment.filename}")
    else:
        await ctx.send("Файл не найден.")


#@bot.command()
#async def help(ctx):
    #await ctx.send("!Help - показывает команды (как ты и догадался), !hint - даёт совет об экологии, !mem - скидывает мем про экологию, !hello - приветствуется с вами.")

bot.run("MTA5Njc2MDk4Nzg3ODY5OTA2OA.G2tH5i.pA89FGjHBXuc_rsfHqWfsYsRbR8WJL2dBVUyzA")