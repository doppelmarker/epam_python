def checkline(line):
    try:
        return True if 3 > int(line) >= 1 else False
    except ValueError:
        raise ValueError("First line of file is not a number!")
