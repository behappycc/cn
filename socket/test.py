new = []
new1 = []
new2 = []
listinput = []
temp = []
capital = 0
count = 0

listinput = "it's not the hot commodity it was last year but gold has been creeping its way back to prominence of late.the yellow metal is once again over $1,700 an ounce, up more than 10% for the year,and well off the lows hit early last summer.With gold in The Upper End of the $1,500 to $1,900 range that it has traded in since making all-time highs in 2011,It's a good time for investors to question whether it's time to load up ahead of a potential push to new highs."
for i in range(len(listinput)):
    if(i == 0):
        temp = listinput[i].upper()
        new.append(temp)

    elif(listinput[i] == "," and (listinput[i+1] == "0" or listinput[i+1] == "1" or listinput[i+1] == "2" \
        or listinput[i+1] == "3" or listinput[i+1] == "4" or listinput[i+1] == "5"\
        or listinput[i+1] == "6" or listinput[i+1] == "7" or listinput[i+1] == "8"\
        or listinput[i+1] == "9")):
        new.append(",")

    elif(listinput[i] == "," and listinput[i+1] == " "):
        new.append(",")

    elif(listinput[i] == "," and listinput[i+1] != " "):
        new.append(",")
        new.append(" ")

    elif(listinput[i] == "." ):
        new.append(".")
        new.append("\n")
        capital = 1

    elif(listinput[i] == " " and listinput[i-1] == "." and capital ==1):
        capital = 1

    elif(listinput[i] != " " and listinput[i-1] == "." and capital ==1):
        temp = listinput[i].upper()
        new.append(temp)
        capital = 0

    elif(listinput[i] != " " and listinput[i-2] == "." and capital ==1):
        temp = listinput[i].upper()
        new.append(temp)
        capital = 0

    elif(listinput[i] != "," and listinput[i] != "." ):
        temp = listinput[i]
        new.append(temp)

#print new
str1 = ''.join(new)

for i in range(len(new)):
    if(new[i] == "\n"):
        new1.append(" ")
    else:
        new1.append(new[i])
str2 = ''.join(new1)
str3 = str2.split(' ')
words = len(str3) - 1
characters = len(str1) - 1

for i in range(len(str3)):
        lenstr = len(str3[i])
        count = count + lenstr
        print str3[i], count
        if(count>=60):
            print "count>60"
            temp = str3[i]
            new2.append("\n")
            new2.append(temp)
            count = 0 + len(temp)
        elif(str3[i].endswith(".")):
            print "endwith"
            temp = str3[i]
            new2.append(" ")
            new2.append(temp)
            new2.append("\n")
            count = 0  
        else:
            print "hi"
            temp = str3[i]
            if(str3[i-1].endswith(".")):
                new2.append(temp)
                count = count + 1
            else:    
                new2.append(" ")
                new2.append(temp)
                count = count + 1 #space
str4 = ''.join(new2)
    #return str4
print str4
#print ne

#output = str(str1) + "\nTotal count : ", words, "words,",characters, "characters" 
#print output
#more than 10% for the year, and well off the lows hit early