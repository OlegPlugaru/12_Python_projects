def really_smart_divider(x: int, y: int) -> None:
    try:
        num = x / y
        print(num)
    except ZeroDivisionError:
        print("Can't divide by zero! Use some other number")
    except TypeError:
        print("Both x & y needs to be numbers.")
    except Exception as e:
        print(f"Oops, something went wrong: {e}")

really_smart_divider(3, 0)
really_smart_divider(3, 4)
really_smart_divider(3, "a")

