import matplotlib.pyplot as plt
import japanize_matplotlib

from problem30 import parse
from problem35 import calc_word_frequency


if __name__ == '__main__':
    filename = 'neko.txt.mecab'
    with open(filename, 'r') as f:
        data = f.read()

    parsed_sentences = parse(data)
    word_freqs = calc_word_frequency(parsed_sentences)
    word_freqs_top10 = word_freqs[:10]
    words, freqs = [], []
    for word, freq in word_freqs_top10:
        words.append(word)
        freqs.append(freq)
    plt.bar(x=range(len(freqs)), height=freqs, tick_label=words)
    plt.savefig('./problem36.png')
