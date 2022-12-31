import json
import discord

from discord.ext import commands

from config import settings
__all__ = (
    "Admin",
)


class Admin(commands.Cog):
    __slots__ = (
        "bot", "roles", "text",
        "emb", "message"
    )

    def __init__(self, bot: commands.Bot, *args, **kwargs) -> None:
        super(Admin, self).__init__(*args, **kwargs)
        self.bot = bot
        self.roles = settings["roles"]
        self.text: str
        self.emb: discord.Embed
        self.message: discord.Message

    @commands.command(aliases=["send_roles"])
    async def __send_roles(self, ctx: commands.context.Context):
        if ctx.author.id != 401555829620211723:
            return
        self.text = ""
        await ctx.channel.purge(limit=1)
        self.emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(
            url='https://cdn.discordapp.com/attachments/572705890524725248/857561471353094164/customroles.png'
        )
        await ctx.send(embed=self.emb)
        for i in self.roles:
            self.text += "\n"
            self.role = discord.utils.get(ctx.guild.roles, id=self.roles[i])
            self.text += f"{i} - {self.role.mention}"

        self.emb = discord.Embed(
            color=0x2F3136,
            description=f"> Нажмите на реакцию, чтобы получить роль\n{self.text}\n\n❌ - Снять роль "
        )
        self.emb.set_image(
            url='https://cdn.discordapp.com/attachments/572705890524725248/857563642962509844/gender.png'
        )

        self.message = await ctx.send(embed=self.emb)
        for emoji in self.roles:
            await self.message.add_reaction(emoji)
        await self.message.add_reaction("❌")
        with open(".json/message_id.json", "w+") as file2:
            json.dump(self.message.id, file2)

    @commands.command(aliases=["send_message"])
    async def __send_message(self, ctx):
        if ctx.author.id != 401555829620211723:
            return
        await ctx.channel.purge(limit=1)
        self.emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/856210141732143134/rules.png')
        self.emb.add_field(
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
        await ctx.send(embed=self.emb)

    @commands.command(aliases=["send_rules"])
    async def __send_rules(self, ctx):
        if ctx.author.id != 401555829620211723:
            return
        await ctx.channel.purge(limit=1)
        self.emb = discord.Embed(colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url='https://cdn.discordapp.com/attachments/572705890524725248/856210141732143134/rules.png')
        await ctx.send(embed=self.emb)
        self.emb = discord.Embed(title="Общие правила", colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210140923822091/main.png")
        self.emb.add_field(
            name=u"\u200b",
            value=f'Мы стараемся придерживаться правил сообщества _'
                  f'Discord Community Guidelines_ и _Discord Terms of Service_, '
                  f'так что ознакомьтесь с ними.\n\n'
                  f'**·** [Discord Terms of Service](https://discord.com/terms)\n'
                  f'**·** [Discord Community Guidelines](https://discord.com/guidelines)', inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.1** Запрещено оскорбление администрации.\n```Мут```', inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.2** Запрещена реклама любых сторонних ресурсов.\n```Мут / Бан```', inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.3** Запрещено распространение личной информации (без согласия).'
                  f'\n```Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.4** Запрещено распространение багов сервера.\n```Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.5** Запрещено разжигание ненависти к расам, религиям, национальностям.\n'
                  f'```Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.6** Запрещены подстрекательства или призывы к нарушению правил сервера.\n'
                  f'```Удаление сообщений / Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.7** Запрещён NSFW контент.\n'
                  f'_Данное правило не распространяется на_ '
                  f'<#786797979583512586>.\n'
                  f'```Удаление сообщения / Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**1.8** На сервере запрещена коммерческая деятельность без согласия администрации.'
                  f'\n```Мут / Бан```',
            inline=False)
        await ctx.send(embed=self.emb)
        self.emb = discord.Embed(title="Правила голосовых каналов", colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210142817943552/voice.png")
        self.emb.add_field(
            name=u"\u200b",
            value=f'**2.1** Запрещено неадекватное поведение в любых его проявлениях.\n'
                  f'_Данное правило не распространяется на приватные каналы и'
                  f' не является тяжёлым, получить '
                  f'бан за данное нарушение ПРАКТИЧЕСКИ невозможно._ ||(все мы люди)||'
                  f'\n```Предупреждение / Мут / Бан```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**2.2** Запрещено использование сторонних программ для воспроизведения звуков через микрофон '
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**2.3** Запрещено использовать программы для изменения голоса '
                  f'(Если это кому-то мешает).\n```Предупреждение / Мут```',
            inline=False)
        await ctx.send(embed=self.emb)
        self.emb = discord.Embed(title="Правила текстовых каналов", colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856210185214361610/chat.png")
        self.emb.add_field(
            name=u"\u200b",
            value=f'**3.1** Запрещено массовое упоминание ролей или пользователей без причины\n'
                  '_Данное правило не распространяется на администраторов и модераторов._'
                  '\n```Предупреждение / Мут```',
            inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'**3.2** Запрещён флуд / спам\n'
                  f'_Данное правило не распространяется на приватные каналы и_  '
                  f'<#771762570288693258>.'
                  '\n```Удаление сообщения / Предупреждение / Мут```',
            inline=False)
        await ctx.send(embed=self.emb)
        self.emb = discord.Embed(title="Ссылка", colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856230192300032010/url.png")
        self.emb.add_field(
            name=u"\u200b",
            value=f'Ссылка-приглашение на сервер.\n'
                  f'https://discord.gg/aYDknKX')
        await ctx.send(embed=self.emb)
        self.emb = discord.Embed(title="Примечание ", colour=discord.Color.from_rgb(47, 49, 54))
        self.emb.set_image(url="https://cdn.discordapp.com/attachments/572705890524725248/856223438237859880/note.png")
        self.emb.add_field(
            name=u"\u200b",
            value=f'Правила и примечания будут обновляться <@401555829620211723> и командой.', inline=False)
        self.emb.add_field(
            name=u"\u200b",
            value=f'```diff\n- АДМИНИСТРАЦИЯ САМА ВЫБИРАЕТ СТЕПЕНЬ НАКАЗАНИЯ И '
                  f'ВПРАВЕ НАЗНАЧИТЬ НАКАЗАНИЕ ЖЕСТЧЕ ИЛИ МЯГЧЕ ПРЕДЛОЖЕННОГО\n```\n'
                  f'```diff\n- ЗАПРЕЩЕНО ЗЛОУПОТРЕБЛЯТЬ НЕДОЧЁТАМИ ПРАВИЛ\n```\n'
                  f'```diff\n- НЕЗНАНИЕ ПРАВИЛ НЕ ОСВОБОЖДАЕТ ОТ ОТВЕТСТВЕННОСТИ\n```'
                  f'АДМИНИСТРАТОРЫ ВЫШЕ <@&767430108377907240> ВКЛЮЧИТЕЛЬНО '
                  f'ОСВОБОЖДАЮТСЯ ОТ ОТВЕТСТВЕННОСТИ\n\n'
                  f'ГЛАВНЫЕ АДМИНИСТРАТОРЫ (<@&567377820209250314> и '
                  f'<@&493982783048384512>) МОГУТ ОТМЕНИТЬ НАКАЗАНИЕ')
        await ctx.send(embed=self.emb)
