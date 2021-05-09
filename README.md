# Inferno-Webhook-Spammer

(FOR THOSE OF YOU WHO ARE CURIOUS, I will try to keep it as simple as possible)

This is a way to send repeated text messages from a discord webhook in a particular channel ( everyone ping as well :D) 
Discord's built in Webhooks function is an easy way to get automated messages and data updates sent to a text channel in your server.
You can basically send pictures and videos(through url), text messages(which include simple messages,user and role mention,everyone and here ping)

so basically all you need to know is the python language (and install "requests" module)

How do I install the requests module?
Simple just open your command prompt and type "pip install requests" (make sure to check the path positioning is done correctly and your pip install doesn't create any problem)


a basic webhook code goes like this :




import requests 

url= "enter your webhook url here" 

while True:
   message=input("Please enter your message: ")
   r= requests.post(url,data={'content'=message})
   
   
   
This also gets the job done but I have installed more modules and made the program interactive overall
It asks you to enter webhook url,image,name and then starts spamming.Please check it out :D
   
   
