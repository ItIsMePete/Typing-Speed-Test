import timeit
import time
import random

#get the text for user to copy from local file
def getChallenge(text):
    f = open(text+".txt", "r")
    l = f.readlines()
    f.close()
    cont = True
    while(cont == True):
        r = random.randint(0,len(l)-1)
        if(len(l[r]) > 2):
            challenge = l[r].strip()
            cont = False
    return challenge

#give the text for user to copy
def testPrompt(challenge, difficulty):
    print("Type out the following:")
    print(challenge)
    input("Press Enter to Begin...")
    testResult, t =  testSpeed(challenge)
    wpm = determineWPM(t, challenge)
    print("WPM: " + str(wpm))
    if(difficulty > 2):
        accuracy = hardAccuracy(testResult, challenge)
    else:
        accuracy = easyAccuracy(testResult, challenge)
    print(str(accuracy) + "% accurate")

#calculate Word Per minute from reference text
def determineWPM(t, challenge):
    wpm = "{:.2f}".format((len(challenge)/5)/t)
    return wpm

#calculate the accuracy of user speed test character by character
def hardAccuracy(testResults, challenge):
    #determine accuracy based on character & position if character at both positions are correct then +1 to correct 
    cnt = 0;
    for i, c in enumerate(challenge):
        try:
            if(testResults[i] == c):
                cnt += 1
        except: pass
    accuracy = (cnt/len(challenge))*100
    return "{:.2f}".format(accuracy)

#calculate the accuracy of user speed test word by word
def easyAccuracy(testResults, challenge):
    test = challenge.split()
    word = testResults.split()
    numbWords = 0
    cnt = 0
    for i, c in enumerate(test):
        if(word[i] == c):
            cnt += 1
        numbWords += 1
    accuracy = (cnt/numbWords)*100
    return accuracy
    
#get user input and total time
def testSpeed(challenge):
    start = time.time() #start time
    words = input("Begin Typing!:\n") #user input text to compare to challenge text
    end = time.time() #end time
    return (words, end-start)

#Speed test starting menu
def main():
    cont = True
    while(cont == True):
        choice = int(input("Choose difficulty (1)Easy, (2) Mediumn, (3)Hard\nChoose: "))
        if choice == 1:
            challenge = getChallenge("easy")
            testPrompt(challenge, 1)
        elif choice == 2:
            challenge = getChallenge("medium")
            testPrompt(challenge, 2)
        elif choice == 3:
            challenge = getChallenge("hard")
            testPrompt(challenge , 3)
        else:
            print("Error invalid input")

        u = input("Y/N:\n").lower()
        if(u == "y"):
            print("go fast")
            cont = True
        else:
            print("stop")
            cont = False



if __name__ == "__main__":
    main()
