from file_read_backwards import FileReadBackwards


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


file = FileReadBackwards("file.txt")
pylines = grep("python", file)
print(list(pylines))
