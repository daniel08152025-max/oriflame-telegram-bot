import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Tokenul tău de la BotFather
TOKEN = "7553659026:AAHSlr_P3IbhG9KWMgEaurNSKgui0dwEjnk"

# Configurarea logging-ului
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()


# Funcția care răspunde la mesajul de bun venit
async def start(update: Update, context: CallbackContext):
    logging.info("Comanda /start a fost primită.")
    await update.message.reply_text(
        "Bine ați venit! Numele meu este Diana. Obțineți o reducere de bun venit de 15% la prima comandă.\n"
        "Pentru a plasa comanda, accesați acest link: "
        "https://shop.oriflame.com/MD-2452422044/Ust3Xho6\n"
        "Cum te pot ajuta mai departe? Îți pot oferi informații despre:\n"
        "- VIP Client Oriflame\n"
        "- Brand Partener Oriflame\n"
        "Dacă dorești să afli mai multe despre una dintre aceste opțiuni, apasă pe cuvintele corespunzătoare.\n"
        "\n"
        "Dacă ai nevoie de ajutor pentru înregistrare sau vrei să faci prima comandă cu reducerea de 15%, scrie-mi pe:\n"
        "- Messenger\n"
        "- Viber\n"
        "- Telegram\n"
        "- WhatsApp\n"
        "Sau mă poți contacta la numărul de telefon: +37360705161\n"
        "Aștept mesajul tău! 😊\n"

        # Mesajul în rusă
        "\n"
        "Добро пожаловать! Меня зовут Диана. Получите 15% скидку на ваш первый заказ.\n"
        "Для того чтобы разместить заказ, перейдите по следующей ссылке: "
        "https://shop.oriflame.com/MD-2452422044/Ust3Xho6\n"
        "Чем я могу помочь? Я могу предоставить информацию о:\n"
        "- VIP клиент Oriflame\n"
        "- Бренд Партнер Oriflame\n"
        "Если вы хотите узнать больше об этих опциях, нажмите на соответствующие слова.\n"
        "\n"
        "Если вам нужно помочь с регистрацией или вы хотите сделать первый заказ со скидкой 15%, напишите мне в:\n"
        "- Messenger\n"
        "- Viber\n"
        "- Telegram\n"
        "- WhatsApp\n"
        "Также вы можете связаться со мной по телефону: +37360705161\n"
        "Жду вашего сообщения! 😊"
    )


# Funcția care răspunde la întrebările despre VIP client
async def vip_client(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "VIP client Oriflame este un statut exclusiv care îți oferă reduceri suplimentare, "
        "oferta de produse premium și multe altele.\n"
        "Pentru a deveni VIP Client, apasă pe link-ul de mai jos și urmează pașii:\n"
        "[Devino VIP Client Oriflame](https://shop.oriflame.com/MD-2452422044/U6CCLzSr)\n"
        "Dacă ai întrebări suplimentare, nu ezita să întrebi!\n"

        # Mesajul în rusă
        "\n"
        "VIP клиент Oriflame — это эксклюзивный статус, который дает вам дополнительные скидки, "
        "предложения по премиум-продуктам и многое другое.\n"
        "Чтобы стать VIP клиентом, нажмите на ссылку ниже и следуйте инструкциям:\n"
        "[Станьте VIP клиентом Oriflame](https://shop.oriflame.com/MD-2452422044/U6CCLzSr)\n"
        "Если у вас есть дополнительные вопросы, не стесняйтесь спрашивать!"
    )


# Funcția care răspunde la întrebările despre Brand Partener
async def brand_partener(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Oportunitatea Brand Partenerului Oriflame îți permite să câștigi comisioane și să îți construiești un business propriu.\n"
        "Pentru a deveni Brand Partener, apasă pe link-ul de mai jos și înregistrează-te:\n"
        "[Devino Brand Partener Oriflame](https://md.oriflame.com/business-opportunity?sc_device=mobileapp&store=MD-2452422044)\n"
        "Dacă ai întrebări suplimentare, te pot ajuta!\n"

        # Mesajul în rusă
        "\n"
        "Возможности для Бренд Партнера Oriflame позволяют вам зарабатывать комиссионные и строить свой бизнес.\n"
        "Чтобы стать Бренд Партнером, нажмите на ссылку ниже и зарегистрируйтесь:\n"
        "[Станьте Бренд Партнером Oriflame](https://md.oriflame.com/business-opportunity?sc_device=mobileapp&store=MD-2452422044)\n"
        "Если у вас есть дополнительные вопросы, я с радостью помогу!"
    )


# Funcția care gestionează mesajele primite de la utilizatori
async def handle_message(update: Update, context: CallbackContext):
    logging.info(f"Mesaj primit: {update.message.text}")
    text = update.message.text.lower()

    if "vip client" in text:
        await vip_client(update, context)
    elif "brand partener" in text:
        await brand_partener(update, context)
    else:
        await update.message.reply_text("Îmi pare rău, nu înțeleg întrebarea. "
                                        "Poți întreba despre:\n"
                                        "1. VIP Client Oriflame\n"
                                        "2. Brand Partener Oriflame\n"
                                        "Dacă ai alte întrebări, sunt aici să te ajut!\n"

                                        # Mesajul în rusă
                                        "\n"
                                        "Извините, я не понимаю ваш вопрос. Вы можете спросить о:\n"
                                        "1. VIP клиент Oriflame\n"
                                        "2. Бренд Партнер Oriflame\n"
                                        "Если у вас есть другие вопросы, я всегда готов помочь!")


def main():
    # Configurarea aplicației Telegram
    application = Application.builder().token(TOKEN).build()

    # Setează handler-ul pentru comanda /start
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Setează un handler pentru mesajele primite
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Rulează botul
    application.run_polling()


if __name__ == "__main__":
    main()
