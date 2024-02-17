import discord
from discord.ext import commands
import datetime
import time
import asyncio
from pytz import timezone
from datetime import datetime


class timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timestamp = datetime.now()
        self.channel_id = 785715573946318868
        

    @commands.Cog.listener()
    async def on_message(self, msg):
      if msg.channel.id == self.channel_id:
        if "RPG love share" in msg.content:
          await asyncio.sleep(45)
          await msg.channel.send(f"{msg.author.mention} , cooldown over!")
          




async def setup(bot):
  await bot.add_cog(timer(bot))