import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import os 
import time

def main():
    #Carrega a tabela
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir,"data\\produtos.csv")
    tabela = pd.read_csv(path)

    #instancia o driver
    driver = webdriver.Chrome()

    #loga no site
    driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    driver.find_element(By.ID, "email").send_keys("email@gmail.com")
    driver.find_element(By.ID, "password").send_keys("PASSWORD")
    driver.find_element(By.ID, "pgtpy-botao").click()
    time.sleep(1)
    

    #preenche os produtos de acordo com a tabela encontrada
    for linha in tabela.index:
        driver.find_element(By.ID,"codigo").send_keys(str(tabela.loc[linha,"codigo"]))
        driver.find_element(By.ID,"marca").send_keys(str(tabela.loc[linha,"marca"]))
        driver.find_element(By.ID,"tipo").send_keys(str(tabela.loc[linha,"tipo"]))
        driver.find_element(By.ID,"categoria").send_keys(str(tabela.loc[linha,"categoria"]))
        driver.find_element(By.ID,"preco_unitario").send_keys(str(tabela.loc[linha,"preco_unitario"]))
        driver.find_element(By.ID,"custo").send_keys(str(tabela.loc[linha,"custo"]))
        obs = tabela.loc[linha,"obs"]
        if(not pd.isna(obs)):
            driver.find_element(By.ID,"obs").send_keys(str(obs))
        driver.find_element(By.ID,"pgtpy-botao").click()
    

if __name__ == "__main__":
    main()