import discord 
import random
from tkinter import Image 
import requests
import os, random
from discord.ext import commands  

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


def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

async def pokemon(message):    
    words = message.content.split(" ")
    url = f'https://pokeapi.co/api/v2/pokemon/{words[1]}'
    res = requests.get(url)
    try:
        data = res.json()
    except:
        await message.channel.send("NO SE ENCONTRÓ")
    else:
        image_url = data["sprites"]["front_default"]
        await message.channel.send(image_url)


async def mem(ctx):
    img_name = random.choice(os.listdir(f'text/images'))
    with open(f'text/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)


def help():
     return """
Comandos:
    /hello: SALUDAR!
    /pass: Generar CONTRASEÑA!
    /coin: Girar una MONEDA, CARA o SELLO
    /emoji: Genera al azar algunos EMOJIS
    /help: Pedir AYUDA
    /duck: Genera una imagen de un PATO al azar
    /pokemon (pokemon): Genera el POKEMÓN escrito   
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

