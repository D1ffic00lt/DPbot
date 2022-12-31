import warnings
import discord
import nest_asyncio

from asyncio import run
from textbytesencoder import Encoder

from bot import DPbot
from config import settings
from modules import *

warnings.filterwarnings("ignore")
nest_asyncio.apply()

print("\n" + "Program started" + "\n")


async def main() -> None:
    intents = discord.Intents.all()
    intents.members = True
    intents.message_content = True

    with open("key.dp", "rb") as file:
        encoder = Encoder(file.read())

    BOT: DPbot = DPbot(
        command_prefix=settings["prefix"],
        intents=intents, case_insensitive=True
    )

    await BOT.add_cog(Events(BOT))
    await BOT.add_cog(Admin(BOT))
    await BOT.add_cog(Slash(BOT, encoder))

    BOT.run(encoder.decrypt(settings["token"]))


if __name__ == '__main__':
    runner = run(main())
