import requests
from bs4 import BeautifulSoup
import time
import datetime
import os
import smtplib, ssl
import getpass

sender_email = "username@email.com"
password = "password"

smtp_server = "smtp.gmail.com"

mess = """\
Subject: BOT alert started for AVENGERS:ENDGAME!

Polling BMS every 15seconds for updates until Avenger endgame is available :D.
This message is sent from Python."""


message = """\
Subject: Hi there,  {mov} booking available now!!

The wait is finally over.
This bot will rest now.
This message is sent from Python."""


port = 465  # For SSL


# Create a secure SSL context
context = ssl.create_default_context()

rc = open(os.path.join(os.getcwd(),"reciever.txt"),"r")
reciever_email = rc.readlines()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email,reciever_email,mess)


Sleep = 15 # make this random

with open("log.file","w+")as fp:
    while True:
        rc = open("reciever.txt","r")
        reciever_email = rc.readlines()
        print(reciever_email)

        r = requests.get("https://in.bookmyshow.com/bengaluru/movies/")
        # no_email = len(get_list_or_404(Email))
        bs = BeautifulSoup(r.content,'html.parser')
        tags = bs.find_all('div','listing-section')
        current_movies = []
        img_movies = []
        for i in tags:
            current_movies.extend(i.find_all('h4'))
        # for i in tags:
        #     img_movies.extend(i.find_all('img','__poster __animated'))

        movies = [i.string for i in current_movies if 'avengers' in i.string.lower() or 'endgame' in i.string.lower()]
        # img_movies = [i['data-src'] for i in img_movies if 'avengers' in i['data-src']or 'endgame' in i['data-src']]
        # zipped_data = zip(movies,img_movies)
        format_st = "Date:{dt} | Connection-status:{ct} | Endgame available: {isit}"
        # print(zipped_data) 
        to_print = format_st.format(dt = datetime.datetime.now(),ct = r.status_code, isit = movies)
        print(to_print)
        fp.write(to_print+"\n")
        if(len(movies)!=0 ):
            print("Email sent!!")
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                message+=str(movies)
                for remail in reciever_email:
                    server.sendmail(sender_email,remail,message.format(mov=str(movies)))
            exit(0)
        time.sleep(Sleep)
