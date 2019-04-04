import winsound
import time
##This allows the program to translate the letters into morse
alphabet={"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.",
"G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..",
"M":"--","N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
"U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----",
"1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....",
"7":"--...", "8":"---..", "9":"----."," ":"space", "&":".-...", "'":".----.", "@":".--.-.", ")":"-.--.-", "(":"-.--.",
":":"---...", ",":"--..--", "=":"-...-", "!":"-.-.--", ".":".-.-.-",
"-":"-....-", "+":".-.-.", '"':".-..-.", "?":"..--..", "/":"-..-.",}
##These functions are used to calculate the time between and the
##Frequency and length of each dot and dash. They are put as functions to enable you to change them easily
global timeUnits
timeUnits=0.060
print(timeUnits)
def letterGap():
    time.sleep(0.180)
def wordGap():
    time.sleep(0.420)
def dashdotGap():
    time.sleep(0.060)
def dot():
    winsound.Beep(900,60)
def dash():
    winsound.Beep(900,180)
while 1==1:
    wordTemp=[]
    morseOutput=[]
    print("""Welcome to EnglishToMorse!
    please type a word or sentence to translate""")
    sentence=input("")
    ##This creates a list of the letters in sentence but upper case
    sentenceLIST=list(sentence.upper())
    print(sentenceLIST) ##(For testing purposes)
    ##This translates the letters from the English alphabet to morse code
    ##And puts them in an array
    for y in sentenceLIST:
        morseOutput.append(alphabet[y])
        print(y)##(For testing purposes)
            
    print(morseOutput)##(For testing purposes)
    for x in range (len(morseOutput)):
        ##This detects if there is a space (indicated by the word space)
        ##In order to check if the next piece of morse code is a new word or not
        if morseOutput[x]=="space":
            ##If there is a space, this calls the wordGap function which waits the time specified in that function
            wordGap()
        else:
            ##This stores the combination of dots and dashes for the Xth word in a list
            ##Meaning the dots and dashes are seperated which means the program can focus on one thing at a time
            wordTemp=morseOutput[x]
            print(wordTemp)
            for y in wordTemp:
                if y==".":
                    ##If the morse code character in position Y is a dot this runs the dot function
                    ##Then the dashdotGap function which waits the amount of time specified in the function
                    dot()
                    dashdotGap()
                if y=="-":
                    ##If the morse code character in position Y is a dash this runs the dash function
                    ##Then the dashdotGap function which waits the amount of time specified in the function
                    dash()
                    dashdotGap()
        ##After the letter has been successfuly(hopefully) translated this
        ##Calls the letterGap function which waits the amount of time specified in the function
        letterGap()
        
            
            
        
    
    
    
    
    
    
    
    
    
    


