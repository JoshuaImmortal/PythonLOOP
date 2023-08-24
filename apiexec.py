import mysql.connector
import requests
import json
# http://universities.hipolabs.com/search?country=United+States (end point for get request)
apidata = requests.get("http://universities.hipolabs.com/search?country=United+States")
data = apidata.json()
if(data):
    country = ""
    domain = ""
    alpha = ""
    state = ""
    web = ""
    name =""
    for darts in data:
        country = darts["country"]    
        domain = darts["domains"]
        alpha = darts["alpha_two_code"]
        state = darts["state-province"]
        web = darts["web_pages"]
        name = darts["name"]
insert = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'university_db',
)
insertion = insert.cursor()
if(insertion):
    for darts in data:
        insert_query = f"""INSERT INTO `api_data` VALUES(%s, %s, %s, %s, %s, %s);"""
        values = (darts["country"], "".join(darts["domains"]), darts["alpha_two_code"], darts["state-province"], "".join(darts["web_pages"]), darts["name"])    
        insertion.execute(insert_query, values)
        insert.commit()
        