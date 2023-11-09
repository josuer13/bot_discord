import discord


import random 


def gen_pass(cantidad):
    contraseña=["+", "-", "/", "*", "!", "&", "$", "#", "?", "=", "@", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    gen_pass=" "
    for i in range(cantidad):
        gen_pass += (random.choice(contraseña)) 
    return gen_pass 


def coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "SELLO"
    

def emoji():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923", "\U0001f468"]
    return random.choice(emoji)


def randint():
    numero = (random.randint(1,100))
    return numero 

def help():
     return """
Comandos:
    /hello: SALUDAR!
    /pass: Generar CONTRASEÑA!
    /coin: Girar una MONEDA, CARA o SELLO
    /emoji: Genera al azar algunos EMOJIS
    /help: Pedir AYUDA   
    /number: Genera un número ALEATORIO
    /math_easy: SUMAS fáciles
    /math_medium: SUMAS medianas
    /math_hard: SUMAS difíciles
    /math_x_easy: MULTIPLICACIONES fáciles
    /math_x_medium: MULTIPLICACIONES medianas
    /math_x_hard: MULTIPLICACIONES difícles
"""


def maths_easy():
    num2 = (random.randint(1,10))
    num1 = (random.randint(1,10))
    num = num2+num1
    return num2,"+", num1, "=", num

def maths_medium():
    num2 = (random.randint(50,100))
    num1 = (random.randint(50,100))
    num = num2+num1
    return num2,"+", num1, "=", num


def maths_hard():
    num2 = (random.randint(600,1000))
    num1 = (random.randint(600,1000))
    num = num2+num1
    return num2,"+", num1, "=", num


def maths_multiplication_easy():
    num2 = (random.randint(1,12))
    num1 = (random.randint(1,12))
    num = num2*num1
    return num2,"*", num1, "=", num


def maths_multiplication_medium():
    num2 = (random.randint(12,50))
    num1 = (random.randint(12,50))
    num = num2*num1
    return num2,"*", num1, "=", num


def maths_multiplication_hard():
    num2 = (random.randint(25,100))
    num1 = (random.randint(25,100))
    num = num2*num1
    return num2,"*", num1, "=", num


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
    if message.content.startswith('/hello'):
        await message.channel.send("Hola!")  
    elif message.content.startswith('/pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('/coin'):
        await message.channel.send(coin())  
    elif message.content.startswith('/emoji'):
        await message.channel.send(emoji())   
    elif message.content.startswith('/help'):
        await message.channel.send(help())
    elif message.content.startswith('/number'):
        await message.channel.send(randint())
    elif message.content.startswith('/math_easy'):
        await message.channel.send(maths_easy())
    elif message.content.startswith('/math_medium'):
        await message.channel.send(maths_medium())
    elif message.content.startswith('/math_hard'):
        await message.channel.send(maths_hard())
    elif message.content.startswith('/math_x_easy'):
        await message.channel.send(maths_multiplication_easy())
    elif message.content.startswith('/math_x_medium'):
        await message.channel.send(maths_multiplication_medium())
    elif message.content.startswith('/math_x_hard'):
        await message.channel.send(maths_multiplication_hard())   
    elif message.content.startswith('/bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)
    

client.run("MTE2NzYyODQ5MjA2MjU4ODkzOQ.GQj22m.p_HNUosoQog6MyeZJDaRSRWxtS9D0PEBJq9XKw")
client.run("")
