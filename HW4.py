import random
words = ['apple', 'bread', 'candy', 'dream', 'eagle', 'flame', 'grape', 'house', 'input', 'joker']

def generate(words):
    return random.choice(words)

def start(words,tries =6):
    secret_word = generate(words)
    word_length = len(secret_word)
    print("Welcome to Wordle!", f"\nGuess the {word_length} -letter word. You have {tries} tries.")

    while tries!=0:
        guess = input("Attempt "+str(7 - tries)+"/6 – Enter guess: ").lower()
        if not guess.isalpha():
            print("Enter a letter")
            continue
        if len(guess)!=word_length:
            print(f"Wrong length. Expected {word_length} letter words, got {len(guess)} " )
            continue

        if guess== secret_word:
            print("You win!!!")
            break


        display=[]
        j=0
        while j<word_length:
            s = guess[j]
            if s == secret_word[j]:
                display.append(f"[{s.upper()}]")
            elif s in secret_word:
                display.append(f"({s})")
            else:
                display.append(s)
            j+=1

        print("Result:", ' '.join(display))
        tries += - 1
    else:
        final = secret_word
        print("You lose! The word was:", final)



def again():

    while True:
        start(words)

        again = input("Again? enter: yes/no ").lower()
        if again != 'yes':
            print("оs.remоve :)")
            break

if __name__ == "__main__":
    again()
