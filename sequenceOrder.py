# python3
# fdelator@github.com

# summary:
# program will prompt for sequence of numbers, separate by commas
# outputs average, min and max number in sequence
# determines if sequence is in ascending, descending, or out of order.
# also determines if a single value was given, or if all values are the same digit.

# modularized functions:
# getAverage()
# getLargest()
# getSmallest()
# isOrdered()
# main() at the bottom.


# calculate the average
def getAverage(numberList):
    sumNumbers = sum(numberList)
    numAverage = sumNumbers/(len(numberList))
    print('The average of the sequence ' + str(numberList) + ' is ' + str(numAverage))

# calculate the max value
def getLargest(numberList):
    maxNumber = max(numberList)
    print('The largest number in the sequence ' + str(numberList) + ' is ' + str(maxNumber))

# calculate the min value
def getSmallest(numberList):
    minNumber = min(numberList)
    print('The smallest number in the sequence ' + str(numberList) + ' is ' + str(minNumber))

def isOrdered(numberList):

  # employ boolean logic
  # 4 conditions to parse through:
  # sameNumber, ascending, descending, outOforder
  # set flags equal to True, until refuted
  sameNumber = True
  ascending = True
  descending = True
  outOforder = True

  # iterate through values of numberList[i] vs numberList[i+1]
  # set flags to False when merely one contradiction exists
  for i in range(len(numberList)-1):
    # example:
    # if seq 1,1,1,2,1
    # then   T,T,T,F,F
    # sameNumber remains F after one violation
    if numberList[i] != numberList[i+1]:
      sameNumber = False
    # example:
    # if seq 2,2,3,4,2,5,
    # then   T,T,T,T,F,F
    # if [i] is larger than [i+1] at any position
    # ascending flag set to False for the remainder of loop  
    if numberList[i] > numberList[i+1]:
      ascending = False
    # same logic here
    # if ascending, then not descending
    if numberList[i] < numberList[i+1]:
      descending = False
    # if sameNumber, ascending, descending = False
    # outOforder flag remains True

  # check boolean logic
  # print statement for flag that is True
  # if sameNumber is True
  if sameNumber:
    print('The sequence is all the same number')
  # if sameNumber, ascending, and descending are False (not True)
  # then out of order
  elif not ascending and not descending:
    print('The sequence is out of order')
  # if ascending and descending are not both false, then one is True
  # if one is False, then the other must be True
  elif not descending:
    print('The sequence is in ascending order')
  elif not ascending:
    print('The sequence is in descending order')

def main():
    # request user input
    # input() generates string
    numberString = input('Enter sequence of whole numbers separated by commas, e.g. -1,0,1: ')
    
    # prompt for correct input
    # while numberString is False (e.g. Enter)
    # ASCII, or numberString[0] is not a number 0-9 or '-' (negative number)
    # then ask for input again
    # cannot process fractional numbers, see below
    while not numberString or ord(numberString[0]) < 45 or ord(numberString[0]) > 57:
      numberString = input('Invalid. Enter sequence of whole numbers separated by commas, e.g. -1,0,1: ')


    # prepare empty list to store values by split method
    numberList = list()

    # for every char split by comma in numberString
    # append char as int to numberList
    # cannot process fractional numbers
    # limitation of int()
    for char in numberString.split(','):
      numberList.append(int(char))
    
    # initialize functions
    getAverage(numberList)
    getLargest(numberList)
    getSmallest(numberList)
    
    
    # 5 conditions to parse thru:
    # input is 1 number
    # input is all sameNumber
    # input is ascending, descending, or outOforder
    # address condition 1
    if len(numberList) == 1:
      print('The sequence is only one digit long')

    # address conditions 2-5 using isOrdered()
    # see isOrdered above
    # print the returned string
    else:
      isOrdered(numberList)
        
# tell intepreter to start module main() first    
if __name__ == '__main__': main()
