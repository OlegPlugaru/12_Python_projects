# Init Variables
theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

profession = ["", "", "", ""]
adj = ["", ""]

# Get Input From User
print("Welcome user")
print("Let's Play a game of madlibs!")
neo = input("Please share with me your name: ")

# Getting the Matrix variable from user
print(f"Hello {neo}! Are you ready?")
theMatrix = input("What is something you want to know more about: ")

# Getting system variable from user
print(f"Oooh! You want to know more about {theMatrix} huh?")
print(f"Okay well first, tell me what you already know about {theMatrix}")
system = input(f"What noun would you categorize {theMatrix} as: ")

# Getting enemy variable from user
enemy = input(f"Give me an opposing noun to {system}: ")

# Getting inside variable from user
inside = input(f"Now give me any relaxing noun (present tense): ")

# Getting all profession from user
print(f"Okay, now I need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"Profession (plural) {i+1} / {len(profession)}: ")

# Getting the save variable
save = input(f"Give me a hero-related verb (present tense): ")

# Getting the unplugged variable
unplugged = input(f"Now give me a verb that makes you think about relief (past tense): ")

# Getting the adjectives
print(f"Lastly I need 2 dystopian adjectives")

for i in range(len(adj)):
    adj[i] = input(f"Adjective {i+1} / {len(adj)}: ")

# Getting the fight variable
fight = input(f"& a verb: ")

# Init Story
madlibstory = (f"{theMatrix} is a {system}, Neo. That system is our {enemy}.\n" + 
f"But when you're {inside}, you look around, what do you see?\n" + 
f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds\n" + 
f"of the people we are trying to {save}. But until we do,\n" + 
f"these people are still a part of that {system} and that makes\n" + 
f"them our {enemy}. You have to understand, most of these people\n" +  
f"are not ready to be {unplugged}. And many of them are so {adj[0]}\n" + 
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.\n")

# Print Story
print(madlibstory)