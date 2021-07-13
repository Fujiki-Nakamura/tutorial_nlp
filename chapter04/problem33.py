import pprint

from problem30 import parse


pp = pprint.PrettyPrinter()


def get_A_no_B(parsed_sentences):
    rets = []  # sentence 単位で正しく抽出されていることを確認する用
    a_no_b = []
    for sentence in parsed_sentences:
        ret = []
        for i in range(1, len(sentence) - 1):
            word_prev = sentence[i - 1]
            word_curr = sentence[i]
            word_next = sentence[i + 1]
            if (word_prev['pos'] == '名詞') and (word_curr['surface'] == 'の') and (word_next['pos'] == '名詞'):
                ret.append(word_prev['surface'] +
                           word_curr['surface'] + word_next['surface'])
                a_no_b.append(
                    word_prev['surface'] + word_curr['surface'] + word_next['surface'])
        rets.append(ret)
    return a_no_b, rets


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    a_no_b, _ = get_A_no_B(parsed_sentences)
    # see examples
    pp.pprint(a_no_b[:20])
