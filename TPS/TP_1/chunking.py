import nltk
from nltk import RegexpParser
import chunks
import sys

nltk.download('averaged_perceptron_tagger')

with open('wsj_0010_sample.txt', 'r') as fr:
    data = fr.read().split('\n')
    

with open('wsj_0010_sample.txt.chk.nltk','w') as fw:

    pattern = chunks.patterns[sys.argv[1]]
    chunker = RegexpParser(pattern)

    for d in data:

        tokens = nltk.word_tokenize(d)
        tags = nltk.pos_tag(tokens)
        output = chunker.parse(tags)
            
        for i in output:
            if not isinstance(i,tuple):
                for j in i:
                    fw.write(j[0] + " " + j[1] + "    ")
                fw.write("\n")
