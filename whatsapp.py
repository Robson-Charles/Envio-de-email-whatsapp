from playwright.sync_api import Playwright, sync_playwright, expect
from time import sleep
import tkinter
def esperar_login(page):
    #espera o request de login
    with page.expect_request("https://web.whatsapp.com/img/bg-chat-tile-dark_a4be512e7195b6b733d9110b408f075d.png", timeout=0) as first:
        page.goto("https://web.whatsapp.com")
    #espera o menu aparecer
    while page.is_visible('data-testid=menu', timeout=0) != True:
        sleep(2)
    #tempo estra para não bugar
    sleep(5)

def enviar_menssagem(page):
    menssagem = 'menssagem que sera enviada'

    numeros = ['21900000000', '+55 21 90000-0000', '21 90000-0000']
    # link de envio de msg para qual quer numero
    #Vai tentar entrar no link caso demore dms ele da erro
    #for para realizar o envio para todos os numeros na string
    for c in range(len(numeros)):
        try:
            #tratando o numero
            numero = numeros[c].replace(" ", "").replace("-", "").replace(".", "").replace("+", "")
            print(f'https://web.whatsapp.com/send?phone={numero}&text={menssagem}')
            page.goto(f'https://web.whatsapp.com/send?phone={numero}&text={nomes[c]+menssagem}', timeout=30000)
            page.wait_for_selector('data-testid=send', timeout=0).click()
            #tempo para não bugar
            sleep(2)

        except:
            #menssagem de erro
            tkinter.showwarning(title='Falha ao entrar no link', message='Link de envio demorou demais para carregar')
            exit()

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    esperar_login(page)

    enviar_menssagem(page)





    #
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
