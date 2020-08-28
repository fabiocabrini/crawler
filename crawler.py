import urllib.request
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

reg_url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp"
req = Request(url=reg_url, headers=headers) 
content = str(urlopen(req).read()) 
print(content)
find = 'de Hoje'
posicao = int(content.index(find) + len(find))
data = content[ posicao : posicao  + 6]

reg_url = "https://www.melhorcambio.com/dolar-hoje"
req = Request(url=reg_url, headers=headers) 
content = str(urlopen(req).read()) 
print(content)
find = '<input type="hidden" value="'
posicao = int(content.index(find) + len(find))
dolar = content[ posicao : posicao  + 4]

reg_url = "https://www.melhorcambio.com/euro-hoje"
req = Request(url=reg_url, headers=headers) 
content = str(urlopen(req).read()) 
find = '<input type="hidden" value="'
print(content)
posicao = int(content.index(find) + len(find))
euro = content[ posicao : posicao  + 4]

reg_url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp"
req = Request(url=reg_url, headers=headers) 
content = str(urlopen(req).read()) 
find = '<span id="max-temp-1">'
print(content)
posicao = int(content.index(find) + len(find))
maxima = content[ posicao : posicao  + 2]

reg_url = "https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp"
req = Request(url=reg_url, headers=headers) 
content = str(urlopen(req).read()) 
print(content)
find = '<span class="_margin-r-20" id="min-temp-1">'
posicao = int(content.index(find) + len(find))
minima = content[ posicao : posicao  + 2]

print("Resultado da busca em" + data)
print("Valor do Dolar: " + dolar)
print("Valor do Euro: " + euro)
print("Temperatura Máxima em São Paulo: " + maxima)
print("Temperatura Mínima em São Paulo: " + minima)
