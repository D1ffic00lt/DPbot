# -*- coding: utf-8 -*-
# !/usr/bin/env python
""" Зачем нужно это поле? """
from config import settings
import discord
from discord.ext import commands
from discord.utils import get
import json

print("\n" + "Program started" + "\n")

__version__ = "0.0.2"

bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
    """
        None
    """
    print(f'Logged in as {bot.user.name}')


@bot.command(aliases=["clear"])
async def __r2134oll(ctx):
    if ctx.author.id == 401555829620211723:
        names = ["Diffic00lt", 'D1ffic00lt']
        for i in ctx.guild.members:
            if i.display_name in names:
                print("edit")
                await i.edit(nick=i.name)


@bot.command(aliases=["send_roles"])
async def __test(ctx):
    text = ""
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
    emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/857561471353094164/customroles.png')
    await ctx.send(embed=emb)
    for i in roles:
        text += "\n"
        role = get(ctx.guild.roles, id=roles[i])
        text += f"{i} - {role.mention}"

    emb = discord.Embed(color=0x2F3136,
                        description=f"> Нажмите на реакцию, чтобы получить роль\n{text}\n\n❌ - Снять роль ")
    emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/857563642962509844/gender.png')

    message = await ctx.send(embed=emb)
    for role in roles:
        await message.add_reaction(role)
    await message.add_reaction("❌")
    with open("json/message_id.json", "w+") as file2:
        json.dump(message.id, file2)


roles = {
    "♀": 766295022764818452,
    "♂": 783504750540619796,
    "🚁": 857287073337966603,
    "🪑": 877568277101052014,
    "🦜": 877569386469265428
}


@bot.event
async def on_raw_reaction_add(payload):
    """
    :param payload:
    """
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    member = get(message.guild.members, id=payload.user_id)
    if not member.bot:
        with open("json/message_id.json", "r") as file:
            message_id = json.load(file)
        if payload.message_id == message_id:
            emoji = str(payload.emoji.name)
            if emoji != "❌":
                role = get(message.guild.roles, id=roles[emoji])
                for role2 in roles:
                    role3 = get(message.guild.roles, id=roles[role2])
                    if role3 in member.roles:
                        await member.remove_roles(role3)
                await member.add_roles(role)
            else:
                for role2 in roles:
                    role3 = get(message.guild.roles, id=roles[role2])
                    if role3 in member.roles:
                        await member.remove_roles(role3)
            await message.remove_reaction(emoji, member)


@bot.command(aliases=["send_message"])
async def __send_message(ctx):
    await ctx.channel.purge(limit=1)
    emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
    emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/856210141732143134/rules.png')
    emb.add_field(
        name="**Грядущие изменения правил сервера**",
        value="Сегодня в _15:30_ был проведён совет по поводу смены правил на "
              "сервере, вот частичный список изменений:\n\n"
              "**·** Пункт 1.1 удалён\n**·** Пункт 3.1 не только не для ролей, но и для пользователей\n"
              "**·** Пункт 1.6 удалён\n**·** Правила [Discord Terms of Service](https://discord.com/terms) и "
              "[Discord Community Guidelines](https://discord.com/guidelines)\n"
              "**·** 1.9 18+ заменить на nsfw и добавить жестокий контент\nПункт 3.2 удалён\n"
              "**·** Коммерческая деятельность без согласия администрации запрещена\n"
              "**·** Администрация сама выбирает степень наказания\n"
              "Изменения вступят в силу в ближайшее время"
    )
    await ctx.send(embed=emb)


@bot.command(aliases=["send_rules"])
async def __send_the_rules(ctx):
    if ctx.author.id == 401555829620211723:
        await ctx.channel.purge(limit=1)
        # channel = bot.get_channel(572682163162578946)
        channel = ctx
        emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/856210141732143134/rules.png')
        await channel.send(embed=emb)
        emb = discord.Embed(title="Общие правила", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210140923822091/main.png")
        emb.add_field(
            name=u"\u200b",
            value=f'Мы стараемся придерживаться правил сообщества _'
                  f'Discord Community Guidelines_ и _Discord Terms of Service_, '
                  f'так что ознакомьтесь с ними\n\n'
                  f'**·** [Discord Terms of Service](https://discord.com/terms)\n'
                  f'**·** [Discord Community Guidelines](https://discord.com/guidelines)', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.1** Запрещено оскорбление администрации.\n```Мут на 3 часа```', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.2** Запрещена реклама любых сторонних ресурсов.\n```Бан навсегда```', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.3** Запрещено распространение личной информации(без согласия).'
                  f'\n```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.4** Запрещено распространение багов сервера.\n```Предупреждение / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.5** Запрещено разжигание ненависти к рассам, религиям, национальностям.\n'
                  f'```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.6** Запрещены подстрекательства или призывы к нарушению правил сервера.\n'
                  f'```Удаление сообщений / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.7** Запрещён NSFW контент.\n```Удаление сообщения / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.8** На сервере запрещена коммерческая деятельность без согласия администрации\n```Мут / Бан```',
            inline=False)
        await channel.send(embed=emb)
        emb = discord.Embed(title="Правила голосовых каналов:", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210142817943552/voice.png")
        emb.add_field(
            name=u"\u200b",
            value=f'**2.1** Запрещено неадекватное поведение в любых его проявлениях.\n'
                  f'_Данное правило не распространяется на приватные каналы и'
                  f' не является тяжёлым, ||все мы люди||, получить '
                  f'бан за данное нарушение ПРАКТИЧЕСКИ невозможно._'
                  f'\n```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**2.2** Запрещено использование сторонних программ для воспроизведения звуков через микрофон'
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**2.2** Запрещено использовать программы для изменения голоса'
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        await channel.send(embed=emb)
        emb = discord.Embed(title="Правила текстовых каналов:", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210185214361610/chat.png")
        emb.add_field(
            name=u"\u200b",
            value=f'**3.1** Запрещено массовое упоминание ролей или пользователей без причины\n'
                  '_Данное правило не распространяется на администраторов и модераторов _'
                  '\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**3.3** Запрещён флуд / спам\n'
                  f'_Данное правило не распространяется на приватные каналы и '
                  f'<#771762570288693258>_'
                  '\n```Удаление сообщения / Предупреждение / Мут```',
            inline=False)
        await channel.send(embed=emb)
        emb = discord.Embed(title="Ссылка", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856230192300032010/url.png")
        emb.add_field(
            name=u"\u200b",
            value=f'Ссылка-приглашение на сервер\n'
                  f'https://discord.gg/aYDknKX')
        await channel.send(embed=emb)
        emb = discord.Embed(title="Примечание: ", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856223438237859880/note.png")
        emb.add_field(
            name=u"\u200b",
            value=f'Правила и примечания будут обновляться <@401555829620211723>', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'```diff\n- АДМИНИСТРАЦИЯ САМА ВЫБИРАЕТ СТЕПЕНЬ НАКАЗАНИЯ\n```\n'
                  f'```diff\n- ЗАПРЕЩЕНО ЗЛОУПОТРЕБЛЯТЬ НЕДОЧЁТАМИ ПРАВИЛ\n```\n'
                  f'```diff\n- НЕЗНАНИЕ ПРАВИЛ НЕ ОСВОБОЖДАЕТ ОТ ОТВЕТСТВЕННОСТИ\n```')
        await channel.send(embed=emb)


@bot.command(aliases=["send_shop"])
async def __send_the_shop(ctx):
    goods = {
        "1️⃣": {
            "name": "Рисунок Валеры(<@557562556311535647>",
            "quantity_left": 0,
            "price": 0
            },
        "2️⃣": {
            "name": "Рисунок Яна(<@805465188827398214>",
            "quantity_left": 0,
            "price": 0
        },
        "3️⃣": {
            "name": "Рисунок Максима Лозина(<@692642027900370974>",
            "quantity_left": 0,
            "price": 0
        }
    }
    if ctx.author.id == 401555829620211723:
        channel = bot.get_channel(877570778676224050)
        emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/877574119200284804/SHOP.png')

# @bot.event
# async def on_command_error(ctx, error):
#     """
#
#     :param ctx:
#     :param error:
#     """
#     print(ctx, error)


bot.run(settings['token'])
