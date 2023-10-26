wordsee = []
vertical = []
diagonal = []
check = []

y = 0

#get the wordsearch
wordSearch = open("Book1.csv","r")
print(wordSearch.read())
wordSearch.close

file1 = open("Book1.csv","r")
file1 = file1.readlines()

for line in file1:
    letter = line.rstrip()
    check.append(letter)

for i in range(len(check)):
    width = int(len(check[0]))
    if width != int(len(check[i])):
        print("invalid measurements")
        exit()
        



# words I need to find
words = ["Binary","ComputerScience","Decimal","Hexadecimal","Jupyter","Matplotlib","Notebook","Octal","Pandas","Powershell"]

#horizontal forwards and backwards
#put the wordsearch into rows and combine them in order for them to be read able (without ",")
for line in file1:
    letter = line.rstrip()
    y += 1
    o = letter.replace(",","")
    #check for word
    for i in range(len(words)):
        if words[i].upper() in o:
            print(o)
            print(f"{words[i]} horizontal starts at {1},{y}")
        # reverse the entire word and check if it is backwards
        txt = f"{words[i]}"[::-1]
        if txt.upper() in o:
            print(o)
            print(f"{words[i]} is horizontal backwards and ends at {0},{y}")

#vertical forwards and backwards
# put the wordsearch into rows and individual spots
y = 0
for line in file1:
    letter = line.rstrip().split(",")
    wordsee.append(letter)

for x in range(len(wordsee)):
    y=0
    vertical = []
    # add each letter from each row 
    for i in range(len(wordsee)):
        vertical.append(wordsee[i][x])
        y+=1
    column = ""
    # put the column so it is readable/ is string now
    for i in range(len(vertical)):
        column = column + vertical[i]
    for i in range(len(words)):
        if words[i].upper() in column:
            print(column)
            print(f"{words[i]} vertical starts at {x+1},{y}")
        txt = f"{words[i]}"[::-1]
        if txt.upper() in column:
            print(column)
            print(f"{words[i]} vertical starts at {x+1},{0}")

wordsee = []
l=0
d=0

for line in file1:
    letter = line.rstrip().split(",")
    wordsee.append(letter)

for j in range(len(wordsee)):
    diagonal = []
    for i in range(len(wordsee)-l):
        diagonal.append(wordsee[i+l][i])
    l +=1
    diag = ""
    for i in range(len(diagonal)):
        diag = diag + diagonal[i]
    for i in range(len(words)):
        if words[i].upper() in diag:
            print(diag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")
        txt = f"{words[i]}"[::-1]
        if txt.upper() in diag:
            print(diag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")


for j in range(len(wordsee)):
    diagonal = []
    for i in range(len(wordsee)-l):
        diagonal.append(wordsee[i][i+d])
    d +=1
    diag = ""
    for i in range(len(diagonal)):
        diag = diag + diagonal[i]
    for i in range(len(words)):
        if words[i].upper() in diag:
            print(diag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")
        txt = f"{words[i]}"[::-1]
        if txt.upper() in diag:
            print(diag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")


z = 0

for j in range(len(wordsee)):
    b = 14
    biagonal = []
    for i in range(len(wordsee)-z):
        biagonal.append(wordsee[i][(b-z)-i])
    z += 1
    biag = ""
    for i in range(len(biagonal)):
        biag = biag + biagonal[i]
    for i in range(len(words)):
        if words[i].upper() in biag:
            print(biag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")
        txt = f"{words[i]}"[::-1]
        if txt.upper() in biag:
            print(biag)
            print(f"{words[i]} diagonial starts at {x+1},{0}")

y = 0

for j in range(len(wordsee)):
    b = 14
    biagonal = []
    for i in range(len(wordsee)-y):
        biagonal.append(wordsee[i+y][(b-z)-i])
    y += 1
    biag = ""
    for i in range(len(biagonal)):
        biag = biag + biagonal[i]
    for i in range(len(words)):
        if words[i].upper() in biag:
            print(biag)
            print(f"{words[i]} diagonial starts at {b+1},{0}")
        txt = f"{words[i]}"[::-1]
        if txt.upper() in biag:
            print(biag)
            print(f"{words[i]} diagonial starts at {b+1},{0}")