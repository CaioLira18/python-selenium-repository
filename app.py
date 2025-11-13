from selenium import webdriver
import time

# Abrir o navegador
navegador = webdriver.Chrome()

# Acessar Site
navegador.get("https://github.com/CaioLira18/python-selenium-repository")

# Colocar em Full Screen
navegador.maximize_window()

# Selecionar um elemento na tela
botao_verde = navegador.find_element("id", ":R75ab:")

# Clicar Botão
botao_verde.click()

time.sleep(90)