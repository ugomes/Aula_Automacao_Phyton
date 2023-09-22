from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import Select

navegador = Firefox()

url = "https://www.jogajuntoinstituto.org/"

def verify_title(title):
    
    assert title in navegador.title
    print("Este é o titulo correto")
    return


navegador.get(url)
def find_element_by_name(nome):
    return navegador.find_element(By.NAME, nome)

navegador.find_element(By.CSS_SELECTOR, 'a[href="/#Contato"]').click()
sleep(5)

form_name = find_element_by_name("nome")

form_name.send_keys("SQUAD 6")

form_email = find_element_by_name("email").send_keys("squad6@teste.com.br")
form_body = find_element_by_name("body").send_keys("Automação com Selenium Web Driver - SQUAD 6")
form_select = find_element_by_name("assunto")


select = Select(form_select)

select.select_by_visible_text("Contratar profissionais")

form_btn = navegador.find_element(By.XPATH, "/html/body/div[1]/div[2]/section[8]/div[1]/form/button")

print(form_btn)

form_btn.submit()


sleep(8)
navegador.quit()





