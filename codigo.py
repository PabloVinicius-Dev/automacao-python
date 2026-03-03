#Bibliotecas = pacote de código.
#Passo a passo de códigos.
#Primeiro passo: entrar no sistema da empresa.
#Segundo passo: fazer login.
#Terceiro passo: Abir a base de dados.
#Quarto passo: Cadastrar um produto.
#Quinto passo: Repetir o passo 4 até acabar a lista.

#pyautogui.click -> clica
#pyautogui.write -> escreve texto
#pyautogui.press -> aperta uma teTESE0003817TESE0005016cla
#pyautogui.hotkey -> aperta um atalho

import pyautogui

import time #biblioteca para conseguir da uma segurada no tempo

pyautogui.PAUSE = 0.5 # Modelo paTESA0002010ra esperar um pouco antes de executar tudo.


pyautogui.press("win") #pressiona na tecla que estar entre ""
pyautogui.write("Chorme") #escreve um texto
pyautogui.press("enter") #pressiona um atalho e abre o Chorme

#Fazer login:
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3) #sleep é para voce fazer uma definição de tempo.
pyautogui.click(x=656, y=467)
pyautogui.write("pabllo6503@gmail.com")
pyautogui.press("tab")
pyautogui.write("Pablo123")
pyautogui.press("tab")
pyautogui.press("enter")
#pausa para o site carregar
time.sleep(2)
#abrir base de dados: (importar aquivo)
import pandas #Trabalha com dados
tabela = pandas.read_csv("produtos.csv") #ler arquivos que temos, tanto faz ser csv ou qualquer outro.

#para cada linha da minha tabela eu vou executar o código dnv:
for linha in tabela.index:

#código
    pyautogui.click(x=875, y=313)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

#marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

#tipo
    tipo = str(tabela.loc[linha, "tipo"]) 
    pyautogui.write(tipo)
    pyautogui.press("tab")

#categoria
    categoria =str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

#preço
    preco_unitario =str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

#custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

#obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    #scroll(voltar para o inicio da tela)
    pyautogui.scroll(5000) 

