
import os
from time import sleep

# Variables : 
status = ''
UserAction = ''
PurCommand = ''
TheList = []
indexlistIncrease = 0

# Function : 
def DisplayList(List) :
    NumberBefore = 1
    ListIndex = 0
    for List in range (len(TheList)) :
        print(NumberBefore , '.' , TheList[ListIndex])
        NumberBefore += 1
        ListIndex += 1

def ActionCleaner(TheInput) :
    global indexlistIncrease
    global PurCommand
    TheInput = list(UserAction)
    for SupprBlank in range(len(TheInput)) :
        if TheInput[indexlistIncrease] == " " :
            TheInput.remove(TheInput[indexlistIncrease])
        else :
            indexlistIncrease += 1
    PurCommand = ''.join(TheInput)
    indexlistIncrease = 0

def ActionChecker(strTotest) :
        global status
        if len(strTotest) > 3 : 
            status = 'ERROR : Max command lenght is 3 characters'
    
def ActionFinder(TheCmd):
    global status
    if TheCmd == 'add' :
        AddAction()
    elif TheCmd == 'del' :
        DelAction()
    elif TheCmd == 'cop' :
        print('test')
    elif TheCmd == 'inf' :
        InfAction()
    elif TheCmd == '' :
        print('test')
    else :
        status = 'ERROR : Unknow Command'

def AddAction() :
    os.system('clear')
    print('///////////// LIST MANAGER /////////////\n')
    print('======== ADDING ========\n')
    StrToAdd = str(input('What do you want to add to the list ? '))
    TheList.append(StrToAdd)

def DelAction() :
    global status
    os.system('clear')
    print('///////////// LIST MANAGER /////////////\n')
    print('======== REMOVING ========\n')
    StrToDel = int(input('Give the index of the element to delete : '))
    if int(StrToDel) :
        # if StrToDel > len(TheList) : 
        TheList.remove(TheList[StrToDel - 1])
    else : 
        status = 'ERROR : you need to give an valid index from the list'
def InfAction() :
    os.system('clear')
    print('///////////// LIST MANAGER /////////////\n')
    print('======== INFORMATION ========\n')
    print('Command list : \nadd -> to add an element to the list\ndel -> to delete an element from the list')
    input('Exit ?')

# Main Loop 

while True : 
    os.system('clear')
    print('///////////// LIST MANAGER /////////////\n')
    print('------------')
    DisplayList(TheList)
    if len(TheList) == 0 : 
        print('\nList is empty \n')
    print('------------')
    print('\ntype "inf" for help')
    if status != '' :
        print(status)
    status = ''
    UserAction = input('Enter an action : ')
    ActionCleaner(UserAction)
    ActionChecker(PurCommand)
    if (status == '') :
        ActionFinder(PurCommand)


