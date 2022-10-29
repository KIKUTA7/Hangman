from random import randint  # Do not delete this line

def displayIntro():
    print("""_______________________________________________
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
_______________________________________________
_____________________Rules_____________________
Try to guess the hidden word one letter at a   
time. The number of dashes are equivalent to   
the number of letters in the word. If a player 
suggests a letter that occurs in the word,     
blank places containing this character will be 
filled with that letter. If the word does not  
contain the suggested letter, one new element  
of a hangman’s gallow is painted. As the game  
progresses, a segment of a victim is added for 
every suggested letter not in the word. Goal is
to guess the word before the man hangs!        
_______________________________________________""")






def displayEnd(result):
    if(result) :
        print("""________________________________________________________________________
          _                                  _                          
         (_)                                (_)                         
__      ___ _ __  _ __   ___ _ __  __      ___ _ __  _ __   ___ _ __    
\ \ /\ / / | '_ \| '_ \ / _ \ '__| \ \ /\ / / | '_ \| '_ \ / _ \ '__|   
 \ V  V /| | | | | | | |  __/ |     \ V  V /| | | | | | | |  __/ |      
  \_/\_/ |_|_| |_|_| |_|\___|_|      \_/\_/ |_|_| |_|_| |_|\___|_|      
           | |   (_)    | |                  | (_)                      
        ___| |__  _  ___| | _____ _ __     __| |_ _ __  _ __   ___ _ __ 
       / __| '_ \| |/ __| |/ / _ \ '_ \   / _` | | '_ \| '_ \ / _ \ '__|
      | (__| | | | | (__|   <  __/ | | | | (_| | | | | | | | |  __/ |   
       \___|_| |_|_|\___|_|\_\___|_| |_|  \__,_|_|_| |_|_| |_|\___|_|   
________________________________________________________________________""")
    else:
        print(""" __     __           _           _   _                                    
 \ \   / /          | |         | | | |                                   
  \ \_/ /__  _   _  | | ___  ___| |_| |                                   
   \   / _ \| | | | | |/ _ \/ __| __| |                                   
    | | (_) | |_| | | | (_) \__ \ |_|_|                                   
    |_|\___/ \__,_| |_|\___/|___/\__(_)                                   
        _______ _                                        _ _          _ _ 
       |__   __| |                                      | (_)        | | |
          | |  | |__   ___   _ __ ___   __ _ _ __     __| |_  ___  __| | |
          | |  | '_ \ / _ \ | '_ ` _ \ / _` | '_ \   / _` | |/ _ \/ _` | |
          | |  | | | |  __/ | | | | | | (_| | | | | | (_| | |  __/ (_| |_|
          |_|  |_| |_|\___| |_| |_| |_|\__,_|_| |_|  \__,_|_|\___|\__,_(_)
__________________________________________________________________________""")

def displayHangman(state):
    if(state == 5):
       print("""     ._______.   
     |/          
     |           
     |           
     |           
     |           
     |           
 ____|___        """)
    elif (state == 4):
        print("""     ._______.   
     |/      |   
     |           
     |           
     |           
     |           
     |           
 ____|___        """)
    elif (state == 3):
        print("""     ._______.   
     |/      |   
     |      (_)  
     |           
     |           
     |           
     |           
 ____|___        """)
    elif (state == 2):
        print("""     ._______.   
     |/      |   
     |      (_)  
     |       |   
     |       |   
     |           
     |           
 ____|___        """)
    elif (state == 1):
     print("""     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |           
     |           
 ____|___        """)
    else:
      print("""     ._______.   
     |/      |   
     |      (_)  
     |      \|/  
     |       |   
     |      / \  
     |           
 ____|___        """)


def getWord():
    lis = []
    file = "hangman-words.txt"
    fileRead = open(file, "r")
    lines = fileRead.readlines()
    for oneLine in lines:
        lis.append(oneLine.strip("\n"))
    return lis[randint(0,852)]






def valid(charConstant):
    if(len(charConstant) != 1): return False
    if(ord('a')<=ord(charConstant) and ord(charConstant)<=ord('z')) : return True
    return False



def play():
    rand = getWord()
    dashes = []
    alphabet = []
    for iterator in range(26):
        alphabet.append(0)
    displayHangman(5)
    for iterator in range(len(rand)):
        dashes.append(0)
    lives = 5
    gamocnobili = 0

    while (lives > 0):
     temp = ""
     for iterator in range(len(dashes)):
            if (dashes[iterator] == 0):
                temp = temp + "_"
            else:
                temp = temp + rand[iterator]
     print("Guess the word:  " + temp)
     userInput = input("Enter the letter: ")
     while (not valid(userInput)):
        userInput = input("Enter the letter: ")

     if(alphabet[ord(userInput) - ord('a')] == 0): alphabet[ord(userInput) - ord('a')] = 1
     else :
         print("You have entered this letter before , please enter another")
         continue
     iterator = 0
     t = False
     for c in rand:
        if(userInput == c):
            t = True
            if (dashes[iterator] == 0):
                gamocnobili += 1
                dashes[iterator] = 1

        iterator +=1
     if(not t):
        lives-=1
     if(gamocnobili < len(rand)):  displayHangman(lives)
     else:
         print("Hidden word was: " + rand)
         return True
    print("Hidden word was: " + rand)
    return False

def hangman():
    while True:
        displayIntro()
        result = play()
        displayEnd(result)
        str1 = input("Do you want to play game one more time?(yes/no)")
        if(str1 == "no") : break



if __name__ == "__main__":
    hangman()

