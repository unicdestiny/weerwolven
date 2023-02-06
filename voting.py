'''
#working config

running = True
i=0
boodschap=""
weerwolven=[
    "peter",
    "jan",
    "jos",
    "an",
    "lies",
    "Kai",
    "Zion",
    "Jayden",
    "Eliana",
    "Luca",
    "Ezra",
    "Maeve",
    "Aaliyah"
]
numberOfPeople=len(weerwolven)-1
weerwolfNaam= weerwolven[int(random.randrange(0,numberOfPeople))]
previousGuess=[]

while running:
    i += 1
    if len(previousGuess)==0:
        name=input("give in a name: ")
        if weerwolfNaam==name:
            boodschap="guessed it"
            running=False
        else:
            previousGuess.append(name)
    else:
        nieuweNaam = input("give in a name: ")
        for previouseName in previousGuess:
            if previouseName==nieuweNaam:
                print("you used it already")
                name=input("give in a name: ")
        if(weerwolfNaam==nieuweNaam):
            text="you guessed it "
            running=False
        elif(i==numberOfPeople):
            text="you're dead"
            running=False
        previousGuess.append(nieuweNaam)
print(boodschap)
'''
