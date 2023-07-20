Profile = {}
for x in range(5):
    username = input('Your username;')
    Password = input('Your password;')
    Age = input('Your Age;')
    Occupation = input('Your occupation;')
    Profile['Name'] = username
    Profile['password'] = Password
    Profile['Age'] = Age
    Profile['Occupation'] = Occupation
    Prof= Profile
    def profiles(Prof):
        print(Prof)
    profiles(Prof)

# assignment run this in a loop