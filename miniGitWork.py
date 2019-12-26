lastCode = input()
newCode = input()

if(len(lastCode)==len(newCode)):
    for i in range(len(lastCode)):
        if (lastCode[i]!=newCode[i]):
            print('[%s | %s]' % (lastCode[i],newCode[i]), end='')
        else:
            print(lastCode[i],end='')
