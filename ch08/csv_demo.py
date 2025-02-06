import csv

if __name__ == "__main__":
    vil = [
        ['Doctor','No'],
        ['Rosa','Klebb'],
    ]

    path = 'F:\\Cache\\python\\ik.csv'
    with open(path,'wt') as fount:
        csvout = csv.writer(fount)
        csvout.writerows(vil)

    vil2 = []
    with open(path, 'rt') as fin:
        cin = csv.DictReader(fin, fieldnames= ['first', 'lase'])
        vil2 = [row for row in cin]

    print(vil2)
