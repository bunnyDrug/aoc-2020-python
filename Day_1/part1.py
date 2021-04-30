def main():
    txt = open('input.txt').readlines()
    values = [(int(x) * int(y)) for x in txt for y in txt if int(x) + int(y) == 2020]
    result = values.pop()
    print(result)


main()
