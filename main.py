from preprocess import preprocess
from solve import solve

# ==== Assign the letters of the letterbox to the following constant.
# * Use exactly 12 letters, no spaces, no punctuation.
# * First the 3 letters of one letterbox edge (say, top edge), then the 3 letters of another edge, etc.
# * Letter case does not matter.
LETTERBOX = 'wcmhksobetai'


def main(letters):
    english_words_csv_path = preprocess()

    solutions = solve(english_words_csv_path=english_words_csv_path, letters=letters)
    print('\n===== SOLTUIONS ======')
    for sol in sorted(solutions):
        print(sol)


if __name__ == '__main__':
    main(letters=LETTERBOX)
