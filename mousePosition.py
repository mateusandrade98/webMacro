import pyautogui as gui
import json
import sys
from pynput.mouse import Listener
import threading


positions = []

gui.FAILSAFE = False

eventos = []

def on_click(x, y, button, pressed):
    if pressed == True:
        if 'Button.left' in str(button):
            print(f'Left Button Pressed ({x},{y})')
            eventos.append([x,y])

def ouvindoMouseClick():
    print('Evento de clique sendo ouvido...')
    with Listener(on_click=on_click) as listener:
        try:
            listener.run()
        except KeyboardInterrupt:
            listener.stop()
        finally:
            listener.stop()

def remover_repetidas(lista):
    l = []
    for elemento in lista:
        if elemento not in l:
            l.append(elemento)
    return l

def adicionar_evento_de_clique(eventos,positions):
    result = []
    for position in positions:
        for evento in eventos:
            if (position[0], position[1]) == (evento[0], evento[1]):
                result.append([position[0], position[1], 1])
                continue
        result.append(position)
    return result


try:
    if sys.argv[1] == 'gravar':
        try:
            ouvindoEvento = threading.Thread(target=ouvindoMouseClick)
            ouvindoEvento.start()
        except KeyboardInterrupt:
            exit()

        while True:
            try:
                x,y = gui.position()
                positions.append((x,y,0))
            except KeyboardInterrupt:
#                print('Quantidade total de posições:',len(positions))
#                positions = remover_repetidas(positions)
#                print('Quantidade de posições válidas:',len(positions))
                positions = adicionar_evento_de_clique(eventos,positions)
                clicks = 0
                for click in positions:
                    if click[2] == 1:
                        clicks += 1
                if clicks > 0:
                    clicks = clicks / 2
                print('Quantidades de cliques:',int(clicks))
                positions = remover_repetidas(positions)
                print('Quantidade de posições:',len(positions))
                positions = json.dumps(positions)
                with open('positions.json', 'wt') as f:
                    f.write(positions)
                    f.close()
                print('Posições do mouse salvado em -> positions.json')
                exit()
except IndexError:
    print('\n')

def movimentarMouse():
    positions = json.loads(open('positions.json','rt').read())

    xy = []
    for position in positions:
        xy.append(position)

    for mouseposition in xy:
        print(mouseposition)
        gui.moveTo(x=mouseposition[0],y=mouseposition[1],duration=0.1)

def obterPosicao():
    positions = json.loads(open('positions.json', 'rt').read())
    xyc = []
    for position in positions:
        xyc.append(position)
    return xyc