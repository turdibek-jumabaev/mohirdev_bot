def start(ism, html=True, MarkdownV2=False):
    if html:
        return f"<b>Assalom alaykum {ism}!</b>\n\n" \
            "Mohirdev.uz - onalyn ta'lim platformasining norasmiy Telegram Botiga xush kelibsiz.\n" \
            "Bot yordamida siz, kurslar haqidagi malumotlarga oson ega bo'lasiz.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."
    elif MarkdownV2:
        return f"**Assalom alaykum {ism}!**\n\n" \
            "Mohirdev.uz - onalyn ta'lim platformasining norasmiy Telegram Botiga xush kelibsiz.\n" \
            "Bot yordamida siz, kurslar haqidagi malumotlarga oson ega bo'lasiz.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."
    else:
        return f"Assalom alaykum {ism}!\n\n" \
            "Mohirdev.uz - onalyn ta'lim platformasining norasmiy Telegram Botiga xush kelibsiz.\n" \
            "Bot yordamida siz, kurslar haqidagi malumotlarga oson ega bo'lasiz.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."


def help(html=True, MarkdownV2=False):
    if html:
        return f"<b>Botdan foydalanish!</b>\n\n" \
            "/start - yordamida botni qayta ishga tushuring.\n" \
            "O'zingizga kerakli bo'limni tanlang.\n" \
            "Kurslar haqidagi malumotlarga oson ega bo'ling.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."
    elif MarkdownV2:
        return f"**Botdan foydalanish!**\n\n" \
            "/start - yordamida botni qayta ishga tushuring.\n" \
            "O'zingizga kerakli bo'limni tanlang.\n" \
            "Kurslar haqidagi malumotlarga oson ega bo'ling.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."

    else:
        return f"Botdan foydalanish!\n\n" \
            "/start - yordamida botni qayta ishga tushuring.\n" \
            "O'zingizga kerakli bo'limni tanlang.\n" \
            "Kurslar haqidagi malumotlarga oson ega bo'ling.\n" \
            "Marhamat, o'zingizni qiziqtirgan katigoriyani tanlang."