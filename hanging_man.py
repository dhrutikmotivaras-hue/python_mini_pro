import random

#words = ("apple","orange","banana","coconut","pineapple")
words = (
"apple","orange","banana","coconut","pineapple","mango","papaya","guava","strawberry","blueberry",
"blackberry","raspberry","watermelon","muskmelon","kiwi","pomegranate","cherry","peach","pear","plum",
"apricot","fig","date","lychee","dragonfruit","passionfruit","grapefruit","lemon","lime","avocado",
"jackfruit","starfruit","cranberry","mulberry","gooseberry","tamarind","sugarcane","carrot","potato","tomato",

"paris","london","tokyo","delhi","mumbai","sydney","berlin","madrid","rome","dubai",
"singapore","bangkok","beijing","seoul","chicago","toronto","vancouver","amsterdam","vienna","prague",
"zurich","oslo","stockholm","helsinki","copenhagen","dublin","edinburgh","lisbon","athens","istanbul",
"cairo","nairobi","capetown","jakarta","manila","kuala","doha","tehran","baghdad","colombo",

"tiger","lion","elephant","giraffe","zebra","kangaroo","panda","koala","monkey","chimpanzee",
"gorilla","leopard","cheetah","hyena","fox","wolf","dog","cat","rabbit","deer",
"horse","donkey","camel","buffalo","cow","goat","sheep","pig","squirrel","rat",
"mouse","bat","owl","eagle","falcon","parrot","sparrow","pigeon","flamingo","peacock",

"table","chair","laptop","mobile","keyboard","mouse","monitor","printer","bottle","glass",
"plate","spoon","fork","knife","clock","watch","fan","light","bulb","switch",
"door","window","curtain","pillow","blanket","mattress","sofa","cupboard","shelf","mirror",
"bag","wallet","purse","umbrella","helmet","shoes","slippers","socks","jacket","shirt",

"river","mountain","ocean","desert","forest","island","valley","waterfall","volcano","glacier",
"cloud","rain","storm","thunder","lightning","rainbow","breeze","shadow","flame","smoke",
"music","dance","painting","drawing","writing","reading","gaming","coding","typing","learning",
"school","college","teacher","student","exam","subject","project","homework","holiday","festival"
)

#dictionary of key:()--->below is the asci art
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" ° ",
                    "   ",
                    "   "),
                2: (" ° ",
                    " | ",
                    "   "),
                3: (" ° ",
                    "/| ",
                    "   "),
                4: (" ° ",
                    "/|\\",
                    "   "),
                5: (" ° ",
                    "/|\\",
                    "/  "),
                6: (" ° ",
                    "/|\\",
                    "/  \\")}


#for line in hangman_art[5]:(this code for just display the man)
#    print(line)


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))



def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer) # this was print dash(_) for random words
    wrong_guesses = 0
    guesses_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter:-- ").lower()
        

        #this is for invalid input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue
        

        #if letter/word already exist
        if guess in guesses_letters:
            print(f"{guess} is already guessed")
            continue

        guesses_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        #this condition for if there is wrong guess
        else:
            wrong_guesses += 1


        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False

        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running = False

if __name__=="__main__":
    main()