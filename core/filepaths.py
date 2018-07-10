import sys

def get_filepath(file):
    print(sys.platform)
    if not sys.platform == "win32":
        return "../data/" + file
    else:
        return "..\\..\\data\\new\\"+ file
