# Import all the libraries needed
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import pandas as pd
import datetime

# today's date
today = datetime.date.today()
print(today)

update = today.strftime("%d.%#m.%Y")

url = "https://markets.businessinsider.com/commodities/historical-prices/oil-price/usd/1.1.2006_{}?type=wti".format(update)
print(url)

# Setting up the browser
browser = webdriver.Chrome("C:\\Users\Lenovo\Documents\Amir\Others\chromedriver_win32\chromedriver.exe")
browser.get(url)

try:
    elem = WebDriverWait(browser, 30).until(
        ec.presence_of_element_located((By.CLASS_NAME, "header-row"))
    )
    soup = Soup(browser.page_source, "html.parser")
except:
    print("website takes too long")
finally:
    browser.quit()

# Create BeautifulSoup object
elem_div = soup.findAll("div", {"id": "historic-price-list"})
# Find tr tag from the html
print(len(elem_div))

elem_tr = elem_div[0].findAll("tr")
print(len(elem_tr))

# Find th tag from the html
header = elem_tr[0].findAll("th")

# Extract all the headers
header_list =[]
for element in header:
    header_list.append(element.text.strip())
print(header_list)

# Extract all the contents
content = []
for each_tr in elem_tr[1:]:
    td = each_tr.findAll("td")
    td_list = []
    for tex in td:
        td_list.append(tex.text.strip())
    content.append(td_list)
print(content)

df = pd.DataFrame(content, columns=header_list)
df["Date"] = pd.to_datetime(df["Date"])
print(df)
df.info()
df.to_csv(r"C:\Users\Lenovo\Documents\Amir\Others\trytry.csv", index=False)
