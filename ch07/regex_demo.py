import re

if __name__ == "__main__":
    result = re.match('.*Fran', "You Franmk")
    if result:
        print(result.group())
