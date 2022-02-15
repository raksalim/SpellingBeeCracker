def writeAnswersToFile(listOfAnswers, mustHave, otherLetters):

    f = open("allPossibleAnswers.txt", "w")
    f.write("\n------------------------------------------------------------------\n")
    f.write(mustHave + "\n")
    f.write(otherLetters + "\n\n")

    for word in listOfAnswers:
        f.write(word + "\n")

    f.close()


def printWordsSortedByLenght(wordList):

    print("\nPossible Words (sorted by length): ")

    wordList.sort(key=len)
    
    for word in wordList:
        print(word)


def isValidWord(word, invalidLetters):

    for letter in invalidLetters:
        if letter in word:
            return False

    return True


def removeLettersFromAlphabet(listOfLettersToRemove):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in listOfLettersToRemove:
        alphabet = alphabet.replace(letter, "")

    return alphabet


## Example Entry:
# The letter the word MUST include: v
# Other letters word may include: tinoel

def main():

    fullListOfWords = open("english_words_usa.txt", "r")

    mustHave = str(input("The letter the word MUST include: "))
    otherLetters = str(input("Other letters word may include: "))
    otherLetters = otherLetters + mustHave

    remainingAplhabets = removeLettersFromAlphabet(otherLetters)

    possibleWords = []

    for word in fullListOfWords:
        if (mustHave in word) and len(word) > 4 and isValidWord(word, remainingAplhabets):
            possibleWords.append(word.strip())

    writeAnswersToFile(possibleWords, mustHave, otherLetters)
    printWordsSortedByLenght(possibleWords)

main()