import requests
import json
apiclass = requests.get("https://api.publicapis.org/entries")
apijot = apiclass.json()["entries"]
# verify = []
verit = []
# lister = ""
for jots in apijot:
    # aps = jots["Category"]
    apt = jots["API"]
    # verify.append(aps)
    verit.append(apt)
    # lister += aps
    # print(apt)
listeth = " ".join(verit)
print(listeth)
# lister = " ".join(verify)
# print(listeth)
# print(lister, listeth)
# appap = open("deapi.csv", "w")
# appap.write(lister)
# appap.close()

apap = open("ferrous.txt", "w")
apap.write(listeth)
apap.close()