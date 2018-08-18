# -*- coding: utf-8 -*-
"""
Code24

For the drinking game that requires you to figure out if the four cards randomly chosen can produce the number 24 by introducing mathematic operations between the numbers in any sequence
WIP: Have not introduced the logic of allowing brackets (which my friends and I permit when we play)
"""
import copy
import collections

def permutate(num1, num2, num3, num4): 
    # Takes 4 numbers
    # Permutate to get all possible sequence
    listOfPermutations = []
    
    numArray = [num1, num2, num3, num4]
    
    for i in range(0,4): 
        
        numArray2 = copy.deepcopy(numArray)
        numInSeq1 = numArray2.pop(i)
        
        for j in range(0,3): 
            
            numArray3 = copy.deepcopy(numArray2)
            numInSeq2 = numArray3.pop(j)
            
            listOfPermutations.append([numInSeq1, numInSeq2, numArray3[0], numArray3[1]])
            listOfPermutations.append([numInSeq1, numInSeq2, numArray3[1], numArray3[0]])
    
    return listOfPermutations
    

def operationSequence(operations): 
    # Takes a list of allowable operations
    # Get all possible operation sequence (Combinatorial)
    # operations = ['+', '-', '*', '/']
    listOfOperationSequence = []
    
    for o1 in operations: 
        for o2 in operations: 
            for o3 in operations: 
                listOfOperationSequence.append([o1,o2,o3])
                
    return listOfOperationSequence


def evalList(listOfCommands): 
    # Takes a list of commands and evaluate them to return a list of their results
    listOfResults = []
    for command in listOfCommands: 
        listOfResults.append(eval(command))
    return listOfResults

def factorial(num): 
    if num == 1: 
        return num
    else: 
        return num*factorial(num-1)

def getDivisor(listOfNums): 
    # Takes a list of numbers to return the number to divide by due to the occurence of the same number more than once
    listOfAppearances = list(collections.Counter(listOfNums).values())
    divisor = 1
    print(listOfAppearances)
    for appearance in listOfAppearances: 
        divisor *= factorial(appearance)
    
    return int(divisor)


def code24(num1, num2, num3, num4): 
    
    permutationOfNumbers = permutate(str(num1), str(num2), str(num3), str(num4))
    combinationOfOperations = operationSequence(['+', '-', '*', '/'])
    listOfJointCombination = []
    
    for permutation in permutationOfNumbers: 
        for combination in combinationOfOperations: 
            listOfJointCombination.append(permutation[0] + 
                                          combination[0] + 
                                          permutation[1] + 
                                          combination[1] + 
                                          permutation[2] + 
                                          combination[2] + 
                                          permutation[3])
    
    results = evalList(listOfJointCombination)
    divisor = getDivisor([num1, num2, num3, num4])
    
    return (results.count(24) > 0, results.count(24)/divisor)