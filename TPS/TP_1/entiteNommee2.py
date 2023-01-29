import nltk
import replace
import sys
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

filename = sys.argv[1]

with open(filename, 'r') as fr:
    data = fr.read().split('\n')
    

with open(filename + '.ne.nltk', 'w') as fw:
    for d in data:
        tokens = nltk.word_tokenize(d)
        tags = nltk.pos_tag(tokens)
        namedEnt = nltk.ne_chunk(tags, binary=False)

        for i in namedEnt:
            if not isinstance(i,tuple):
                Ent = str(i).replace("(","").replace(")","") + "\n"
                fw.write(replace.replaceTokens(Ent))
