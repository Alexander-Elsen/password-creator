

def main():
    '''This is the main def that always gets executed'''
    import random
    import string
    import time
    continuewithloop = True
    while continuewithloop:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle1 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle2 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle3 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle4 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle5 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle6 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle7 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle8 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle9 = letter + str(cijfer) + speciaal_teken
        letter = random.choice(letters)
        cijfer = random.randrange(1, 9)
        speciaal_teken = random.choice(string.punctuation)
        alle10 = letter + str(cijfer) + speciaal_teken
        Alle1 = random.choice(alle1)
        Alle2 = random.choice(alle2)
        Alle3 = random.choice(alle3)
        Alle4 = random.choice(alle4)
        Alle5 = random.choice(alle5)
        Alle6 = random.choice(alle6)
        Alle7 = random.choice(alle7)
        Alle8 = random.choice(alle8)
        Alle9 = random.choice(alle9)
        Alle10 = random.choice(alle10)

        Alles = Alle1 + Alle2 + Alle3 + Alle4 + Alle5 + Alle6 + Alle7 + Alle8 + Alle9 + Alle10
        print(Alles)
        time.sleep(1.5)
        vraag = input('Do you want another password?')
        if vraag == 'no':
            print('Okay!')
            continuewithloop = False
        elif vraag == 'yes':
            print('Okay!')
            time.sleep(1)
        else:
            print("I don't know that word so I'll give you another password!")
            time.sleep(2)



if __name__ == "__main__":
    main()