# Forms-vote-bot

O Forms Vote Bot é um projeto em Python voltado para automatizar a votação de uma competição com Google Forms por meio do pyautogui. Controlando mouse, teclado e rolagem de tela, permitindo abrir formulários, localizar opções específicas a partir de imagens, selecionar respostas e submeter o formulário automaticamente.

Este projeto tem caráter educacional e experimental. É utilizado apenas para fins de estudo.

---

## Visão geral do projeto

O pipeline consiste em abrir um Google Forms em uma aba do navegador, aguardar o carregamento da página, localizar a opção desejada com base em uma imagem previamente capturada, clicar na caixinha correspondente, rolar a página até o final e acionar o botão de envio.

---

## Requisitos de ambiente

### Sistema

* Windows 10 ou 11
* Google Chrome ou Microsoft Edge
* Resolução de tela estável
* Zoom do navegador em 100%
* Escala do Windows preferencialmente em 100%

### Software

* Anaconda ou Miniconda
* Python 3.10 ou superior
* Git

---

## Dependências Python

Principais bibliotecas utilizadas:

* pyautogui
* opencv-python
* python-dotenv
* pyperclip

---

## Criação do ambiente Conda

Crie um ambiente dedicado ao projeto:

```bash
conda create -n Forms-vote-bot python=3.11 -y
conda activate Forms-vote-bot
```

Atualize o pip e instale as dependências:

```bash
python -m pip install --upgrade pip
pip install -e .
pip install pyautogui opencv-python python-dotenv pyperclip
```

---

## Estrutura do repositório

```text
Forms-vote-bot/
├── README.md
├── keys.env
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── environment.yaml
└── src/
    └── Forms-vote-bot/
        │   __init__.py
        ├── runner.py
        ├── utils/
        │   ├── __init__.py
        │   ├── automator.py
        │   ├── position.py
        │   └── validate.py
        ├── config/
        │   ├── __init__.py
        │   └── settings.py
        └── images/
            ├── checkbox.png
            └── submit.png
```

---

## Configuração obrigatória (keys.env)

É necessário criar um arquivo `keys.env` na raiz do projeto.

Também é necessário entrar em "runner.py" e adicionar a URL do seu formulário.

### Exemplo de `keys.env`

```env
IMAGE_FOLDER=C:\Users\seu_usuario\Documents\Github\Forms-vote-bot\src\Forms-vote-bot\images
```

Observações importantes:

* Utilize caminho absoluto
* O caminho deve apontar exatamente para a pasta `images`
* Não utilize aspas
* Não versionar esse arquivo (inclua no `.gitignore`)

---

## Pasta images

A pasta `images` deve conter capturas de tela dos elementos que a automação irá localizar.

Exemplos:

* `checkbox.png`: imagem da opção (título ou miniatura)
* `submit.png`: botão Enviar

Boas práticas para as imagens:

* Recortar somente o elemento necessário
* Evitar grandes áreas de fundo
* Salvar em formato PNG
* Capturar com o navegador em 100% de zoom

---

## Execução

Ative o ambiente Conda:

```bash
conda activate Forms-vote-bot
```

Execute o script principal:

```bash
python src/Forms-vote-bot/runner.py
```

Durante a execução:

* Não mova o mouse
* Não altere o foco da tela
* Para interromper rapidamente, mova o mouse para o canto superior esquerdo (failsafe do PyAutoGUI)

---

## Limitações conhecidas

* Dependência de resolução e zoom fixos
* Pode falhar caso o layout do Google Forms seja alterado
* Conexão instável(A ser resolvido)

---

## Autor

Enzo Maldinni

---
