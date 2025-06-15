import random

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker',"nigga"]
x = random.random()
y = x * len(words)
secret_word = words[int(y)]

tries = 6
wl = len(secret_word)
w = secret_word

print("Welcome to Wordle!", f"\nGuess the {wl} -letter word. You have {tries} tries.")

while tries!=0:
    guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
    
    if len(guess)!=wl:
        print(f"Wrong length. Expected {wl} letter words, got {len(guess)} " )
        continue

    if guess==w:
        print("You win!!!")
        break


    display=[]
    j=0
    while j<wl:
        s = guess[j]
        if s == w[j]:
            display.append(f"[{s.upper()}]")
        elif s in w:
            display.append(f"({s})")
        else:
            display.append(s)
        j+=1


    print("Result:", ' '.join(display))
    tries += - 1
else:
    final = secret_word
    print("You lose! The word was:", final)
