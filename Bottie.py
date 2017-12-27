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
        if text.startswith("roll"):
            params = re.fullmatch(r'([0-9]*)d([0-9]+)()', text[5:])
            if params:
                rolls = int(params[1]) if params[1] else 1
                sides = int(params[2])
                if rolls == 0 or sides == 0:
                    response = "It's zero, and you know it! :angry:"
                elif rolls > 100:
                    response = "Chill! I have only 100 dice."
                elif sides > 100:
                    response = "Chill! I have only d100 max."
                elif sides == 1:
                    response = "Obviously, it's %s!" % (rolls)
                else:
                    roll = random.choices(range(1, sides+1), k=rolls)
                    response = "I've rolled %s. Result is %s %s." % (params[0], sum(roll), roll)
                response = "%s, %s" % (message.author.mention, response)
                await self.send_message(message.channel, content=response)
            else:
                await self.send_message(message.channel, content="Sorry. I can't roll that.")
            return
        await self.send_message(message.channel, content='Command not recognized. Sorry.')
