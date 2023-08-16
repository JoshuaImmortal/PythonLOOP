import requests
from bs4 import BeautifulSoup

# r = requests.get("https://cyclobold.com/")
# soup = BeautifulSoup(r.content, "html.parser")
# data = soup.prettify()
# content = soup.find(class_= 'modal-content')
# print(content.text)
# scrape = open('scrape.pdf', 'w')
# scrape.write(content.text)
# scrape.close()


# r = requests.get("https://cyclobold.com/")
# soup = BeautifulSoup(r.content, "html.parser")
# data = soup.prettify()
# image = soup.find(class_ = 'col-md-6 col-lg-3 mb-4')
# print(image.text)
# images = open('image.html', 'w')
# images.write(image.text)
# images.close()

import requests
from bs4 import BeautifulSoup

import mysql.connector

db_con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "management_db"
)
cursor = db_con.cursor()
r = requests.get("https://cyclobold.com/")
data = BeautifulSoup(r.content, "html.parser")
soup = data.prettify()
ps = data.find_all('p')
text = ""
num = 8
for p in ps:
    text = p.text
if cursor:
    mysql_insert_query = f"""
                INSERT INTO `content` VALUES (%s, %s);
"""
    record = (num, text)
    cursor.execute(mysql_insert_query, record)
    db_con.commit()
    print(text)






