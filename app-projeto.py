import pyautogui
from time import sleep

# 1 - clicar e digitar meu usuário
pyautogui.click(866,448,duration=0.01)
pyautogui.write("kalew")
# 2 - Clicar e digitar minha senha
pyautogui.click(854,477,duration=0.01)
pyautogui.write("123")
# 3 - Clicar em "Enter"
pyautogui.click(710,511,duration=0.01)
# 4 - Extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
#     1 - clicar e digitar produto
        pyautogui.click(531,440,duration=0.01)
        pyautogui.write(produto)
#     2 - clicar e digitar quantidade
        pyautogui.click(530,464,duration=0.01)
        pyautogui.write(quantidade)
#     3 - clicar e digitar preço
        pyautogui.click(529,490,duration=0.01)
        pyautogui.write(preco)
#     4 - clicar em registrar
        pyautogui.click(433,646,duration=0.01)
