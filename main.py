"""
1. Assign the letters of the letterbox to LETTERBOX below.
    * Use exactly 12 letters, no spaces, no punctuation.
    * First the 3 letters of one letterbox edge (say, the top edge), then the 3 letters of another edge, etc.
    * Letter case and the order of letters of the same edge do not matter.
2. Run this script.
"""
# For example, the following letters correspond to the letterbox in `example.png`.
LETTERBOX = 'wcmhksobetai'

from preprocess import preprocess
from solve import solve


def main(letters):
    english_words_csv_path = preprocess()

    solutions = solve(english_words_csv_path=english_words_csv_path, letters=letters)
    print('\n===== SOLTUIONS ======')
    for sol in sorted(solutions):
        print(sol)


if __name__ == '__main__':
    main(letters=LETTERBOX)
