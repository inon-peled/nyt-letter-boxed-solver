from os import chdir

from preprocess import preprocess
from solve import solve


def test_solve_1():
    solutions = solve(english_words_csv_path='english_words.csv', letters='wcmhksobetai')

    assert solutions == {
        ('biochemist', 'thwack'),
        ('biochemist', 'tomahawk'),
        ('biochemist', 'tweak'),
        ('bisect', 'tomahawk')
    }


def test_solve_2():
    solutions = solve(english_words_csv_path='english_words.csv', letters='traeonwbihkp')

    assert solutions == {
        ('pawnbroker', 'rethink')
    }


def test_solve_3():
    word = 'stenographic'
    letter_boxed = ''
    for i in range(3):
        letter_boxed += word[i] + word[i + 3] + word[i + 6] + word[i + 9]

    solutions = solve(english_words_csv_path='english_words.csv', letters=letter_boxed)

    assert word in solutions


def test_preprocess():
    chdir('tests')
    save_path = 'test_preprocess_result.csv'

    preprocess(
        save_path=save_path,
        url='https://dumps.wikimedia.org/enwiktionary/20231201/enwiktionary-20231201-pages-articles-multistream-index.txt.bz2'
    )

    with open(save_path) as f_actual, open('expected_preprocess_result.csv') as f_expected:
        actual = set(line.strip() for line in f_actual)
        expected = set(line.strip() for line in f_expected)
        assert actual == expected
