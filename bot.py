import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hi"):
        await message.channel.send("Hi! I am Py-Bot")

client.run('NzY2MjAyMjQwMTEyNjU2Mzk1.X4f7cQ.qD0jVXcomKklqFidkY1JKDBRZp0')
