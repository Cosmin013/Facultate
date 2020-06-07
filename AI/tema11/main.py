from nltk.corpus import wordnet


def find_hypernym(word):
    out = ''
    syn = wordnet.synsets(word)
    if syn:
        for item in syn:
            if item.lemmas()[0].name() == word.lower() and item.pos() == 'n':
                if item.hypernyms():
                    out = out + item.hypernyms()[0].lemmas()[0].name() + ' '
                break
        else:
            out = out + word + ' '
    else:
        out = out + word + ' '

    return out


def words(path):
    out = ''
    content = ''
    with open(path, 'r') as f:
        for line in f:
            content += line.rstrip() + ' '

    for sentence in content.split('.'):
        if sentence != ' ':
            distances = list()
            for word1 in sentence.split():
                for word2 in sentence.split():
                    if word1[-1] in "',;-_":
                        word1 = word1[:-1]
                    if word2[-1] in "',;-_":
                        word2 = word2[:-1]
                    syn1 = wordnet.synsets(word1)
                    syn2 = wordnet.synsets(word2)
                    if syn1 and syn2:
                        distances.append(syn1[0].shortest_path_distance(syn2[0]))

            for word in sentence.split():
                out += find_hypernym(word)
            out = out[:-1] + '.' + str(max([i for i in distances if i is not None])) + ' '

    f.close()
    f = open(path, 'w')
    f.write(out)


if __name__ == "__main__":
    words('words.txt')
