


if __name__ == "__main__":
    poem = '''Whose Speed was far faster than light;'''

    f = open("F:\\Cache\\python\\a.txt",'r')
    while True:
        frag = f.read(2)
        if not frag:
            break
        print(frag)
    f.close()

    print("==========")