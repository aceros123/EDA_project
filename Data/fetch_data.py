import requests


def fetch_data():
    API_URL = "https://www.datos.gov.co/resource/nxt2-39c3.json?$limit=1000000"
    try:
        response = requests.get(API_URL, timeout=60)
        if response.status_code == 200:
            print("Datos recibidos correctamente.")
            data = response.json()
        else:
            print(
                f"Error al obtener los datos: {response.status_code} - {response.reason}")
    except Exception as e:
        print(f"Error al obtener los datos: {e}")

    return data


pass
