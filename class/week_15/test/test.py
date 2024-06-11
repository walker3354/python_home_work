import requests
 
# for i in range(1910):
url = f'https://tw.stock.yahoo.com/class-quote?sectorId=37&exchange=TAI'
res = requests.get(url)
print(res.text)
