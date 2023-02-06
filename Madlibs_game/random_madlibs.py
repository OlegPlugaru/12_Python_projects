import madlibs, starwars, magic_computers, hobbyLark, Matrix
import random

if __name__ == "__main__":
    m = random.choice([magic_computers, madlibs, starwars, hobbyLark, Matrix])
    m.madlib()
    input()