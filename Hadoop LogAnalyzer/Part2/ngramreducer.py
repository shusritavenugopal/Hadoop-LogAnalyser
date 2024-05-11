import sys

def reducer():
    current_ngram = None
    current_count = 0

    for line in sys.stdin:
        ngram, count = line.strip().split('\t')
        count = int(count)

        if ngram == current_ngram:
            current_count += count
        else:
            if current_ngram:
                print('%s\t%s' % (current_ngram, current_count))
            current_ngram = ngram
            current_count = count

    if current_ngram:
        print('%s\t%s' % (current_ngram, current_count))

if __name__ == "__main__":
    reducer()
