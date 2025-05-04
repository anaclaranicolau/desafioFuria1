# PANTERA BOT

Um bot do Telegram para torcedores da FURIA, com frases motivacionais, desabafos, perfis de jogadores e até quiz!

# Funcionalidades

- `/start` – Mensagem de boas-vindas
- `/menu` – Lista de comandos
- `/jogo` – Mostra o próximo jogo da FURIA
- `/fe` – Frase motivacional
- `/rage` – Desabafo de torcedor
- `/player <nome>` – Perfil de um jogador (art, kscerato, yuurih, drop, chelo)
- `/quiz` – Inicia um quiz sobre o time
- Mensagens comuns – Serve como resposta para o quiz

# Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/anaclaranicolau/desafioFuria1
   cd seu-repo

2. Crie um arquivo .env com seu token do bot:
    ```ini 
    BOT_TOKEN=seu_token_aqui

3. Instale as dependências:
    ```bash 
    pip install -r requirements.txt

4. Rode o bot:
    ```bash
    python nome_do_arquivo.py

# Requisitos 

1. Python 3.10+

2. python-telegram-bot

3. python-dotenv

# Estrutura
1. bot.py – Código principal do bot

2. .env – (ignorado pelo Git) armazena o token do bot

3. index.html - algumas informações do bot

4. README.md – Este arquivo