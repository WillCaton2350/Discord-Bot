import responses
import discord 


async def send_message(message, user_message,is_private):
    try:
        respo = responses.get_response(
            user_message)
        await message.author.send(
            respo) if is_private else await message.channel.send(
                respo)
    except Exception as err:
        print(err)
    

def run_Discord_Bot():
    TOKEN = '00000000000000000000000000000000000000000000000000000'
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guild_messages = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(username, channel)
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message,user_message,is_private=False)
    client.run(TOKEN)
        
