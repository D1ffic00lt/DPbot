# -*- coding: utf-8 -*-
import discord

from discord.ext import commands

from modules.additions import get_time


class DPbot(commands.Bot):
    def __init__(self, command_prefix: str, *, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)
        self.remove_command('help')

    async def on_ready(self) -> None:
        await self.wait_until_ready()
        await self.change_presence(
            status=discord.Status.online,
            activity=discord.Game("Косяк")
        )
        print(f"[{get_time()}] [INFO]: DPbot connected")
