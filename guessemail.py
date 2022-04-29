import sys

import Lista_clear

class GuessEmail:

    def __init__(self,email,chooice):
        self.choice = chooice
        self.email = self.clear_email(email)
        self.results = []
        self.filter = []
        self.hasz_res = []
        self.guess()
        self.anw = self.filtered()
        self.show()

    def action(self,match):
        action_save = input("Do you want save the guesses ? Y/N")
        if action_save.upper()== 'Y':
            self.save(match)


    def show(self):

        if len(self.filter) == 0 and len(self.results) ==0 :
            print("Unknown domain")

            if self.count_letters(self.check_ending(self.email)) == 0:

                check = input("Do you want to see simillar length domain ? Y/N")
                if check.upper() == 'Y':
                    matches = self.hasz_all()
                    if len(matches)==0:
                        print("No matches")
                    else:
                        print(*matches, sep="\n")
                        self.action(matches)
                else:
                    sys.exit()


        else:
            if len(self.filter ) > 0:
                print(f"Guesses found ({len(self.filter)}):",*self.filter,sep="\n")
                self.action(self.filter)
            else:
                print(f"Guesses found ({len(self.results)}):",*self.results,sep="\n")
                self.action(self.results)

    def hasz_all(self):
        for domain in Lista_clear.domain_list:
            # cz2 po kropce and
            if self.check_len_match(domain) == True and self.check_len_match_before(domain) == True:
                self.hasz_res.append(domain)
        return self.hasz_res



    def check(self,text):
        letter_count = 0
        for letter in text:
            if letter.isalpha() == True or letter =="-":
                letter_count +=1
            else:
                break
        return letter_count


    def guess(self):

        if self.choice == 'Y':
            for domain in Lista_clear.mix_list:
                if len(domain) == len(self.email) and domain[0] == self.email[0]:
                    if self.check_len_match(domain) == True:
                        self.results.append(domain)

        else:
            for domain in Lista_clear.domain_list:
                if len(domain) == len(self.email) and domain[0] == self.email[0]:
                    if self.check_len_match(domain) == True:
                        self.results.append(domain)

    def filtered(self):
        ver = self.check_ending(self.email)
        #number of letters

        ver1 = self.count_letters(ver)
        dl = len(self.email)

        #jesli nie ma zadnych liter po kropce
        if ver1 ==0 :
            return False

        #jesli jest 1 litera
        if ver1 == 1:
            for domain in self.results:
                v = self.check_ending(domain)
                if ver[0] == v[0]:
                    self.filter.append(domain)

                # jesli jest 1 litera

        #jeslisa 2 litery
        if ver1 == 2:
            for domain in self.results:
                v = self.check_ending(domain)
                if ver[0] == v[0] and ver[1]==v[1]:
                    self.filter.append(domain)

        #jesli koncowka jest cala w literach
        if ver1 == len(ver):
            for domain in self.results:
                v = self.check_ending(domain)
                if ver == v:
                    self.filter.append(domain)


    def check_len_match(self,domain):
        end1 = self.check_ending(domain)
        end2 = self.check_ending(self.email)

        if len(end1) == len(end2):
            return True

    def check_len_match_before(self,domain):
        end1 = self.clear_email(domain)
        end2 = self.clear_email(self.email)

        if len(end1) == len(end2):
            return True

    def check_first_letter(self,domain):
        end1 = self.check_ending(domain)
        end2 = self.check_ending(self.email)

        if end2[0] != '#':
            if end1[0]==end2[1]:
                return True
            else:
                return False
        else:
            return False

    def check_ending(self,domain):
        indeks = domain.find(".")
        text2 = domain[indeks + 1::]
        return text2

    def clear_email(self,email):
        indeks = email.find("@")
        text2 = email[indeks + 1::]
        return text2

    def count_letters(self,ending):
        count = 0
        for letter in ending:
            if letter.isalpha() == True or letter.isalnum() == True:
                count += 1
        return count

    def save(self,result):
        with open(f"{self.email}.txt",'w') as f:
            for domain in result:
                f.writelines(domain +'\n')
