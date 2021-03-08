from selenium import webdriver
import yaml

info = yaml.load(open('pw.yml'))
mail_id =info["gmail"]["email"]
password = info["gmail"]["password"]
url = info["gmail"]["url"]

driver = webdriver.Chrome()

def login(url,mail_address,mail_id,password_address,password,submit_address_1,submit_address) :
    driver.get(url)
    driver.find_element_by_id(mail_address).send_keys(mail_id)
    driver.find_element_by_id(submit_address_1).click()
    driver.implicitly_wait(5)
    driver.find_element_by_name(password_address).send_keys(password)
    driver.find_element_by_id(submit_address).click()


driver.maximize_window()
login(url,"identifierId",mail_id,"password",password,"identifierNext","passwordNext")



