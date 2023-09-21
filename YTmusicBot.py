import telebot

bot_token= "6411100264:AAEr7h8tychNYNLYE39GrJYga7o-Fyk_w9g"
bot= telebot.TeleBot( token=bot_token )
#step1
@bot.message_handler()
def initial_step(message):
    content = message.text.lower()
    answer = "Hey, what about some music?"
    
#register thread       
    thread = bot.reply_to(message, answer)
    bot.register_next_step_handler(thread, second_step)
    
#step2    
def second_step(message):
    content = message.text.lower()
#asking the user
    if content.find("yes") != -1:
        answer= "Great! \nHere are some of my favorite genres: \nJazz \nRock \nTechno"
        thread = bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, third_step)
#when the answer is no
    else:
        answer= "Alright, no problem."
        bot.reply_to(message, answer)
#step3
def third_step(message):
    content = message.text.lower()
    
    if content.find("jazz") != -1:
        answer= "Here is a good playlist: \nhttps://open.spotify.com/playlist/2sbK7BWceXbmYylfcMxgcp?si=2930859bd7a3494d"
    elif content.find("rock") != -1:
        answer= "Here is a good playlist: \nhttps://open.spotify.com/playlist/4u8IztgIYihUJKuHP6tPUM?si=47d11a847794423b"
    elif content.find("techno") != -1:
        answer= "Here is a good playlist: \nhttps://open.spotify.com/playlist/5WvvfyGqMUKV1mFQCDJP8P?si=4563545189a744d0"

        
    bot.reply_to(message, answer)
bot.polling()
