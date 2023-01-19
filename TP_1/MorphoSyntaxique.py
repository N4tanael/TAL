import nltk

nltk.download('averaged_perceptron_tagger')

with open('wsj_0010_sample.txt', 'r') as file:
    data = file.read().split('\n')
    

with open('wsj_0010_sample.txt.pos.nltk', 'w') as fp:
    space = False
    for d in data:
        if space:
            fp.write(" " + "	" + " " + "\n")
        else:
            space = True
        tokens = nltk.word_tokenize(d)
        tags = nltk.pos_tag(tokens)

        for item in tags:
            fp.write(item[0] + "	" + item[1] + "\n")

