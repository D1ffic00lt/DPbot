import json

import discord
from discord.ext import commands
from discord import app_commands

from textbytesencoder import Encoder

__all__ = (
    "Slash",
)


class Slash(commands.Cog):
    __slots__ = (
        "bot", "encoder",
        "data", "fmt"
    )

    def __init__(self, bot: commands.Bot, encoder: Encoder) -> None:
        super().__init__()
        self.fmt = None
        self.bot = bot
        self.encoder = encoder

    @app_commands.command(name="add_winner")
    @app_commands.guilds(493970394374471680)
    @app_commands.choices(price_class=[
        app_commands.Choice(name="Classic", value="classic"),
        app_commands.Choice(name="Basic", value="basic")
    ])
    async def __add_winner(
            self, inter: discord.Interaction,
            member: discord.Member,
            price_class: app_commands.Choice[str]
    ) -> None:
        if inter.user.id != 401555829620211723:
            await inter.response.send_message("неееее)))", ephemeral=True)
            return
        with open(".json/nitro.json", "r") as file:
            self.data = json.load(file)

        for i in range(len(self.data[price_class.value])):
            if not self.data[price_class.value][i]["used"]:
                self.data[price_class.value][i]["used"] = True
                self.data[price_class.value][i]["winner_id"] = member.id
                with open(".json/nitro.json", "w") as file:
                    json.dump(self.data, file, sort_keys=True, indent=4)
                await inter.response.send_message("✅", ephemeral=True)
                return
        await inter.response.send_message("❌", ephemeral=True)

    @app_commands.command(name="get_nitro")
    @app_commands.guilds(493970394374471680)
    async def __get_nitro(self, inter: discord.Interaction) -> None:
        with open(".json/nitro.json", "r") as file:
            self.data = json.load(file)

        with open(".json/nitro.json", "+w") as file:
            for nitro_class in ["classic", "basic"]:
                for nitro in range(len(self.data[nitro_class])):
                    if self.data[nitro_class][nitro]["winner_id"] == inter.user.id and \
                            not self.data[nitro_class][nitro]["taken"]:
                        await inter.user.send(self.encoder.decrypt(self.data[nitro_class][nitro]["url"]))
                        self.data[nitro_class][nitro]["taken"] = True

            json.dump(self.data, file, sort_keys=True, indent=4)
        await inter.response.send_message("✅")

    @app_commands.command(name="support")
    @app_commands.guilds(493970394374471680)
    async def __support(
            self, inter: discord.Interaction,
            topic: str, description: str,
            member: discord.Member = None
    ) -> None:
        await inter.response.send_message("✅", ephemeral=True)
        emb = discord.Embed(
            title=f"{topic}",
            color=0x2F3136,
            description=f"{'member: -' if member is not None else f'member: {member.mention}'}"
                        f"\n{description}"
        )
        await self.bot.get_channel(572705890524725248).send(embed=emb)

    @commands.command()
    async def sync(self, ctx: commands.context.Context, type_: str = "local"):
        if ctx.author.id == 401555829620211723:
            if type_ == "global":
                self.fmt = await ctx.bot.tree.sync()
                await ctx.reply(f"Synced {len(self.fmt)} (global)")
            else:
                self.fmt = await ctx.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced {len(self.fmt)}")
        else:
            await ctx.message.add_reaction('❌')
