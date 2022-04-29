from guessemail import GuessEmail
import Lista_clear
def main():


    f = open('pigeon.txt', 'r')
    print(''.join([line for line in f]))

    print("__________________________________________________________________")
    print("Author: Martyna Mazur")
    print("https://github.com/laexa")
    print("__________________________________________________________________")
    print(f"Current List containts {len(Lista_clear.domain_list)} checked domains")
    print("List with old and unchecked domains containts ",len(Lista_clear.mix_list))

    print("__________________________________________________________________")

    check= input("Do you want to include email providers which can be no longer availble ? Y/N")
    print("Find email domain ")


    email = input("Email:")
    print("_________________________________")
    GuessEmail(email,check.upper())
    print("_________________________________")



if __name__ == '__main__':
    main()