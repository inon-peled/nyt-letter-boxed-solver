from solve import solve

LETTERBOX = 'trapkhnoeibw'

if __name__ == '__main__':
    solutions = solve(LETTERBOX)
    for sol in solutions:
        print(f'\n{sol}')
