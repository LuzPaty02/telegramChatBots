
import telebot
import requests
bot_token = "6411100264:AAEr7h8tychNYNLYE39GrJYga7o-Fyk_w9g"
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(  )
def initial_step(message):
    content = message.text.lower()
    answer="text"

#lights    
    #lights on
    if content.find("lights")!= -1:
        if content.find("on")!= -1:
            light_on_url="http://128.199.15.106:8081/encenderLuz/A01637442"
            home_functions= requests.get(light_on_url).json()
            answer= "The lights are on"

        #lights off
        elif content.find("off")!= -1:
            light_off_url="http://128.199.15.106:8081/apagarLuz/A01637442"
            home_functions= requests.get(light_off_url).json()
            answer= "The lights are off"
#tv       
    elif content.find("tv")!= -1:
        #tv on
        if content.find("on")!= -1:
            tvOn_url="http://128.199.15.106:8081/encenderTV/A01637442"
            home_functions= requests.get(tvOn_url).json()
            answer= "The tv is on"

        #tv off
        elif content.find("off")!= -1:
            tvOff_url="http://128.199.15.106:8081/apagarTV/A01637442"
            home_functions= requests.get(tvOff_url).json()
            answer= "The tv is off"
    
#Hifi Tv
    elif content.find("hifi")!= -1:
        #Hifi Tv on
        if content.find("on"):
            hifiOn_url="http://128.199.15.106:8081/encenderHiFi/A01637442"
            home_functions= requests.get(hifiOn_url).json()
            answer= "The Hifi is on"
        #Hifi Tv off   
        elif content.find("off")!= -1:
            hifiOff_url="http://128.199.15.106:8081/apagarHiFi/A01637442"
            home_functions= requests.get(hifiOff_url).json()
            answer= "The Hifi is off"
            
#Youtube video
    elif content.find("youtube")!= -1:
            video_url="http://128.199.15.106:8081/reproducir/A01637442/youtubeID"
            home_functions= requests.get(video_url).json()
            answer= "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            
#change city
    elif content.find("city")!= -1:
        city_name= content.split(":")[1]
        url= "http://128.199.15.106:8081/clima/A01637442/"+city_name 
        weather_data= requests.get(url).json()
        answer= "The weather of"+ str(city_name) + "is"+ str(weather_data)
        
    bot.reply_to( message, answer )

bot.polling()