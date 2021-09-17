import discord
import json
import random
from utils import Command

botcf = json.load(open("botconfig.json"))

async def greet_func(client, message, args, prefix):
  target = False
  try:
  	target = message.mentions[0]
  except:
    pass
  
  if not target:
    await message.reply("Invalid command usage")
    return
  
  actions = ["waved at", "yelled 'hi' to", "said 'yo' to"]
  action = actions[random.randrange(0, len(actions))]
  
  embed = discord.Embed(color = message.author.roles[-1].color, description = f"{message.author.mention} {action} {target.mention}")
  embed.set_author(name="Greeting!", icon_url=message.author.avatar_url)
  embed.set_footer(text=message.guild.name, icon_url=message.guild.icon_url)
  
  await message.channel.send(embed=embed)
  
  try:
    await message.delete()
    canDel = True
  except:
    pass
  
  return



# creating cmd objs
greet = Command("greet", "greet target", "fun", f"{botcf['prefix']}greet", greet_func)