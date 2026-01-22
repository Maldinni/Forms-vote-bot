import os
from pathlib import Path
from dotenv import load_dotenv # Recebe as variáveis de ambiente

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
#print(BASE_DIR)
teste = load_dotenv(BASE_DIR / "keys.env")  # Carrega o arquivo .env localizado na raiz do projeto
#print(teste)

#as configs de app receberão os itens do dicionario para acertar os parametros

BASEPATH = Path(os.getenv("LOCAL_BASEPATH")) #caminho padrão do computador para acesso e manipulação das pastas e arquivos do projeto, criar e alterar o arquivo .env para conter o SIGAMA_BASEPATH(caminho)
IMAGE_BASEPATH = Path(os.getenv("IMAGES_FOLDER"))

#if not BASEPATH:
#    raise RuntimeError("BASEPATH não definido no .env")

if not IMAGE_BASEPATH:
    raise RuntimeError("IMAGE_BASEPATH não definido no .env")

IMAGE_DIR = IMAGE_BASEPATH

TIMEOUT = 60