import socket

def correctingTxt(data):
    new = []
    new1 = []
    new2 = []
    listinput = []
    temp = []
    capital = 0
    count = 0

    listinput = data.lower()
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

    str1 = ''.join(new)

    for i in range(len(new)):
        if(new[i] == "\n"):
            new1.append(" ")
        else:
            new1.append(new[i])
    str2 = ''.join(new1)
    str3 = str2.split(' ')
    words = str(len(str3) - 1)
    characters = str(len(str1) - 1)
    #output = str1 + "\nTotal count : " + str(words) + " words, " + str(characters) + " characters"

    for i in range(len(str3)):
        lenstr = len(str3[i])
        count = count + lenstr
        if(count>=60):
            temp = str3[i]
            new2.append("\n")
            new2.append(temp)
            count = 0 + len(temp)
        elif(str3[i].endswith(".")):
            temp = str3[i]
            new2.append(" ")
            new2.append(temp)
            new2.append("\n")
            count = 0  
        else:
            temp = str3[i]
            if(str3[i-1].endswith(".")):
                new2.append(temp)
                count = count + 1
            else:    
                new2.append(" ")
                new2.append(temp)
                count = count + 1 #space
    str4 = ''.join(new2)
    output = str4 + "\nTotal count : " + str(words) + " words, " + str(characters) + " characters"
    return output

HOST = '' # Symbolic name meaning all available interfaces
PORT = 30036 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    newdata = correctingTxt(data)
    conn.sendall(newdata)
conn.close()
