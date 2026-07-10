import random


hangman_art = {
    0: (
        " _ ",
        "   ",
        "   "
    ),
    1: (
        " O ",
        "   ",
        "   "
    ),
    2: (
        " O ",
        " | ",
        "   "
    ),
    3: (
        " O ",
        "/| ",
        "   "
    ),
    4: (
        " O ",
        "/|\\",
        "   "
    ),
    5: (
        " O ",
        "/|\\",
        "/  "
    ),
    6: (
        " O ",
        "/|\\",
        "/ \\"
    )
}
words =("apple", "banana", "melon", "strawberry", "pineapple")
def display_man(Wrong_Guesses):
    print("#######################")
    for line in hangman_art[Wrong_Guesses]:
        print(line)
        
    print("#######################")
    
    
def display_hint(hint):
    print(" ".join(hint))
    pass
def display_ans(answer):
    print(" ".join(answer))
def main():
    answer = random.choice(words)
    
    hint =["_"]*len(answer)
    wrong_guesses =0
    guessed_letters = set()
    is_runnig =True
    
    while is_runnig:
        display_man(wrong_guesses)
        display_hint(hint)
       
        guess =input("Enter a letter : ").lower()
        
        if len(guess)>1 or not guess.isalpha:
            print(f"'{guess}' is invalid input enter a single letter please")
            continue
        
        if guess in guessed_letters:
            print(f"You have already guessed this letter '{guess}'")
            continue 
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess
            
        else:
            wrong_guesses+=1
            
        if "_" not in hint:
            display_man(wrong_guesses)
            display_ans(answer)
            
            print("\n\nYou won !!!!")
            is_runnig=False
            
        
        
        if wrong_guesses==6:
            display_man(wrong_guesses)
            print(f"Game ower !!!!  {answer}  was correct answer")
            is_runnig=False
                  
if __name__ == "__main__":
    main()