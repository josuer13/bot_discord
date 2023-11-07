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
