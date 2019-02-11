# python3
# fdelator@github.com

# program accoplishes the following tasks:
# 1) takes ref.txt and stores words in a reference dictionary
# 2) prepareUserFile prompts user for file, generates dictionary with word count
# 3) filterNumbers takes dictionary from prepareUserFile and removes numbers
# 4) fileInfo prints misspelled words, and prompts user for word to give frequency

def prepareUserFile():
    # prompt for filename as string
    fileString = input('Type filename or path to check against reference: ')
    # if Enter pressed, terminate program.
    if not fileString:
        print('No file entered. Program ended.')
        # terminate program
        exit()
    
    # set flag as False
    foundFile = False
    # ask for fileString until string matches a file
    while foundFile == False:
        # error may occur here
        # string may not match file in working directory
        try:
            # assign open file to userFile
            # start at beginning with 'r'
            userFile = open(fileString, 'r')
            # skip directly to 'except' if FileNotFoundError
            # if no FileNoteFoundError, set foundFile to True
            foundFile = True
            # while-loop closes
        except FileNotFoundError:
            # prompt for new fileString if FileNotFoundError
            fileString = input('File not found. Enter file name, or path: ')
            # foundFile remains False if FileNotFoundError
            # try block repeats via with new fileString
            if not fileString:
                # exit if Enter pressed
                print('No file entered. Program ended.')
                exit()
    # inititate empty list
    # make userWords global
    global userWords
    userWords = []
    # nested for-loop
    # read each line in the open file
    # each line is a string
    for text in userFile.readlines():
        # make the string lowercase
        # split the string by spaces to make words
        for word in text.lower().split():
            # common punctuation marks in writing samples
            userWords.append(word.strip('.,!;:'))
    # userWords is a list of words in lowercase
    # close userFile
    userFile.close()

def filterNumbers(userWords):
    # initiate empty dictionary for words from userFile
    # make wordCount global
    global wordCount
    wordCount = {}
    # filter-out numbers in userWords
    # recall that userWords is a list of strings
    for string in userWords:
        try:
            # cast string as int
            int(string)
            # ValueError possible
            # if int() successful...
            # then remove string element
            userWords.remove(string)
        except ValueError:
            # when string cannot be cast as int
            # skip a.k.a 'pass' to next string element
            pass
    # calculate frequency of words
    # for every string in updated userWords list
    for word in userWords:
        # no string is accounted for at the beginning
        # when string is not in wordCount...
        # the 'key:value pair' is added for that string
        # as for-loop progresses...
        # if the 'key' already exists, then add 1 to value
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    # dictionary 'wordCount' is complete

def fileInfo(userWords, wordCount):
    # userWords is a list of strings
    # iterate through every element in userWords list
    for word in userWords:
        # if an element is not in the reference dictionary...
        # then the word is misspelled
        if word not in dictionary:
            print('The word \'' + word + '\' is misspelled.')

    # prompt for word to find in 'counters' dictionary
    testWord = input('Enter word in file to get word frequency: ')
    
    # set a flag as False until testWord is valid
    foundWord = False
    while foundWord == False:
        # if testWord is found
        if testWord in userWords:
            print('The word \'' + testWord + '\' repeats ' + str(wordCount[testWord]) + ' times.')
            # while-loop closes when foundWord set to True
            foundWord = True
            # proceed to exit()
        if testWord not in userWords:
            print('The word \'' + testWord + '\' is not in the file.')
            # prompt user for another testWord
            testWord = input('Enter word in file to get word frequency: ')
            # while-loop continues
            # if Enter pressed
            if not testWord:
                print('No word entered. Program ended.')
                exit()
    
def main():
    # generate reference dictionary
    # open the reference file
    # start at beginning with 'r'
    referenceFile = open('ref.txt', 'r')
    
    # initiate empty dictionary
    # make dictionary global
    global dictionary
    dictionary = {}
    
    # start index as value for key:value pair
    # hardcode the first element in the index
    index = 1
    # for every word to read in referenceFile
    for word in referenceFile.readlines():
        # store 'word' in empty tuple
        tempTuple = tuple()
        # employ strip method to remove endline
        tempTuple = word.strip('\n')
        # update the dictionary with key:value pair
        # value is the index, starting at 1
        dictionary.update({tempTuple:index})
        # increase index by 1 for next iteration
        index += 1
    # reference dictionary complete
    # call 'dictionary' when needed
    # call each function
    prepareUserFile()
    filterNumbers(userWords)
    fileInfo(userWords,wordCount)
    exit()
 
if __name__ == '__main__': main()