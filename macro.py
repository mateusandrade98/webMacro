from selenium import webdriver
import time
import mousePosition as mousebot
import pyautogui as gui

firefox = webdriver.Firefox()
firefox.get('https://sigaa.ufpb.br/sigaa/logon.jsf')

meuUsuario = 'batata'
minhaSenha = 'batata'

script = 'alert(\'Robô simulando um humano\')'

listaCaracteresUsuario = []
listaCaracteresSenha = []

for i in range(0,len(meuUsuario)):
    listaCaracteresUsuario.append(meuUsuario[i])

for i in range(0,len(minhaSenha)):
    listaCaracteresSenha.append(minhaSenha[i])

usuario = firefox.find_element_by_name('form:login')
senha = firefox.find_element_by_name('form:senha')
bt = firefox.find_element_by_name('form:entrar')

time.sleep(2)

firefox.execute_script(script=script)

time.sleep(6)

alerta = firefox.switch_to.alert
alerta.dismiss()

time.sleep(1)

positions = mousebot.obterPosicao()

step = 0
for position in positions:
    if position[2] == 1:
        step += 1
        if step == 1:
            for caractere in listaCaracteresUsuario:
                time.sleep(0.05)
                usuario.send_keys(caractere)
        elif step == 2:
            for caractere in listaCaracteresSenha:
                time.sleep(0.05)
                senha.send_keys(caractere)
        else:
            bt.click()
    else:
        gui.moveTo(x=position[0],y=position[1])


if firefox.current_url == 'https://sigaa.ufpb.br/sigaa/portais/discente/beta/discente.jsf':
    informacoes = firefox.find_element_by_class_name('painel-usuario-identificacao').text
    stripInfo = str(informacoes).split('\n')
    print(f'Nome: {stripInfo[0].replace("Olá, ","")}')
    print(f'vínculo: {stripInfo[1]}')
    print(stripInfo[2])
    exit()
