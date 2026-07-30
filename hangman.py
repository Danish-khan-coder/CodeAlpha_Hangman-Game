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
start_art = r"""
 _   _    _    _   _  ____ __  __    _    _   _ 
| | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
| |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
|  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
|_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|
"""
win_art = r"""
__   __           __        ___       _ 
\ \ / /__  _   _  \ \      / (_)_ __ | |
 \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
  | | (_) | |_| |   \ V  V / | | | | |_|
  |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
"""
lose_art = r"""

 __   __            _                     
 \ \ / /__  _   _  | |    ___  ___  ___   
  \ V / _ \| | | | | |   / _ \/ __|/ _ \  
   | | (_) | |_| | | |__| (_) \__ \  __/  
   |_|\___/ \__,_| |_____\___/|___/\___| 
"""
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
    print(start_art)
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
            
            print(win_art)
            is_runnig=False
            
        
        
        if wrong_guesses==6:
            display_man(wrong_guesses)
            print(f"\n{lose_art}\nThe correct word was: {answer}")
            is_runnig=False
                  
if __name__ == "__main__":
    main()