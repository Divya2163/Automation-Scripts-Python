import requests 

#web scraping library 
from  bs4 import BeautifulSoup
#smtp connection to send emails 
import smtplib

#creating email and managing the content of it 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#system date and time manipulation 
import datetime
now = datetime.datetime.now()

content =''

#Using beautiful soup to extract the headlines from the website and create the content of the email of the body 
def extract_news(url):
    print('Extracting your date....')
    cnt=''
    cnt+=('<b>Top stock picks from moneycontrol today:</b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('div',attrs={'class':'item company All'})):
        cnt += ((str(i+1)+' :: '+ '<a href="' + tag.a.get('href') + '">' + tag.text + '</a>' + "\n" + '<br>'))
    return(cnt)
  
cnt = extract_news('https://www.moneycontrol.com/news/')
content +=cnt
content += ('<br>---------------------<br>')
content += ('<br><br>End of Message')

#Sending the email and authentication 
print('Composing Email...')

#Creating the server parameters 
Server = 'smtp.gmail.com'
Port = 587
From = 'divyamohan210603@gmail.com'
To = 'divyamohan6597@gmail.com'
Appass = 'chxm yogh rdqz zsgr'

msg = MIMEMultipart()
msg['Subject'] ='Top Stock picks from Moneycontrol [Automated Email]'+''+str(now.day)+'-'+str(now.month)+'-'+str(now.year)
msg['From']=From
msg['To']=To

msg.attach(MIMEText(content,'html'))

print('Initializing Server...')

#Server authentication 
server = smtplib.SMTP(Server,Port)
server.set_debuglevel(1)
server.ehlo
server.starttls()
server.login(From,Appass)
server.sendmail(From,To,msg.as_string())

print('Email Sent...')

server.quit()