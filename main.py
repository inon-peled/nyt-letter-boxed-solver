"""
Solver for the New York Times' Letter Boxed Daily Puzzle Game:
https://www.nytimes.com/puzzles/letter-boxed


List of English words was extracted from
https://dumps.wikimedia.org/enwiktionary/20231201/enwiktionary-20231201-pages-articles-multistream-index.txt.bz2
via
```cat ./enwiktionary-20231201-pages-articles-multistream-index.txt |
    cut -f3 -d: |
    grep -E '^[a-z]*$' >
    ./only_small_caps.csv
```
"""

LETTERBOX = 'WCMHKSOBETAI'


def _load_words():
    """Load words from a file."""
    with open('only_small_caps.csv') as f:
        return {line.strip() for line in f.readlines()}


def _narrow_down(words, letters):
    """Narrow down the list of words based on the letters."""
    letters_set = set(letters.lower())
    narrowed = {word for word in words if not (set(word) - letters_set)}
    return narrowed


def _is_eligible(word, edge_indexes):
    word_as_edge_indexes = [edge_indexes[t] for t in word]
    return all(
        word_as_edge_indexes[i] != word_as_edge_indexes[i + 1]
        for i in range(len(word) - 1)
    )


def _eligible_words(narrowed_down_words, letters):
    edge_indexes = {
        t: (letters.lower().index(t) // 4)
        for t in letters.lower()
    }
    eligible_words = {
        w for w in narrowed_down_words
        if _is_eligible(w, edge_indexes)
    }
    return eligible_words


def _eligible_pairs(eligible_words, letters):
    letters_set = set(letters.lower())
    eligible_pairs = {
        (w1, w2)
        for w1 in eligible_words
        for w2 in eligible_words
        if (w1[-1] == w2[0]) and (set(w1 + w2) == letters_set)
    }
    return eligible_pairs


if __name__ == '__main__':
    all_words = _load_words()
    narrowed = _narrow_down(all_words, LETTERBOX)
    eligible = _eligible_words(narrowed, LETTERBOX)
    eligible_pairs = _eligible_pairs(eligible, LETTERBOX)
    print(eligible_pairs)
