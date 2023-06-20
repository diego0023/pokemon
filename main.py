import requests
import random
import mysql.connector


def obtener_pokemon_random():
    random_id = random.randint(1, 898)
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    respuesta = requests.get(url)
    datos = respuesta.json()

    nombre = datos["name"]
    numero = datos["id"]
    print(f"#{numero}: {nombre.capitalize()}")

    return (numero, nombre.capitalize())


def guardar_en_base_de_datos(pokemon):
    conexion = mysql.connector.connect(
        host="ls-2ae21f649b4cfd43e38854e7b977523dc45bea2b.ctjurabuhnva.us-east-1.rds.amazonaws.com",
        user="admin",
        password="lospachessondepapaydearroz1833",
        database="pokemon"
    )

    cursor = conexion.cursor()
    consulta = "INSERT INTO pokemon (numero, nombre) VALUES (%s, %s)"
    cursor.execute(consulta, pokemon)
    conexion.commit()

    cursor.close()
    conexion.close()


def main():
    for _ in range(10):
        pokemon = obtener_pokemon_random()
        guardar_en_base_de_datos(pokemon)


if __name__ == "__main__":
    main()
