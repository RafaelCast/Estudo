from fastapi import FastAPI
from pydantic import BaseModel
import os
import re
import requests

app = FastAPI()

def count_comits(usuario: str, repo: str, branch: Optional[str] = None, token: Optional[str] = None) -> int:
    if token is None:
        token = os.getenv("GITHUB_TOKEN")

    url = f"https://api.github.com/repos/{usuario}/{repo}/commits"
    params = {"per_page": 1}

    if branch:
        params["sha"] = branch

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        r = requests.get(url, params=params, headers=headers, timeout=30)
        # Repositório vazio retorna 409
        if r.status_code == 409:
            return 0
        r.raise_for_status()

        # Se houver mais de 1 commit, o GitHub envia o header Link com rel="last"
        link = r.headers.get("Link", "")
        if link:
            # Ex: <...&page=2>; rel="next", <...&page=34>; rel="last"
            for part in link.split(","):
                if 'rel="last"' in part:
                    m = re.search(r"[?&]page=(\d+)", part)
                    if m:
                        return int(m.group(1))

        # Sem header Link: só 0 ou 1 commit na resposta
        data = r.json()
        return len(data)  # 0 ou 1

    except requests.HTTPError as e:
        # Propaga uma mensagem mais amigável
        raise RuntimeError(f"Erro HTTP ao acessar a API do GitHub: {e} - {r.text}") from e
    except requests.RequestException as e:
        raise RuntimeError(f"Erro de rede ao acessar a API do GitHub: {e}") from e

class Message(BaseModel):
    message: str

class Usuario(BaseModel):
    nome: str
    idade: int

@app.get("/")
def status():
    return "API Online"


@app.get("/soma")
def sum_number(a: float, b: float) -> float:
    return a + b

@app.get("/echo")
def echo(data: Message):
    return data

@app.post("/usuario")
def create_user(usuario: Usuario):
    return "Usuario recebido"