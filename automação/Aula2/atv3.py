from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


navegador = Firefox()


url = 'https://web.whatsapp.com/'

navegador.get(url)

navegador.maximize_window()

mensagem =" Automação do WhatsApp WEB - SQUAD 6"

nome_do_grupo =" IJJ - BUGOU? QA TÁ ON"


try:
    campo_pesquisa = WebDriverWait(navegador,30).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")))
    campo_pesquisa.click()
    digitar_busca = navegador.find_element(By.CSS_SELECTOR, '.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp')
    sleep(5)
    digitar_busca.send_keys(nome_do_grupo)   
   
    for caractere in nome_do_grupo:
        digitar_busca.send_keys(caractere)
        sleep(0.1)
    digitar_busca.send_keys(Keys.RETURN) 

    clicar_caixa_mensagem = navegador.find_elements(By.XPATH,"//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
    sleep(5)
    clicar_caixa_mensagem[1].click()

    sleep(5)
    digitar_mensagem = navegador.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"][contenteditable="true"]')
    digitar_mensagem.send_keys(mensagem)
    
    for caractere in mensagem:
       digitar_mensagem.send_keys(caractere)
       sleep(0.1)
    
    enviar_mensagem = navegador.find_element(By.CSS_SELECTOR, "button[data-tab='11'][aria-label='Enviar'].tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq")

    sleep(5)
    enviar_mensagem.click()
except Exception as e:
    print("Elemento não encontrado")












