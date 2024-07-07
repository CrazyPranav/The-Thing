import discord
from discord.ext import commands
import datetime
from discord.utils import get 

class nevermore(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.logging_channel_id = 960185686017867956
    self.rules_channel = 797027464294957067
    self.self_roles = 771309504058490910


  @commands.Cog.listener()
  async def on_member_join(self, member):
    guild = member.guild
    if guild.id == 734418473580494869:
      embed = discord.Embed(title=" <a:ace_heart:865258867234570250> Welcome to Skyline 𖤓  <a:ace_heart:865258867234570250>",color = 0x2f3136, description=f" <a:REAL_RightArrow:865840196927225886> Account Created : <t:{int(member.created_at.timestamp())}:f> \n<a:REAL_RightArrow:865840196927225886> [Rules](https://discord.gg/9jAhQkkUgB) • [Self Roles](https://discord.gg/Etj68bKJJz) • [Drops](https://discord.gg/6DwHyVXkVj)")
      embed.set_footer(text = f" You are {len(guild.members)}th member! | {member}",icon_url=member.display_avatar.url)
      embed.set_image(url= "https://cdn.discordapp.com/attachments/913514091677614160/1259472473661898842/IMG_20240707_170351.jpg?ex=668bcea5&is=668a7d25&hm=999428eee42904e51b521684c7f60bc778f9c7377d6dfbb78a44c9071215baa3&")
      channel = self.bot.get_channel( self.logging_channel_id )
      rules = self.bot.get_channel(self.rules_channel)
      srole = self.bot.get_channel(self.self_roles)
      await rules.send(f"<a:ace_dil:865258883533373450> {member.mention} , Please do follow all the rules! <a:ace_dil:865258883533373450> ",delete_after=10)
      await srole.send(f" <a:ace_dil:865258883533373450> {member.mention} , Please take some roles for yourself ! <a:ace_dil:865258883533373450> ",delete_after=10)
      await channel.send(content=member.mention, embed=embed)

  @commands.command()
  async def weltest(self,ctx):
      guild = ctx.guild
      member = ctx.author
      embed = discord.Embed(title=" <a:ace_heart:865258867234570250> Welcome to Skyline 𖤓  <a:ace_heart:865258867234570250>",color = 0x2f3136, description=f" <a:REAL_RightArrow:865840196927225886> Account Created : <t:{int(member.created_at.timestamp())}:f> \n<a:REAL_RightArrow:865840196927225886> [rules](https://discord.gg/9jAhQkkUgB) • [self roles](https://discord.gg/Etj68bKJJz) • [drops](https://discord.gg/6DwHyVXkVj)")
      embed.set_footer(text = f" You are {len(guild.members)}th member! | {member}",icon_url=member.display_avatar.url)
      embed.set_image(url= "https://cdn.discordapp.com/attachments/913514091677614160/1259472473661898842/IMG_20240707_170351.jpg?ex=668bcea5&is=668a7d25&hm=999428eee42904e51b521684c7f60bc778f9c7377d6dfbb78a44c9071215baa3&")
      channel = self.bot.get_channel( self.logging_channel_id )
      await channel.send(content=member.mention,embed=embed)

async def setup(bot):
  await bot.add_cog(nevermore(bot))
