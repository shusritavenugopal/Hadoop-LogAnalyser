import sys
import re
from collections import defaultdict

def generate_ngrams(text, n):
    # Generate n-grams
    ngrams = [text[i:i+n] for i in range(len(text) - n + 1)]
    return ngrams

def mapper():
    ngram_counts = defaultdict(int)
    for line in sys.stdin:
        line = line.strip()
        ngrams = generate_ngrams(line, int(sys.argv[1]))
        for ngram in ngrams:
            ngram_counts[ngram] += 1
    for ngram, count in ngram_counts.items():
        print('%s\t%s' % (ngram, count))

if __name__ == "__main__":
    mapper()

