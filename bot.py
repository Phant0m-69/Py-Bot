import discord
import os
npm i profanities

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Hi! I am Py-Bot")

client.run(os.environ['TOKEN'])

#anti-profanity filter
var profanities = require('profanities',)

//profanity
for(x in profanities)
  if(message.content.toUpperCase() == profanities(x).toUpperCase())
     message.channel.send("Hey, Don't say that!")
     message.delete()
     return;
