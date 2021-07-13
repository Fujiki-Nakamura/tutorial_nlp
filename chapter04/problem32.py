import pprint

from problem30 import parse


pp = pprint.PrettyPrinter()


def get_verb_bases(parsed_sentences):
    verb_bases = []
    for sentence in parsed_sentences:
        for word in sentence:
            if word['pos'] == '動詞':
                verb_bases.append(word['base'])
    return verb_bases


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    verb_bases = get_verb_bases(parsed_sentences)
    # see examples
    pp.pprint(verb_bases[:20])
