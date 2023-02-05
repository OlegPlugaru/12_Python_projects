import madlibs, starwars, magic_computers, hobbyLark
import random

if __name__ == "__main__":
    m = random.choice([magic_computers, madlibs, starwars, hobbyLark])
    m.madlib()