import os
import discord
import re
from keep_alive import keep_alive
import asyncio
import requests

client = discord.Client()

def matchEndSentence(word, string):
  return re.match(r"\b(.*{0})\b[ .!?\\-]*$".format(word), string)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="vykio.fr | Dans " + str(len(client.guilds)) + " serveurs!"))
  await update_status()

async def update_status():
  while(True):

    response = requests.get("https://vykio.fr/api/hello")

    if response.json()["live"] == True:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="twitch.tv/vykio en LIVE !"))
    else:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="vykio.fr | Ajouté dans " + str(len(client.guilds)) + " serveurs!"))
    await asyncio.sleep(10)
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if "quoi" in message.content.lower():
    string = message.content.lower()
    #print(string)
    if matchEndSentence("quoi", string):
      await message.channel.send("Feur ! :eyes:")
  elif "oui" in message.content.lower():
    string = message.content.lower()
    if matchEndSentence("oui", string):
      await message.channel.send("Stiti ! :see_no_evil:")
  elif "hein" in message.content.lower():
    string = message.content.lower()
    if matchEndSentence("hein", string):
      await message.channel.send("Deux ! :v:")
  elif "ouais" in message.content.lower():
    string = message.content.lower()
    if matchEndSentence("ouais", string):
      await message.channel.send("Stern ! :cowboy:")
  elif "nan" in message.content.lower() or "non" in message.content.lower():
    string = message.content.lower()
    if matchEndSentence("nan", string) or matchEndSentence("non", string):
      await message.channel.send("Si ! :eye::lips::eye:")

bot_token = os.environ['bot_token']

keep_alive()
client.run(bot_token)
