import pprint

from problem30 import parse


pp = pprint.PrettyPrinter()


def get_noun_concat(parsed_sentences):
    rets = []  # sentence 単位で正しく抽出されていることを確認する用
    noun_concats = []
    for sentence in parsed_sentences[:70]:
        ret = []
        nouns = ''
        cnt = 0
        for word in sentence:
            if word['pos'] == '名詞':
                nouns = nouns + word['surface'] # `nouns += word['surface']` で良い
                cnt += 1
            else:
                if cnt >= 2:
                    ret.append(nouns)
                    noun_concats.append(nouns)
                    nouns = ''
                    cnt = 0
                else:
                    nouns = ''
                    cnt = 0
        rets.append(ret)
    return noun_concats


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    noun_concats = get_noun_concat(parsed_sentences)
    # see examples
    pp.pprint(noun_concats[:20])
