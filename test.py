from solve import solve


def test_solve_1():
    assert solve(english_words_csv_path='english_words.csv', letters='wcmhksobetai') == {
        ('biochemist', 'thwack'),
        ('biochemist', 'tomahawk'),
        ('biochemist', 'tweak'),
        ('bisect', 'tomahawk')
    }


def test_solve_2():
    assert solve(english_words_csv_path='english_words.csv', letters='traeonwbihkp') == {
        ('pawnbroker', 'rethink')
    }
