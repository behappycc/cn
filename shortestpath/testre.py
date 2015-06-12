import re

listinformation = []

def parseData():
    f = open('usa.txt', 'r')
    fileout = open('out.txt', 'w')
    sourceInLines = f.readlines()
    f.close()
    for index, line in enumerate(sourceInLines):
        if  index > 0 and index < 87576:
            temp = re.split('\s+', line)
            a = [ int(x) for x in temp if x != '' ]
            listinformation.append(a)
            fileout.write(str(a))
            fileout.write('\n')
        elif index > 87576 and index < 209538:
            temp = re.split('\s+', line)
            a = [ int(x) for x in temp if x != '' ]
            listinformation.append(a)
            fileout.write(str(a))
            fileout.write('\n')
        else:
            pass   
        
if __name__ == '__main__':
    parseData()
    print listinformation[87575][0]