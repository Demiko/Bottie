import discord
import random
import re


class Bottie(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)

    async def on_ready(self):
        self.appInfo = await self.application_info()

    async def on_message(self, message):
        if message.author.id == self.user.id or not message.server.me.mentioned_in(message):
            return
        print(message.content)
        text = message.content.replace(message.server.me.mention, '').strip()
        response = "I can't recognize the command. Sorry."
        if text=="":
            response = "How can i help you?"
        elif re.match("introduce", text):
            response = "Hi, my name is %s." % (self.appInfo.name)
        elif re.match("roll", text):
            roll = re.match(r"roll (?P<rolls>\d+)?d(?P<sides>\d+)(?P<modifier>[\+-]\d+)?", text)
            if not roll:
                response = "I can't roll that."
            else:
                rolls = int(roll.group('rolls')) if roll.group('rolls') else 1
                sides = int(roll.group('sides'))
                modifier = int(roll.group('modifier')) if roll.group('modifier') else 0
                if rolls < 0 or sides < 0:
                    response = "You know, I would have to go to negative universe to do that. Try something more sane"
                elif rolls == 0 or sides == 0:
                    response = "It's %s, and you know this!" % modifier
                elif rolls > 100:
                    response = "Chill! I have only 100 dice."
                elif sides > 100:
                    response = "Chill! I have only d100 max."
                elif sides == 1:
                    response = "Obviously, it's %s!" % (rolls + modifier)
                else:
                    result = random.choices(range(1, sides+1), k=rolls)
                    response = "I've rolled %s. Result is %s %s." % (roll[0][5:], sum(result) + modifier, result)
        elif re.match("halt", text):
            if message.author.id == self.appInfo.owner.id:
                await self.logout(message.channel)
                return
            else:
                response = "Only my master can do that!"
        response = "%s\n%s" % (message.author.mention, response)
        await self.send_message(message.channel, content=response)

    async def logout(self, channel):
        await self.send_message(channel, content="Bye-bye.")
        await super().logout()
