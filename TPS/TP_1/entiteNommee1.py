import nltk
import replace
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


with open('wsj_0010_sample.txt', 'r') as file:
    data = file.read().split('\n')
    

with open('wsj_0010_sample.txt.ne.nltk', 'w') as fp:
    for d in data:
        tokens = nltk.word_tokenize(d)
        tags = nltk.pos_tag(tokens)
        namedEnt = nltk.ne_chunk(tags, binary=False)

        for i in namedEnt:
            if not isinstance(i,tuple):
                Ent = str(i).replace("(","").replace(")","") + "\n"
                fp.write(replace.replaceTokens(Ent))




    

