# zoro = {
#     "Name": "Roronoa Zoro",
#     "Affiliation":"Pirate",
#     "Bounty" : "1.11 Bilion Berries",
#     "Pirate Crew" : "Strawhats",
#     "Class" : "Swordsman",
#     "Likes" : "Sake",
#     "Nickname":"Pirate Hunter",
#     "Nickname":"King of Hell",
# }

# print(zoro)
#{'Name': 'Roronoa Zoro', 'Affiliation': 'Pirate', 'Bounty': '1.11 Bilion Berries', 
# 'Pirate Crew': 'Strawhats', 'Class': 'Swordsman', 'Likes': 'Sake', 'Nickname': 'King of Hell'}
# print(zoro["Nickname"])
# #King of Hell
# print(len(zoro))
# #7
zoro = {
    "Name": "Roronoa Zoro",
    "Affiliation":"Pirate",
    "Bounty" : "1.11 Bilion Berries",
    "Pirate Crew" : "Strawhats",
    "Class" : "Swordsman",
    "Likes" : "Sake",
    "Nickname":["Pirate Hunter","King of Hell"],
}

print(type(zoro))
print(zoro)