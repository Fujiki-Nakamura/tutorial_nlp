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
    freqs = [freq for word, freq in word_freqs]
    plt.scatter(x=range(1, len(freqs) + 1), y=freqs)
    plt.xscale('log')
    plt.yscale('log')
    plt.savefig('./problem39.png')
