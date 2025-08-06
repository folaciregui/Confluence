import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "https://frba-utn-edu.atlassian.net/wiki/rest/api/content"
AUTH = HTTPBasicAuth("folacireguibonilla@frba.utn.edu.ar", "x") # poner tu token
SPACE_KEY = "FRBAUTNEDU"  

def buscar_pagina_por_titulo(titulo):
    params = {
        "title": titulo,
        "spaceKey": SPACE_KEY,
        "expand": "version"
    }
    response = requests.get(BASE_URL, params=params, auth=AUTH)
    response.raise_for_status()
    data = response.json()

    if data["size"] > 0:
        return data["results"][0]["id"]
    else:
        return None

def borrar_pagina(id_pagina):
    url_delete = f"{BASE_URL}/{id_pagina}"
    response = requests.delete(url_delete, auth=AUTH)
    if response.status_code == 204:
        print("Página eliminada con éxito.")
    else:
        print(f"Error al eliminar la página. Código: {response.status_code}")
        print(response.text)

def main():
    titulo = input("Ingresa el título de la página que quieres borrar: ").strip()
    id_pagina = buscar_pagina_por_titulo(titulo)

    if id_pagina:
        confirmar = input(f"Se encontró la página con ID {id_pagina}. ¿Quieres borrarla? (s/n): ").lower()
        if confirmar == "s":
            borrar_pagina(id_pagina)
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró ninguna página con ese título.")

if __name__ == "__main__":
    main()
