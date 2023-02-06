from time import sleep
def slow_print(text, delay):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

slow_print("Hello World!", 0.1)


def slowet(text):
    for letter in text:
        print(letter, end='', flush=True)
        sleep(0.11)
    print()

slowet("Hello brother, How are you doing, Welcome to the Matrix!")