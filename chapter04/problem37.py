from collections import defaultdict
import pprint
import matplotlib.pyplot as plt
import japanize_matplotlib

from problem30 import parse


pp = pprint.PrettyPrinter()


def calc_word_frequency_with_neko(parsed_sentences):
    counter = defaultdict(int)
    for sentence in parsed_sentences:
        if '猫' in [word['surface'] for word in sentence]:
            for word in sentence:
                if (word['pos'] not in ['記号', '助詞', '助動詞']) and (word['surface'] != '猫'):
                    counter[word['base']] = counter.get(word['base'], 0) + 1
    ret = sorted(
        [(word, freq) for word, freq in counter.items()],
        key=lambda e: e[1], reverse=True)
    return ret


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    word_freqs = calc_word_frequency_with_neko(parsed_sentences)
    words, freqs = [], []
    for word, freq in word_freqs[:10]:
        words.append(word)
        freqs.append(freq)

    plt.bar(x=range(len(freqs)), height=freqs, tick_label=words)
    plt.savefig('./problem37.png')
