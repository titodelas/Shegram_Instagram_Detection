import requests
from bs4 import BeautifulSoup

def es_perfil_falso(usuario):
    url = f"https://www.instagram.com/{usuario}/"
    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    meta = soup.find_all("meta")
    for m in meta:
        if m.get("property") == "og:description":
            descripcion = m.get("content")
            seguidores = descripcion.split("Followers")[0].strip()
            seguidores = int(seguidores.replace(",", ""))

            publicaciones = descripcion.split("Following")[0].split()[1]
            publicaciones = int(publicaciones.replace(",", ""))

            if publicaciones == 0 or seguidores / publicaciones > 10:
                return True

            return False
