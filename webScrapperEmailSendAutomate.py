import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import bs4
from bs4 import BeautifulSoup

now = datetime.now()
content = ''

def extract(url):
    print("Extracting Headlines...")
    strs = ""
    strs += ('<b>HN Top Stories:</b>' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser') # parse html in content and store in soup
    for i,tag in enumerate(soup.find_all('td',attrs={'class':"title",'valign':''})): 
        res = "{} :: {} \n <br>".format(i+1,tag.text) if tag.text != 'More' else ''
        strs += res
    return strs

cnt = extract('https://news.ycombinator.com/')
content += cnt
content += ('<br>---------<br>')
content += ('<br><br>End Of Message')

#Email Automation
print('Composing Email')
SERVER = 'smtp-mail.outlook.com'
PORT = 587
FROM = 'userEmail@domain.com'
TO = 'receiverMail@domain.com'
PASS = 'UserPassword'

msg = MIMEMultipart()

msg['Subject'] = "[Automated Mail] Top stories from HN" + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content,'html')) # email payload done

print("Initiating Server...")

server = smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print("Email Sent")

server.quit()


