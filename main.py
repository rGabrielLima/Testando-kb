#importar api's: random, keyboard, pyautogui, time
import os

#os.system ("cls") or None

import pyautogui as pg #utilizado para mover o cursor
import random 
import keyboard as kb #utilizado para usar o teclado
import time #utilizado para dar comando de aguardar determinado tempo
## from pynput import mouse #biblioteca que utilizei brevemente para capturar as coordenadas do mouse na tela.
## from pynput import keyboard -- Importação comentada por hora
"""
#utilizando o pyinput para capturar as coordenadas clicadas pelo mouse
def on_click(x, y, button, pressed): #aqui eu criei uma função que define os eixos e botões apertados
    if pressed and (button == mouse.Button.right or button == mouse.Button.left):
        print(x, y) # aqui mostra na tela o eixo de cada botão apertado

with mouse.Listener(on_click=on_click) as coordenadas:
    coordenadas.join()
"""

# -> tentei utilizar o próprio pynput para capturar também a contagem de teclas já digitada, como um progresso, porém eu não consegui fazer o programa funcionar. Deixarei o código comentado, para mais pra frente resolver essa parte, já que ela não é fundamental para o programa.

"""
contagemTeclas = [] # aqui serão armazenadas as teclas que serão clicadas

def on_press(tecla):
    try:
        tecla = tecla.char 
    except AttributeError:
        tecla.char = str(tecla)
        contagemTeclas.append(tecla)
        print(f"{tecla}")
        if tecla == keyboard.Key.esc:
            return False
        
with keyboard.Listener(on_press=on_press) as contagem:
    contagem.join
"""


#variável com parâmetros das letras do alfabeto
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', " ",]

coordX = 554
coordY = 437



#abrir bloco de notas
time.sleep(5) #espera 5s para iniciar o codigo
kb.press("win")
kb.press("m") 
kb.release("win")
kb.release("m") #pressiona e solta o atalho de minimizar

pg.moveTo(coordX,coordY) #move o mouse para a coordenada desejada

pg.click()
pg.click()

time.sleep(2)

pg.click()

kb.press("win")
kb.press("Up Arrow")
kb.release("win")
kb.release("Up Arrow")

pg.click()

# função escrever randomicamente
for i in range(10000): #quantidade de caracteres que será digitado
    escreva = random.choice(letras)
    pg.write(escreva)
    if i == 10000:
        break