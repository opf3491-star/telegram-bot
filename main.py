import os
import subprocess
import sys

# লাইব্রেরি ইনস্টল নিশ্চিত করা
try:
    import telebot
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyTelegramBotAPI"])
    import telebot

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# আপনার টেলিগ্রাম বট টোকেন
TOKEN = "9205388478:AAGH_F_-C93shIUUkoyr-SaqgH0nQWfagGM"

# আপনার টেলিগ্রাম অ্যাডমিন ইউজার আইডি বা চ্যাট আইডি (যেখানে বট সরাসরি নোটিফিকেশন পাঠাবে)
ADMIN_CHAT_ID = "@Rifat_ex"

SUPPORT_GROUP = "https://t.me/+LtkLNdQ7UB5jZTQ1"

bot = telebot.TeleBot(TOKEN)
user_languages = {}
user_waiting_for_lang = set()

# লেটেস্ট আপডেটেড এপিকে ডেটাবেজ (পুরোনো ফাইল বা লিংক স্বয়ংক্রিয়ভাবে ওভাররাইড/আপডেট হবে)
app_database = {
    "facebook": {
        "link": "https://example.com/facebook-v2.apk", 
        "version": "v2.0 (Latest)",
        "updated": True
    },
    "whatsapp": {
        "link": "https://example.com/whatsapp-v3.apk", 
        "version": "v3.1 (Latest)",
        "updated": True
    },
    "telegram": {
        "link": "https://example.com/telegram-v5.apk", 
        "version": "v5.0 (Latest)",
        "updated": True
    },
    "gemini": {
        "link": "https://example.com/gemini-v2.apk", 
        "version": "v2.0 (Latest)",
        "updated": True
    }
}

texts = {
    "bn": {
        "lang_set": "✨ ভাষা সফলভাবে সেট করা হয়েছে। এখন আপনার প্রয়োজনীয় অ্যাপটির নাম লিখুন বা পাঠান।",
        "not_found": "⚠️ দুঃখিত! এই অ্যাপটি বর্তমানে আমাদের সংগ্রহে নেই।",
        "not_updated_note": "ℹ️ নোট: এই অ্যাপটি এখনো লেটেস্ট ভার্সনে আপডেট করা হয়নি (Not Updated)।",
        "support_btn": "💬 সাপোর্ট গ্রুপে যোগ দিন"
    },
    "hi": {
        "lang_set": "✨ भाषा सफलतापूर्वक सेट हो गई है। अब अपने ऐप का नाम भेजें।",
        "not_found": "⚠️ क्षमा करें! यह ऐप वर्तमान में उपलब्ध नहीं है।",
        "not_updated_note": "ℹ️ नोट: यह ऐप अभी अपडेट नहीं किया गया है।",
        "support_btn": "💬 सहायता समूह से जुड़ें"
    },
    "ur": {
        "lang_set": "✨ زبان کامیابی سے سیٹ ہو گئی ہے۔ اب اپنی مطلوبہ ایپ کا نام بھیجیں۔",
        "not_found": "⚠️ معذرت! یہ ایپ فی الحال دستیاب نہیں ہے۔",
        "not_updated_note": "ℹ️ نوٹ: یہ ایپ ابھی اپ ڈیٹ نہیں کی گئی۔",
        "support_btn": "💬 سپورٹ گروپ میں شامل ہوں"
    },
    "ar": {
        "lang_set": "✨ تم تعيين اللغة بنجاح. الآن أرسل اسم التطبيق الذي تحتاجه.",
        "not_found": "⚠️ عذراً! هذا التطبيق غير متوفر حالياً.",
        "not_updated_note": "ℹ️ ملاحظة: هذا التطبيق غير محدث حالياً.",
        "support_btn": "💬 انضم إلى مجموعة الدعم"
    },
    "ne": {
        "lang_set": "✨ भाषा सफलतापूर्वक भयो। अब आफ्नो एपको नाम पठाउनुहोस्।",
        "not_found": "⚠️ माफ गर्नुहोला! यो एप हाल उपलब्ध छैन।",
        "not_updated_note": "ℹ️ नोट: यो एप अद्यावधिक गरिएको छैन।",
        "support_btn": "💬 समर्थन समूहमा सामेल हुनुहोस्"
    },
    "en": {
        "lang_set": "✨ Language selected successfully. Now send your app name.",
        "not_found": "⚠️ Sorry! This app is currently not available.",
        "not_updated_note": "ℹ️ Note: This app is not updated to the latest version yet.",
        "support_btn": "💬 Join Support Group"
    }
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🇧🇩 বাংলা", callback_data="lang_bn"),
        InlineKeyboardButton("🇮🇳 हिन्दी", callback_data="lang_hi"),
        InlineKeyboardButton("🇵🇰 اردو", callback_data="lang_ur"),
        InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar"),
        InlineKeyboardButton("🇳🇵 नेपाली", callback_data="lang_ne"),
        InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        InlineKeyboardButton("➕ অন্য ভাষা (Other Language)", callback_data="lang_custom")
    )
    welcome_msg = (
        "╭───────────────────╮\n"
        "│   **iOS 17 App Store**  │\n"
        "│  ✨ *Fast & Secure APK*  │\n"
        "╰───────────────────╯\n\n"
        "🌐 Please select your language / ভাষা নির্বাচন করুন:"
    )
    bot.send_message(message.chat.id, welcome_msg, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('lang_'))
def set_language(call):
    chat_id = call.message.chat.id
    lang_code = call.data.split('_')[1]
    
    if lang_code == "custom":
        user_waiting_for_lang.add(chat_id)
        bot.answer_callback_query(call.id, "Please type your preferred language.")
        bot.edit_message_text(
            "✍️ অনুগ্রহ করে আপনার পছন্দের ভাষাটির নাম লিখে পাঠান (যেমন: French, Spanish ইত্যাদি):", 
            chat_id, 
            call.message.message_id
        )
        return

    user_languages[chat_id] = lang_code
    selected_text = texts[lang_code]["lang_set"]
    bot.answer_callback_query(call.id, "✨ Premium Language Updated!")
    bot.edit_message_text(selected_text, chat_id, call.message.message_id)
    
    try:
        user_info = f"👤 ইউজার: @{call.from_user.username} (ID: {chat_id})\n🌐 সিলেক্ট করা ভাষা: {lang_code.upper()}"
        bot.send_message(ADMIN_CHAT_ID, f"🔔 **নতুন ভাষা নোটিফিকেশন:**\n\n{user_info}", parse_mode="Markdown")
    except Exception as e:
        print("Admin notify error:", e)

@bot.message_handler(func=lambda message: True)
def handle_app_search(message):
    chat_id = message.chat.id
    user_text = message.text.strip()
    
    if chat_id in user_waiting_for_lang:
        user_waiting_for_lang.remove(chat_id)
        user_languages[chat_id] = "en"
        
        bot.reply_to(message, "✅ আপনার ভাষা রিকোয়েস্টটি সেভ করা হয়েছে। খুব শীঘ্রই এটি অ্যাড করা হবে। এখন আপনার প্রয়োজনীয় অ্যাপের নাম লিখুন:")
        
        try:
            admin_msg = (
                f"🚨 **নতুন ভাষা রিকোয়েস্ট (New Language Request):**\n\n"
                f"👤 ইউজার: @{message.from_user.username} (ID: {chat_id})\n"
                f"🗣️ ইউজার যে ভাষায় কথা বলতে চায়: *{user_text}*"
            )
            bot.send_message(ADMIN_CHAT_ID, admin_msg, parse_mode="Markdown")
        except Exception as e:
            print("Custom lang notify error:", e)
        return

    user_lang = user_languages.get(chat_id, "en")
    app_name = user_text.lower().strip()

    if app_name in app_database:
        app_info = app_database[app_name]
        apk_link = app_info["link"]
        version = app_info["version"]
        is_updated = app_info["updated"]
        
        status_note = ""
        if not is_updated:
            status_note = f"\n{texts[user_lang]['not_updated_note']}"

        success_msg = (
            f"╭───────────────────╮\n"
            f"│  📱 **App Found! (Latest)** │\n"
            f"╰───────────────────╯\n"
            f"📦 **Name:** {app_name.capitalize()}\n"
            f"🔄 **Version:** {version}{status_note}\n"
            f"🔗 **Download Link:** {apk_link}"
        )
        bot.send_message(chat_id, success_msg, parse_mode="Markdown")
    else:
        msg_text = texts[user_lang]["not_found"]
        btn_text = texts[user_lang]["support_btn"]
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(btn_text, url=SUPPORT_GROUP))
        bot.send_message(chat_id, f"{msg_text}\nদয়া করে আমাদের প্রিমিয়াম সাপোর্ট গ্রুপে জয়েন করুন:", reply_markup=markup)
        
        try:
            bot.send_message(ADMIN_CHAT_ID, f"⚠️ **অপরিচিত অ্যাপ সার্চ রিকোয়েস্ট:**\nইউজার @{message.from_user.username} খুঁজেছে: `{app_name}`", parse_mode="Markdown")
        except Exception as e:
            print("Missing app notify error:", e)

print("Bot with Admin Notifications & Auto-Update APK is running...")
bot.infinity_polling()
