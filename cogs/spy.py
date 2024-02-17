import discord
from discord.ext import commands
import datetime
import time
from pytz import timezone
from datetime import datetime


class spy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timestamp = datetime.now()
        self.logging_channel_id = 990309743555915866
        self.user_id = 918956960571879437


    @commands.Cog.listener()
    async def on_voice_state_update(sef, member, before, after):
        if not before.channel and after.channel:
            if member.id == 730680241265311824:
              ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M %p')
              ind_time1 = datetime.now(timezone("Asia/Kolkata"))
              user = self.bot.get_user(918956960571879437)
              embed = discord.Embed(title = f"Joined Vc", description = f'[{member.name}](https://discordapp.com/users/{member.id}) : Joined Vc\nTime : `{ind_time}`\nExact Data : `{ind_time1}`\nVc Name : {after.channel.mention}', color = 0)
              embed.set_footer(text = f"{member.name} joined vc",icon_url=member.avatar.url)
              embed.set_author( name="Pranav's Spy",icon_url=self.bot.user.avatar.url)
              await user.send(embed=embed)
        elif before.channel and not after.channel:
            if member.id == 730680241265311824:
              ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M %p')
              ind_time1 = datetime.now(timezone("Asia/Kolkata"))
              user = self.bot.get_user(918956960571879437)
              embed = discord.Embed(title = f"Left Vc", description = f'[{member.name}](https://discordapp.com/users/{member.id}) : Left Vc\nTime : `{ind_time}`\nExact Data : `{ind_time1}`\nVc Name : {before.channel.mention}', color = 0)
              embed.set_footer(text = f"{member.name} left vc",icon_url=member.avatar.url)
              embed.set_author( name="Pranav's Spy",icon_url=self.bot.user.avatar.url)
              await user.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
      if str(before.raw_status) == "offline":
        if before.id == 730680241265311824 or before.id == 941762190510264351 :
          ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M %p')
          ind_time1 = datetime.now(timezone("Asia/Kolkata"))
          pranav = self.bot.get_user(self.user_id)
          channel = self.bot.get_channel(self.logging_channel_id)
          embed = discord.Embed(title = f"Target Came Online", description = f'[{before.name}](https://discordapp.com/users/{before.id}) : Came Online\nTime : `{ind_time}`\nExact Data : `{ind_time1}`', color = 0)
          embed.set_footer(text = f"{before.name} is online",icon_url=before.avatar.url)
          embed.set_author( name="Pranav's Spy" ,icon_url=self.bot.user.avatar.url)
          await channel.send(embed = embed)
      #try: 
        #dm = await pranav.create_dm()
        #await dm.send(embed=embed)
      #except:
        #await channel.send("Dms closed")
      
      if str(after.raw_status) == "offline":
        if before.id == 730680241265311824 or before.id == 941762190510264351 :
          ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M %p')
          ind_time1 = datetime.now(timezone("Asia/Kolkata"))
          pranav = self.bot.get_user(self.user_id)
          channel = self.bot.get_channel(self.logging_channel_id)
          embed = discord.Embed(title = f"Target Went Offline", description = f'[{after.name}](https://discordapp.com/users/{after.id}) : Went Offline\nTime : `{ind_time}`\nExact Data : `{ind_time1}`', color = 0)
          embed.set_footer(text = f"{after.name} is offline",icon_url=before.avatar.url)
          embed.set_author( name="Pranav's Spy", icon_url=self.bot.user.avatar.url)
          await channel.send(embed = embed)
      #try: 
        #dm = await pranav.create_dm()
        #await dm.send(embed=embed)
      #except:
        #await channel.send("Dms closed")

    @commands.command()
    async def test(self, ctx):
      ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%I:%M %p')
      ind_time1 = datetime.now(timezone("Asia/Kolkata"))
      embed = discord.Embed(title = f"Target Came Online", description = f'[{ctx.author.name}](https://discordapp.com/users/{ctx.author.id}) : Came Online\nTime : `{ind_time}`\nExact Data : `{ind_time1}`', color = 0)
      embed.set_footer(text = f"{ctx.author.name} is online",icon_url=ctx.author.avatar.url)
      embed.set_author( name="Pranav's Spy" ,icon_url= self.bot.user.avatar.url)
      await ctx.send(embed=embed)
      


    @commands.Cog.listener()
    async def on_ready(self):
        print('Ready!')
        print('Logged in as ---->', self.bot.user)
        print('ID:', self.bot.user.id)


async def setup(bot):
  await bot.add_cog(spy(bot))