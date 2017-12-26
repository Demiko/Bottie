import discord
import random
import re


class Bottie(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

    async def on_message(self, message:discord.Message):
        if not self.user.mentioned_in(message):
            return
        text:str = message.content.replace(self.user.mention, '').strip()
        print(text)
        if text == "halt":
            info = await self.application_info()
            if message.author.id == info.owner.id:
                await self.send_message(message.channel, content='Bye-bye.')
                await self.logout()
            else:
                await self.send_message(message.channel, content="Only my master can do that!")
            return
        elif text.startswith("roll"):
            params = re.fullmatch(r'([0-9]*)d([0-9]+)', text[5:])
            if params:
                rolls = int(params[1]) if params[1] else 1
                sides = int(params[2])
                responce = "I've rolled %s. Result is %s" % (params[0], sum(random.choices(range(sides), k=rolls)))
                await self.send_message(message.channel, content=responce)
            else:
                await self.send_message(message.channel, content="Sorry. I can't roll that.")
        else:
            await self.send_message(message.channel, content='I\'m alive!')
