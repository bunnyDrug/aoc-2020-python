def main():
    txt = open('input.txt').readlines()
    values = [(int(x) * int(y) * int(z))
              for x in txt
              for y in txt
              for z in txt
              if int(x) + int(y) + int(z) == 2020]
    result = values.pop()
    print(result)


main()
