
import telebot

bot_token = "6411100264:AAEr7h8tychNYNLYE39GrJYga7o-Fyk_w9g" 
bot = telebot.TeleBot(token=bot_token)
cart= []
price= 0
@bot.message_handler(  )

def welcome_step(message): #pregunta si quiere ver el menu o el cart
     content = message.text.lower()
     answer = "Welcome to PaKai, would you like to see the menu or the cart?"
     thread= bot.reply_to(message, answer)
     bot.register_next_step_handler(thread, second_step)
     
def second_step(message): #despliega el menu y registra la opción del usuario
    global price
    content = message.text.lower()
    if content=="menu": #envia a menu
        answer= "Our menu is:\nTacos $54\nSushi $42\nSpaguetti $77\nWhich one would you like? "
        thread=bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, order_step)
    elif content=="cart":
         answer= "The total is $"+ str(price) +"\nTo buy the items in your order go to pay"
         thread= bot.reply_to(message, answer)
         bot.register_next_step_handler(thread, pay_step)
    else: #en caso de error en el input, vuelve a presentar la pregunta
        answer= "I'm sorry I don't understand\nThe options are:\nMenu\nCart"
        thread=bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, second_step)
        
def order_step(message):            
    global price
    content = message.text.lower()
    if content == "tacos" or content == "sushi" or content== "spaguetti":
        cart.append(content)
        if content == "tacos":
            price= price + 54
        elif content == "sushi":
            price= price + 42
        elif content=="spaguetti":
            price= price + 77
        answer= "Got it! "+ content +" it's been added to the list\nOptions:\nMenu\nCart"
        thread=bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, second_step)    
    else:
        answer= "Invalid entry\nChoose one of following options:\nTacos\nSushi\nSpaguetti"
        thread=bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, order_step)
        
def pay_step(message): 
    content = message.text.lower()
    answer= ""
    if content=="pay":
        answer="Your total to pay is $"+ str(price)+ " pesos\n"      
        for element in cart:
            answer= answer + element + "\n"
        answer= answer + "\n Thanks for buying with us :)"
        bot.reply_to(message, answer)
    else:
        answer="Invalid entry"
        thread=bot.reply_to(message, answer)
        bot.register_next_step_handler(thread, pay_step)
bot.polling()