import unicodedata

def unicode_test(value):
    name = unicodedata.name(value)
    values2 = unicodedata.lookup(name)
    print('values = "%s", name = "%s"， value2 = "%s"' % (value, name, values2));


if __name__ == "__main__":
    unicode_test('A')
    unicode_test('$')
    unicode_test('你')
    unicode_test('\u2603')