"""
Solver for the New York Times' Letter Boxed Daily Puzzle Game:
https://www.nytimes.com/puzzles/letter-boxed
"""


def _load_english_words(input_csv_path):
    """Load English words from a file."""
    with open(input_csv_path) as f:
        return {line.strip() for line in f.readlines()}


def _narrow_down(words, letters):
    """Narrow down to English words that consist only of the given letters, disregarding box edges."""
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
        t: (letters.lower().index(t) // 3)
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


def _find_single_word_solutions(eligible_words, letters):
    letters_set = set(letters.lower())
    single_word_solutions = {
        w for w in eligible_words
        if set(w) == letters_set
    }
    return single_word_solutions


def solve(english_words_csv_path, letters):
    assert len(letters) == 12 and len(set(letters)) == 12 and letters.isalpha()

    all_words = _load_english_words(input_csv_path=english_words_csv_path)
    narrowed = _narrow_down(all_words, letters)
    eligible = _eligible_words(narrowed, letters)

    single_word_solutions = _find_single_word_solutions(eligible, letters)
    two_word_solutions = _eligible_pairs(eligible, letters)

    return single_word_solutions | two_word_solutions
