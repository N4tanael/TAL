import nltk

with open('POSTags_PTB_Universal_Linux.txt', 'r') as file:
    data = [tuple(line.split()) for line in file]

with open('wsj_0010_sample.txt.pos.nltk', 'r') as fr:

    newlines = ""

    for line in fr:
        myline = line.split()
        if len(myline)==0:
            continue
        for (i,j) in data:
            if myline[1]==i:
                myline[1]=j
        newlines += myline[0] + "   " + myline[1] + "\n"
        
                


with open('wsj_0010_sample.txt.pos.univ.nltk', 'w') as fw:
    fw.write(newlines)


with open('wsj_0010_sample.pos.ref', 'r') as fr:

    newlines = ""
    for line in fr:
        myline = line.split()
        if len(myline)==0:
            continue
        for (i,j) in data:
            if myline[1]==i:
                myline[1]=j
        newlines += myline[0] + "   " + myline[1] + "\n"

with open('wsj_0010_sample.txt.pos.univ.ref', 'w') as fw:
    fw.write(newlines)
