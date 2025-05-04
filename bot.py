from telegram import Update 
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random
import random

from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("BOT_TOKEN")
print(token)

# Dados de jogadores da FURIA (simples)
jogadores = {
    "art": {
        "nome": "Andrei 'arT' Piovezan",
        "função": "IGL / Entry Fragger",
        "destaque": "Conhecido por seu estilo ultra agressivo.",
    },
    "kscerato": {
        "nome": "Kaike 'KSCERATO' Cerato",
        "função": "Rifler",
        "destaque": "Consistente, clutch god e um dos melhores do BR.",
    },
    "yuurih": {
        "nome": "Yuri 'yuurih' Santos",
        "função": "Rifler",
        "destaque": "Parça de longa data do KSCERATO, sempre sólido.",
    },
    "drop": {
        "nome": "André 'drop' Abreu",
        "função": "Support",
        "destaque": "Papel sujo, mas essencial.",
    },
    "chelo": {
        "nome": "Marcelo 'chelo' Cespedes",
        "função": "Lurker / Rifler",
        "destaque": "Energia pura, vibes positivas e bala na cabeça.",
    }
}

# Frases
frases_fe = [
    "Confia no arT, ele sabe o que faz!",
    "Hoje é dia de highlight ou rage, mas tamo junto!",
    "A FURIA não joga, ela dá show!",
    "Se tem um time que nunca desiste, é a FURIA!"
]

frases_rage = [
    "POR QUE FORAM DE RUSH B DE NOVO???",
    "Pelo amor de deus, compra um colete!",
    "Esse eco era nosso!",
    "QUE CALL FOI ESSA MEU DEUS"
]

# Perguntas do quiz
quiz_perguntas = [
    {
        "pergunta": "Quem é o IGL da FURIA?",
        "resposta": "art"
    },
    {
        "pergunta": "Qual jogador é conhecido por ser o 'clutch god' da FURIA?",
        "resposta": "kscerato"
    },
    {
        "pergunta": "Quem é o parceiro de longa data do yuurih?",
        "resposta": "kscerato"
    },
    {
        "pergunta": "Qual jogador da FURIA é conhecido pela vibe positiva?",
        "resposta": "chelo"
    }
]

# Comandos do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, FURIOSO! Digita /menu pra ver os comandos!")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "Comandos disponíveis:\n"
        "/jogo - Ver o próximo jogo\n"
        "/fe -  Frase motivacional\n"
        "/rage - Desabafo de torcedor\n"
        "/player <nome> - Perfil de um jogador\n"
        "/quiz - Começar um quiz da FURIA"
    )
    await update.message.reply_text(texto)

async def jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Próximo jogo: FURIA vs. NAVI - 25/04 às 15h (BO3)")

async def fe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(frases_fe))

async def rage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(frases_rage))

async def player(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    if not args:
        await update.message.reply_text("Digite o nome de um jogador. Ex: /player art")
        return
    nome = args[0].lower()
    if nome in jogadores:
        j = jogadores[nome]
        texto = f"{j['nome']}\nFunção: {j['função']}\nDestaque: {j['destaque']}"
    else:
        texto = "Jogador não encontrado. Tenta: art, kscerato, yuurih, drop, chelo"
    await update.message.reply_text(texto)

# Quiz simples
quiz_ativa = {}

async def quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = random.choice(quiz_perguntas)
    quiz_ativa[update.effective_chat.id] = pergunta["resposta"]
    await update.message.reply_text(pergunta["pergunta"])

async def resposta_quiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id in quiz_ativa:
        resposta_correta = quiz_ativa[chat_id].lower()
        resposta_user = update.message.text.strip().lower()
        if resposta_user == resposta_correta:
            await update.message.reply_text("Acertou, miserávi!")
        else:
            await update.message.reply_text(f"Errou! A resposta era: {resposta_correta}")
        del quiz_ativa[chat_id]

# Inicia o bot
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("jogo", jogo))
app.add_handler(CommandHandler("fe", fe))
app.add_handler(CommandHandler("rage", rage))
app.add_handler(CommandHandler("player", player))
app.add_handler(CommandHandler("quiz", quiz))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), resposta_quiz))

print("PanteraBot rodando!")
app.run_polling()












