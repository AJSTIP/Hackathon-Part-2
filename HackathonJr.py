#pip install pyttsx3
#pip install python-decouple

from distutils.command.config import config
from email import header
import imp
import requests
from bs4 import BeautifulSoup
import os
import smtplib
from datetime import datetime
import pyttsx3
from decouple import config

EMAIL_ADRESS=config('EMAIL_ADRESS')
EMAIL_PASS=config('EMAIL_PASS')


#region Web Scraper:
def runProgram(): 
    url = 'https://weather.com/weather/tenday/l/ca56f3612e83373c0833df5a107e37a43550a3d5fec6055758a8120409026b9d'

    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    }

    response=requests.get(url, headers=header)
    #print(response.content)

    soup = BeautifulSoup(response.content, 'lxml')

    test="\n"

    vlad = soup.select('.DetailsSummary--extendedData--365A_')[0].get_text()
    steve = soup.select('.DetailsSummary--extendedData--365A_')[2].get_text()
    gary = soup.select('.DetailsSummary--extendedData--365A_')[4].get_text()
    greg = soup.select('.DetailsSummary--extendedData--365A_')[6].get_text()
    larry = soup.select('.DetailsSummary--extendedData--365A_')[8].get_text()

    daddy = vlad + test + steve + test + gary + test + greg + test + larry

    print(daddy)

    if vlad or steve or gary or greg or larry == "AM Snow Showers" or vlad or steve or gary or greg or larry =="Rain/Snow" or vlad or steve or gary or greg or larry == "Windy" or vlad or steve or gary or greg or larry == "Freezing":
        SpeakText(userText)
#endregion



#region Email Code:
    now = datetime.now()
    current_time = now.strftime("%H:%M")


    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()


        smtp.login(EMAIL_ADRESS, EMAIL_PASS)

        subject=f'{current_time}: The next 5 day forecast is: ' 
        body= f'{daddy}'

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADRESS, 'apocalypticemergencyservices@gmail.com', msg)
        print("Sent!")

        
#endregion

#region Condition Alarm and Time
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
userText=f'Treacherous conditiions @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'

while True:
    now = datetime.now()
    timeNow = now.strftime("%H:%M:%S")
    if timeNow=="08:49:00":
        runProgram()
#endregion