if __name__ == '__main__':
    n = int(input())

    # Students and grade lists
    nameList = []
    gradeList = []

    # Importing values
    if __name__ == '__main__':
        for _ in range(n):
            name = input()
            score = float(input())
            nameList.append((score,name))
            gradeList.append(score)

    # Define final lists
    finalNameList = nameList[:]
    finalGradeList = []
    finalList = []

    # Removing unwanted values
    for i in range(n):
        if nameList[i][0] == min(gradeList):
            finalNameList.remove(nameList[i])

    # Final grade list creation
    for i in range(len(finalNameList)):
        finalGradeList.append(finalNameList[i][0])

    # Adding wanted values
    for i in range(len(finalNameList)):
        if finalNameList[i][0] == min(finalGradeList):
            finalList.append(finalNameList[i][1])

    # Sorting the list
    finalList.sort()

    # Print result 
    for i in range(len(finalList)):
        print(finalList[i])