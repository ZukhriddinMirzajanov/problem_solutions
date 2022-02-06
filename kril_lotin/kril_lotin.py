import letters

letters = letters.letters


b = input("Kril so'z kirgazing: ")


def kril_lotin(b):
    a = """"""
    for i in b:
        for j in letters:
            if i == j:
                a += letters[j]
    print(a)
    f = open("text.txt", "w")
    f.write(a)
    f.close()


kril_lotin(b)
