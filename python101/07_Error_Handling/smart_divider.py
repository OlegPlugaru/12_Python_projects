def smart_divider(x: int, y: int) -> None:
    try:
        # code 
        num = x / y
    except ZeroDivisionError: # specific error:
        # do error
        print("Can't divide by zero! Use some other number")


smart_divider(4, 5)