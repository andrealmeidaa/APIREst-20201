import requests,json

URL='http://localhost:5000/marcas'


dados={'nome':'Ferrari'}
headers={'Content-Type':'application/json'}

response=requests.post(url=URL,data=json.dumps(dados),headers=headers)
if response:
    print(response.json())
    


response=requests.get(URL)
if response.status_code==200:
    marcas=response.json()
    for marca in marcas:
        print("ID:{0} - Marca:{1}".format(marca['id'],marca['nome']))