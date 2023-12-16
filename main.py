from preprocess import preprocess
from solve import solve

LETTERBOX = 'wcmhksobetai'


def main(letters):
    english_words_csv_path = preprocess()

    solutions = solve(english_words_csv_path=english_words_csv_path, letters=letters)
    print('\n===== SOLTUIONS ======')
    for sol in sorted(solutions):
        print(sol)


if __name__ == '__main__':
    main(letters=LETTERBOX)
