import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://spotifycharts.com/regional/{}/weekly/latest"

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(executable_path=r"C:\Program Files\chromedriver.exe", options = chrome_options)

def pegar_top200(country):
    driver.get(url.format(country))
    driver.implicitly_wait(1)
    element = driver.find_element_by_xpath(
            "//table[@class='chart-table']")
    html_content = element.get_attribute('outerHTML')
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find(name='table')
    df_full = pd.read_html(str(table))
    
    df = df_full[0].drop(columns=["Unnamed: 0", "Unnamed: 1", "Unnamed: 2"])
    df["Track"] = df["Track"].str.split(" by ")
    df["Artist"] = ""
    
    for i in range(len(df)):
        df["Artist"][i] = df["Track"][i][1]
        df["Track"][i] = df["Track"][i][0]
    
    return df[["Track", "Artist", "Streams"]]

Andorra = pegar_top200("ad")

Argentina = pegar_top200("ar")

Áustria = pegar_top200("at")

Austrália = pegar_top200("au")

Bélgica = pegar_top200("be")

Bulgária = pegar_top200("bg")

Bolívia = pegar_top200("bo")

Brasil = pegar_top200("br")

Canadá = pegar_top200("ca")

Suíça = pegar_top200("ch")

Chile = pegar_top200("cl")

Colombia = pegar_top200("co")

Costa_Rica = pegar_top200("cr")

Chipre = pegar_top200("cy")

Tchéquia = pegar_top200("cz")

Alemanha = pegar_top200("de")

Dinamarca = pegar_top200("dk")

República_Dominicana = pegar_top200("do")

Equador = pegar_top200("ec")

Estônia = pegar_top200("ee")

Espanha = pegar_top200("es")

Finlândia = pegar_top200("fi")

França = pegar_top200("fr")

Reino_Unido = pegar_top200("gb")

Grécia = pegar_top200("gr")

Guatemala = pegar_top200("gt")

Hong_Kong = pegar_top200("hk")

Honduras = pegar_top200("hn")

Hungria = pegar_top200("hu")

Indonésia = pegar_top200("id")

Irlanda = pegar_top200("ie")

Israel = pegar_top200("il")

Islândia = pegar_top200("is")

Índia = pegar_top200("in")

Itália = pegar_top200("it")

Japão = pegar_top200("jp")

Lituânia = pegar_top200("lt")

Luxemburgo = pegar_top200("lu")

Letônia = pegar_top200("lv")

México = pegar_top200("mx")

Malásia = pegar_top200("my")

Nicarágua = pegar_top200("ni")

Netherlands = pegar_top200("nl")

Noruega = pegar_top200("no")

Nova_Zelândia = pegar_top200("nz")

Panamá = pegar_top200("pa")

Peru = pegar_top200("pe")

Filipinas = pegar_top200("ph")

Polônia = pegar_top200("pl")

Portugal = pegar_top200("pt")

Paraguai = pegar_top200("py")

România = pegar_top200("ro")

Rússia = pegar_top200("ru")

Suécia = pegar_top200("se")

Singapura = pegar_top200("sg")

Eslováquia = pegar_top200("sk")

El_Salvador = pegar_top200("sv")

Tailândia = pegar_top200("th")

Turquia = pegar_top200("tr")

Taiwan = pegar_top200("tw")

Ucrânia = pegar_top200("ua")

Estados_Unidos = pegar_top200("us")

Uruguai = pegar_top200("uy")

Vietnã = pegar_top200("vn")

África_do_Sul = pegar_top200("za")