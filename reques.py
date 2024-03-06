import requests
from bs4 import BeautifulSoup
import json


url_login = 'https://ase1.ceti.mx/tecnologo/seguridad/iniciarsesion'
url_home = 'https://ase1.ceti.mx/tecnologo/tgoalumno/horario'

datos_post = {
    'registro': '',
    'password': '',
}

sesion = requests.Session()
sesion.post(url_login, data=datos_post)

response_home = sesion.get(url_home)
print(response_home.content)

soup = BeautifulSoup(response_home.content, 'html.parser')

etiquetas_td = soup.find_all('td', {'align': 'center', 'class' : 'gris'})

valores = [etiqueta.text.strip() for etiqueta in etiquetas_td]

# print(response_home.content)

# with open('output.html', 'w', encoding='utf-8') as file:
#     file.write(soup.prettify())


# with open('valores.json', 'w', encoding='utf-8') as file:
#     json.dump(valores, file, ensure_ascii=False, indent=2)

print(f"Registro:\t\t\t {valores[0]}")
print(f"Nombre:\t\t\t\t {valores[1]}")
print(f"Status:\t\t\t\t {valores[2]}")
print(f"Periodo:\t\t\t {valores[3]}")
print(f"Carrera:\t\t\t {valores[5]}")
print(f"Especialidad:\t\t {valores[6]}")
print(f"Semestre:\t\t\t {valores[7]}")
print(f"CURP:\t\t\t\t {valores[10]}")

# for link in soup.find_all('td'):
#     print(link.get('href'))