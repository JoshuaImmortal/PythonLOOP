import requests
import json
data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
# print(data.json()['data'])
request = data.json()['data']
for req in request:
    nation = print(req["Nation"])
for req in request:
    nationID = print(req["ID Nation"])
for req in request:
    year = print(req["Year"])
for req in request:
    population = print(req["Population"])
# Table = open('api.html', 'w')
# Table.write(set)
# Table.close()