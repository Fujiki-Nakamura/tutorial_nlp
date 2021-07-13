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
    plt.hist(freqs, bins=100)
    plt.savefig('./problem38.png')
