import discord
from discord.ext import commands
from dislash import Button, ButtonStyle, ActionRow, ResponseType, slash_command


class Slash(commands.Cog, name='Commands module'):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.settings = None
        self.create_channel = None
        self.category = None
        self.bot = bot

    @commands.command()
    async def create(self, ctx):
        self.category = await ctx.guild.create_category("private rooms")
        self.create_channel = await ctx.guild.create_voice_channel(name=f'создать +', category=self.category,
                                                                   user_limit=1)
        self.settings = await ctx.guild.create_text_channel(name="Управление", category=self.category)
        self.msg = await ctx.send("aasd", components=[Button(style=ButtonStyle.green, label="accept")])
        self.response = await self.bot.wait_for("button_click")
        if self.response.channel == ctx.channel:
            if self.response.component.label == "accept":
                await self.response.respond(content="asdasd")

    @slash_command(description="Says Hellasdasdo", test_guilds=[751338987788042241])
    async def helloo(self, inter):
        await inter.respond("Hello from cog!")
