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
