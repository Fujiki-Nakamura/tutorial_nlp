import pprint


pp = pprint.PrettyPrinter()


def parse(data):
    sentences = data.split('EOS')
    parsed_sentences = []
    for sentence in sentences:
        words = sentence.split('\n')
        parsed_sentence = []
        for word in words:
            if word == '':
                continue
            surface, others = word.split('\t')
            if surface in ['', '\u3000']:
                continue
            others = others.split(',')
            d = {
                'surface': surface,
                'base': others[6],
                'pos': others[0],
                'pos1': others[1],
            }
            parsed_sentence.append(d)
        parsed_sentences.append(parsed_sentence) # parsed_sentence != []の時のみappendの方がいいかも？

    return parsed_sentences


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    # see examples
    pp.pprint(parsed_sentences[3])
    pp.pprint(parsed_sentences[5])
