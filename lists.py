N = int(input())
myList = []

for line in range(N):
    commandLine = input().split()

    match commandLine[0]:
        case 'append':
            myList.append(int(commandLine[1]))
        case 'insert':
            myList.insert(int(commandLine[1]), int(commandLine[2]))
        case 'print':
            print(myList)
        case 'remove':
            myList.remove(int(commandLine[1]))
        case 'sort':
            myList.sort()
        case 'pop':
            myList.pop()
        case 'reverse':
            myList.reverse()