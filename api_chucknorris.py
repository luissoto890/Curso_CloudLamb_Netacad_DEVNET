#importamos los módulos necesarios:
import requests
import json 
#importamos un modulo para traducir el chiste de ingles a español:
from googletrans import Translator


#hacemos una solicitud GET a la API de Chuck Norris para obtener la lista de categorías:
response = requests.get('https://api.chucknorris.io/jokes/categories')
categories = json.loads(response.text) #convertimos formato json a un objeto python más facil de leer y manejar

#imprimimos en consola la lista de categorias:
print('Categorías:')
for category in categories: #recorremos cada elemento de la lista categories
    print('- ' + category) #imprimimos un guion y concatenamos con la categoría

#luego de obtener la lista de categorias, le pedimos al usuario que ingrese la que desee:
category = input('Ingresa una categoría: ')

#creamos una variable URL para consultar a la API sobre una categoria específica
#usamos el formato f para poder agregar valores de variables a la cadena de caracteres, en este caso la variable category
url = f'https://api.chucknorris.io/jokes/random?category={category}'

#hacemos una solicitud GET a la URL que acabamos de crear utilizando la biblioteca requests. 
#La respuesta de la API se almacena en la variable response.
response = requests.get(url)

#cargamos el contenido de la respuesta de la API al un objeto json con json.loads, para hacerlo mas legible 
#luego accedemos solo al valor de la clave value en el objeto json para obtener el chiste, el cual se guarda en la variable joke
joke = json.loads(response.text)['value']

#como el chiste lo entrega en ingles, lo traducimos de la siguiente manera:
translator = Translator() #creamos un objeto translator que contiene la clase Translator del módulo googletrans

#creamnos la variable donde usamosla funcion translate para traducir el chiste,
#la funcion translate pide dos argumentos: el texto que se quiere traducir (joke), y el idioma que se desea (dest="es"), 
#colocamos el .text para solo obtener el texto traducido, ya que aparte de este, cuando solicitamos la traduccion, 
# nos entrega otros datos como la pronunciacion, el idioma original (src=en), y extra_data que es información adicional, 
# normalmene confidencial
joke_es = translator.translate(joke, dest='es').text

#finalmente imprimimos en pantalla los valores deseados:
print(f'Chiste de {category}:')
print(joke)
print (joke_es)

