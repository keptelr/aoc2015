
def read(day: str):
    file = open("resources/" + day + ".txt", "r")
    lines = file.read()
    file.close()
    return lines
