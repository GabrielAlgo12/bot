import discord

from bot_logic import gen_pass
from bot_logic import gen_emodji
from bot_logic import flip_coin

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")


    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))


    elif message.content.startswith('$generate_emoji'):
        await message.channel.send(gen_emodji)


    elif message.content.startswith('$flip_coin'):
        await message.channel.send(flip_coin)

    elif message.content.startswith('bye'):
        await message.channel.send("\U0001F612")


    else:
        await message.channel.send("No entiendo el comando")

client.run("MTEyNTkyMTE3NTI1MjUxMjg2OA.G3zbGN.x7sqfQqCOk6kmkLgGtBGeeVXXF3RWjTcT-19PI")