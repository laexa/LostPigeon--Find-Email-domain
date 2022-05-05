from guessemail import GuessEmail


def main():


    f = open('pigeon.txt', 'r')
    print(''.join([line for line in f]))

    print("__________________________________________________________________")
    print("Author: Martyna Mazur")
    print("https://github.com/laexa")
    print("__________________________________________________________________")



    check= input("Do you want to include email providers which can be no longer available ? Y/N")
    print("__________________________________________________________________")
    print("Find email domain ")


    email = input("Email:")
    print("_________________________________")
    GuessEmail(email,check.upper())
    print("_________________________________")





if __name__ == '__main__':
    main()