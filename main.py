import requests
import soup as soup
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
site='https://currency.com/crypto'

full_page=requests.get(site, headers=headers)
soup=BeautifulSoup(full_page.content, 'html.parser')

convert0=soup.findAll("span",{"class":"table-instruments__description"})

convert = soup.findAll("span", {"class":"name"})
convert1=soup.findAll("span",{"class":"name"})
convert4=soup.findAll("span",{ "class":"table-instruments__price negative-price"})
convert5=soup.findAll("th",{"class":"Name"})
print(convert1,convert,convert0,convert4,convert5)
