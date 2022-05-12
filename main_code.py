# -*- coding: utf-8 -*-
# !/usr/bin/env python
""" Зачем нужно это поле? """
import os

from config import settings
import discord
from discord.ext import commands
from Cybernator import Paginator as pag
from discord.utils import get
import json

print("\n" + "Program started" + "\n")

__version__ = "0.0.1"

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


@bot.command(aliases=["test"])
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
    "🧚‍♀️": 766295022764818452,
    "🚁": 857287073337966603,
    "🦄": 783504750540619796,
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


@bot.command(aliases=["send_rules"])
async def __send_the_rules(ctx):
    if ctx.author.id == 401555829620211723:
        channel = bot.get_channel(572682163162578946)
        emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/856210141732143134/rules.png')
        await channel.send(embed=emb)
        emb = discord.Embed(title="Общие правила:", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210140923822091/main.png")
        emb.add_field(
            name=u'\u200b',
            value=f'**1.1** Запрещено злоупотребление ненормативной лексики.\n```Мут на 30 минут```', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.2** Запрещено оскорбление администрации.\n```Мут на 3 часа```', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.3** Запрещена реклама любых сторонних ресурсов.\n```Бан навсегда```', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.4** Запрещено распространение личной информации(без согласия).'
                  f'\n```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.5** Запрещено распространение багов сервера.\n```Предупреждение / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.6** Запрещено массовое упоминание ролей без причины\n**Исключение: см. список в конце**'
                  '\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.7** Запрещено разжигание ненависти к рассам, религиям, национальностям.\n'
                  f'```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.8** Запрещены подстрекательства или призывы к нарушению правил сервера.\n'
                  f'```Удаление сообщений / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**1.9** Запрещён +18 контент.\n```Удаление сообщений / Мут / Бан```',
            inline=False)
        # emb.add_field(
        #     name=u"\u200b",
        #     value=f'**1.4**\n``````',
        #     inline=False)
        await channel.send(embed=emb)
        emb = discord.Embed(title="Правила голосовых каналов:", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210142817943552/voice.png")
        emb.add_field(
            name=u"\u200b",
            value=f'**2.1** Запрещено неадекватное поведение в любых его проявлениях.\n**Исключение: см. список в '
                  f'конце** '
                  f'\n```Предупреждение / Мут / Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**2.2** Запрещено использование сторонних программ для воспроизведения звуков через микрофон'
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**2.2** Запрещено использовать программы для изменения голоса.'
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**2.3** Запрещена реклама других проектов/групп/каналов..\n```Бан```',
            inline=False)
        await channel.send(embed=emb)
        emb = discord.Embed(title="Правила текстовых каналов:", colour=discord.Color.from_rgb(47, 49, 54))
        emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210185214361610/chat.png")
        emb.add_field(
            name=u"\u200b",
            value=f'**3.1** Запрещено массовое упоминание ролей без причины\n**Исключение: см. список в конце**'
                  '\n```Предупреждение / Мут```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**3.1** Запрещена реклама других проектов/групп/каналов'
                  '\n```Бан```',
            inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'**3.3** Запрещён флуд / спам\n**Исключение: см. список в конце**'
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
            value='`1.6/3.1` Данные правила не распространяются '
                  'на каналы: <#{}> <#{}> <#{}>, на роли-администраторы'
                  '(выше <@&{}>) и <@&{}>'.format(767431134631297025,
                                                  767670212941316107,
                                                  773600185195692082,
                                                  704292000429637712,
                                                  767430108377907240), inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'`2.1` Данное правило не распространяется на приватные каналы и'
                  f' не является тяжёлым, ||все мы люди||, получить'
                  f'бан за данное нарушение ПРАКТИЧЕСКИ невозможно.', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'`3.3` Данное правило не распространяется на приватные каналы и '
                  f'<#771762570288693258>', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'Правила и примечания будут обновляться <@401555829620211723>', inline=False)
        emb.add_field(
            name=u"\u200b",
            value=f'```ЗАПРЕЩЕНО ЗЛОУПОТРЕБЛЯТЬ НЕДОЧЁТАМИ ПРАВИЛ```\n'
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
