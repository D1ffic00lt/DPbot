import json
import discord

from discord.ext import commands

from config import settings

__all__ = (
    "Events",
)


class Events(commands.Cog):
    __slots__ = (
        "bot", "roles", "role_to_remove"
    )

    def __init__(self, bot: commands.Bot, *args, **kwargs) -> None:
        super(Events, self).__init__(*args, **kwargs)
        self.bot = bot
        self.roles = settings["roles"]
        self.emoji: str = ""
        self.message_id: int = 0
        self.member = None
        self.channel = None
        self.message = None
        self.role = None
        self.role_to_remove = None

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(ctx, error)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        self.channel = self.bot.get_channel(payload.channel_id)
        self.message = await self.channel.fetch_message(payload.message_id)
        self.member = discord.utils.get(self.message.guild.members, id=payload.user_id)
        if not self.member.bot:
            with open(".json/message_id.json", "r") as file:
                self.message_id = json.load(file)
            if payload.message_id == self.message_id:
                self.emoji = str(payload.emoji.name)
                if self.emoji != "❌":
                    self.role = discord.utils.get(self.message.guild.roles, id=self.roles[self.emoji])
                    for role_from_list in self.roles:
                        self.role_to_remove = discord.utils.get(self.message.guild.roles, id=self.roles[role_from_list])
                        if self.role_to_remove in self.member.roles:
                            await self.member.remove_roles(self.role_to_remove)
                    await self.member.add_roles(self.role)
                else:
                    for role_from_list in self.roles:
                        self.role_to_remove = discord.utils.get(self.message.guild.roles, id=self.roles[role_from_list])
                        if self.role_to_remove in self.member.roles:
                            await self.member.remove_roles(self.role_to_remove)
                await self.message.remove_reaction(self.emoji, self.member)
