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
    print("Extracting Headlines from Noteboookcheck...")
    strs = ""
    strs += ('<b>HN Top Stories:</b>' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser') # parse html in content and store in soup
    for i,tag in enumerate(soup.find_all('td',attrs={'class':"title",'valign':''})): 
        res = "{} :: <h3>{}</h3> \n <br>".format(i+1,tag.text) if tag.text != 'More' else ''
        strs += res
    return strs

cnt = extract('https://news.ycombinator.com/')
content += cnt
content += ('<br>---------<br>')
content += ('<br><br>End Of Message')
# print(content,now) Data scrapped successfully

#Email Automation
print('Composing Email')
SERVER = 'smtp-mail.outlook.com'
PORT = 587
FROM = '1901330100158@niet.co.in'
TO = 'mohdathar1991@gmail.com'
PASS = 'K@whiL3onard'





