# module imports
import discord
import json

# bot/event imports
from utils import Event

# config imports
botcf = json.load(open('botconfig.json'))



async def main_event(client, message, prefix):
  return False

async def ping4prefix_event(client, message, prefix):
  embed = discord.Embed(description = f"prefix: `{prefix}`\nexample: `{prefix}help`", color = message.author.roles[-1].color)
  embed.set_author(name=f"{client.user.name}'s Prefix!")
  embed.set_thumbnail(url=client.user.avatar_url)
  
  await message.reply(embed=embed)



# creating event objs
main = Event("*", main_event)
ping4prefix = Event("<@!885566247041912863>", ping4prefix_event)



# events arr for export
events = [main, ping4prefix]