from bs4 import BeautifulSoup
import urllib.request , urllib.parse , urllib.error

url = "https://myanimelist.net/topanime.php"

data = urllib.request.urlopen(url)

soup = BeautifulSoup(data, 'html.parser')

tag = soup.find_all("div",{'class':'di-ib clearfix'})

count = 0

for tag in tag:
        count =count +1 
        print(str(count) + "." +tag.text)