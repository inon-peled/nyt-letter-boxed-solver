import os

from preprocess import preprocess
from solve import solve

LETTERBOX = 'trapkhnoeibw'


def main(letters):
    english_words_csv_path = preprocess()

    solutions = solve(english_words_csv_path=english_words_csv_path, letters=letters)
    for sol in solutions:
        print(f'\n{sol}')


if __name__ == '__main__':
    main(letters=LETTERBOX)
