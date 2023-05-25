# import re
# while True:
#       user = input('search for characters?')
#       text = 'wale'
#       if(re.search(user, text)):
#           print('found')
#       else:
#           print('not found')
# valid = re.search(user, text)

# print(valid)

# import re
# while True:
#     user = input('search for names?')
#     names = 'Bolade, hassan, shazam, chichi, Ren, Klein, Jake, qing, captain'
#     if(re.search(user, names)):
#         print('found')
#     else:
#         print('not found')    

import re
while True:
    user = input('What novel are you looking for?')
    Novels = "LOTM, Oracle's Path, Revered immortal, circle of inevitability, ORV, The author's Pov, swallowed star, mythological genes"
    if(re.search(user, Novels)):
        print(user)
    else:
        print('unavailable')   