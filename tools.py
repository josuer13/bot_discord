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
2", "\U0001F606", "\U0001F923", "\U0001f468"]
    return random.choice(emoji)
