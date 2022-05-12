# -*- coding: utf-8 -*-
from pypresence import Presence
from time import time
from discord.ext import commands
import discord
import config2

bot = commands.Bot(command_prefix=config2.settings["prefix"], intents=discord.Intents.all())
btns = [
    {
        "label": "DPcoin BOT",
        "url": "https://vk.com/dpcoinbot"
    },
    {
        "label": "Антон",
        "url": "https://www.youtube.com/channel/UCSs94sM5xgtaZ759RlFTXpA"
    }
]

RPC = Presence("765825973601697815")
RPC.connect()
RPC.update(
    state="Антик заплатил за рекламу",
    buttons=btns,
    details="DPcoin BOT топ!",
    large_image="avatar512",
    small_image="antik",
    start=time()
)
# @bot.event
# async def on_ready():
#     await bot.change_presence(status=discord.Status.online, activity=RPC)
#     print(1)
bot.run(config2.settings['token'])
