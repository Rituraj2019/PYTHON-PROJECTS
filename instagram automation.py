
#retest

from instabot import Bot #importing Bot class from instabot package
bot=Bot()
bot.login(username="pythonklie", password= "pythonproj")
bot.upload_photo("Nilaroom.jpg", caption="ha bhai pyhton se kiya hai")