# Number 1
# import re
# student_portifolio = "John is a syudent of cyclobold and his matric number is M123d but he often says that he is 'the scholar of our time?'"
# checks = re.findall("\w" "+" "\d", student_portifolio)
# space = re.findall("\s", student_portifolio)
# if checks:
#     print('found', checks)
# if space:
#     print('found', space)

# Number 2
# import re
# string = 'Rendover '
# match = re.sub("\s", "_23", string)
# print(match)

# Number 3
# import re
# stingify = "pablo, escobar01, rene, shallipopi, seyivibez23, asake, verizon202"
# matching = re.findall("\w" "+" "\d", stingify)
# print(matching)

# Number 4+
# import re
# sentence = "I am John, the name of my tech academy is Cyclobold"
# space = re.findall("\s", sentence)
# substituting = re.sub(",", " and", sentence)
# print(space)
# print(substituting)

# Number 5
# import re
# words = "'eleniyan', 'tofunmi', 'agbero', 'semi', 'akande', 'gbogunmi'"
# begin = re.search("^(a|e)+\.+[a-z]", words)
# print(begin)

# Number 6
# import re 
# emails = input("Your email: ")
# validate = re.findall("^[a-z]+@+(gmail|yahoomail)+\.+(com|net|org|edu)$", emails)
# print(validate)
# if validate:
#     print("registration successfull")
# else:
#     print('wrong input')

# Number 7
# import re
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('p')
# test = str(para)
# print(test)
# validation = "movies, form"
# validating = re.findall("movies" "form" "\s" "\d", test)
# if validating:
#     print("successful")
# else:
    # raise TypeError("unsuccessful")

# Number 8
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('p')
# test = str(para)
# pdf = open("exec.pdf", "w")
# pdf.write(test)
# pdf.close()

# Number 9
# import webbrowser
# import requests
# from bs4 import BeautifulSoup
# r = requests.get("https://cyclobold.com/")
# data = BeautifulSoup(r.content, 'html.parser')
# order = data.prettify()
# para = data.find_all('img')
# test = str(para)
# img = open("imgg.html", "w")
# img.write(test)
# img.close()
# webbrowser.open("imgg.html")