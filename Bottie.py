import discord
from discord import channel


class Bottie(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

    async def on_message(self, message:discord.Message):
        idTag = '<@%s>' % message.server.me.id
        if not message.content.startswith(idTag):
            return

        text:str = message.content.replace(idTag, '').strip()
        print(text)
        if text == "halt":
            await self.send_message(message.channel, content='Bye-bye')
            await self.logout()
        else:
            await self.send_message(message.channel, content='I\'m alive')
