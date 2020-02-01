import discord
import configparser 
import asyncio

client = discord.Client()

config = configparser.RawConfigParser()
config.read('token.properties')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

    if message.content.startswith('$create'):
        channel = message.channel
        creator = message.author
        await message.channel.send('Event name?')
        def check(m):
            return m.channel == channel

        try:
            resp = await client.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send('Oooh a pretty butterfly! [timeout for input]')
        else:
            event_name=resp.content
            await message.channel.send('{}\'s event is: {}'.format(creator, event_name))
            


# Need a local file called token.properties
# [Token]
# value=TOKEN_HERE
# Don't forget to add to .git/info/exclude
# Because we should not check in the token
client.run(config.get('Token', 'value'))