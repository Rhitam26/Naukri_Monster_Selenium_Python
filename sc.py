config_f="config.json"
log_f ='logs.log'

import logging, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import autoit

import time
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename=log_f, level=logging.INFO, format='%(asctime)s:%(levelname)s: %(message)s')

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome('./Chrome_Driver/chromedriver.exe', options=options)
def naukri(dict_config):
    try:
        logging.info('------ NAUKRI UPDATE PROCESS STARTS -------')
        driver.get("https://www.naukri.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,'//*[@id="login_Layer"]').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input').click()
        un= dict_config["naukri_un"]
        password = dict_config["naukri_pw"]
        driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input').send_keys(un)
        driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input').send_keys(password)
        driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div/div[2]/img').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div/div[1]/div[2]/a').click()
        driver.implicitly_wait(15)
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="attachCV"]'))
            )
        driver.find_element(By.XPATH,'//*[@id="lazyAttachCV"]/div/div/div[2]/div/div/div[1]/div[1]/section/div').click()
        time.sleep(5)
        cv_path = dict_config["cv_path"]
        autoit.control_send("Open","Edit1",cv_path)
        autoit.control_click("Open","Button1")
        logging.info('------ NAUKRI UPDATE PROCESS ENDS -------')
    except:
        logging.error(f'Error while perfomring Naukri Upload')


def foundit(dict_config):
    logging.info('------ MONSTER UPDATE PROCESS STARTS -------')
    driver.get("https://www.foundit.in/")
    driver.maximize_window()
    driver.find_element(By.XPATH,'//*[@id="topHeader"]/div[2]/div[2]/div/div[2]/ul/li[1]/a/span').click()
    un= dict_config["monster_un"]
    password = dict_config["monster_pw"]
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,'//*[@id="signInName"]').send_keys(un)
    driver.find_element(By.XPATH,'//*[@id="password"]').send_keys(password)
    driver.find_element(By.XPATH,'//*[@id="signInbtn"]').click()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH,'//*[@id="topHeader"]/div[2]/div[2]/div/div[2]/ul/li[3]/span/span').click()

    try:
        driver.find_element(By.XPATH,'//*[@id="user-profile-left"]/aside/div[1]/div[2]/div/span').click()
    except:
        print("Exception")

    driver.find_element(By.XPATH,'//*[@id="availableToJoin"]/div/div/span/label').click()

    try:
        driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/aside/div[2]/div/div[2]/div/div/div/div/div/div[5]/div/div/button').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/aside/div[2]/div/div[2]/div/div/div/div/div/div/div/div/button').click()
    except:
        logging.error("Exception Occured while Updating Notice Period")
    logging.info('------ MONSTER UPDATE PROCESS ENDS -------')

def main(dict_config):
    if dict_config['execution_type'] == 'both':
        naukri(dict_config)
        foundit(dict_config)
    elif dict_config['execution_type'] == 'naukri':
        naukri(dict_config)
    elif dict_config['execution_type'] == 'monster':
        foundit(dict_config)


if __name__== '__main__':
    dict_config={}
    error_msg= None
    with open(config_f,'r') as f:
        try:
            dict_config= json.loads(f.read())
        except json.JSONDecodeError:
            error_msg ="Config File Format is corrupt"
        except:
            error_msg= "Error while reading the Config File - This is a new exception"
    if not(error_msg):
        main(dict_config)