import sys
import re

class GuessEmail:

    def __init__(self,email,choice):
        self.choice = choice
        self.provider_list = []
        self.full_list = []
        self.g_results = []

        self.email = self.clear_email(self.action_input_check(email))


        self.email_end = self.check_ending(self.email)
        self.email_end_l = len(self.email_end)
        self.end_letter_amount = self.count_letters(self.email_end)
        self.email_dom = self.clear_email(self.email)


        self.d = self.split_half(self.email_dom)
        self.d = self.only_letters(self.d)



        self.e = self.split_half(self.email_end)
        self.e = self.only_letters(self.e)


        self.email_letter = self.only_letters(self.d)
        self.email_dom_l = len(self.email_dom)
        self.endd_letter_amount = self.count_letters(self.d)
        self.end_letter = self.only_letters(self.e)


        self.open()
        self.check_matches()
        self.results()


    def results(self):
        if len(self.g_results)==0:
            print("Unknown domain")

        else:
            print(f"Guesses found ({len(self.g_results)}):",*self.g_results, sep="\n")
            anwser = input("Do you want to save results ? Y/N")

            if anwser.upper() =='Y':
                self.save(self.g_results)
            else:
                sys.exit()


    def choice_act(self):
        if self.choice =='Y':
            return self.full_list
        else:
            return self.provider_list

    def check_matches(self):



        for provider in self.choice_act():

            provider_dom = provider
            provider_dom_l = len(provider_dom)
            provider_end = self.check_ending(provider)
            provider_end_l = len(provider_end)


            #spr czy dlugosc poczatku i konca jest taka sama w obu
            if self.email_dom_l == provider_dom_l and self.email_end_l == provider_end_l:

                #gdy nie ma zadnej litery
                if self.endd_letter_amount == 0 and self.end_letter_amount == 0:
                    self.g_results.append(provider)


                #gdy litera w provider ale nie w end
                if self.endd_letter_amount > 0 and self.end_letter_amount == 0:
                    if provider_dom.startswith(self.d) == True:
                        self.g_results.append(provider)


                # nie ma litery w provider ale jest w end
                if self.endd_letter_amount == 0 and self.end_letter_amount > 0:
                    if provider_end.startswith(self.end_letter) == True:
                        self.g_results.append(provider)


                #litery w obu
                if self.endd_letter_amount > 0 and self.end_letter_amount > 0:
                    if provider_end.startswith(self.end_letter) == True and provider_dom.startswith(self.email_letter) == True:
                        self.g_results.append(provider)





    def only_letters(self,dom):
        index= dom.split('#',1)
        k= index[0]
        return k

    def action(self,match):
        action_save = input("Do you want save the guesses ? Y/N")
        if action_save.upper()== 'Y':
            self.save(match)


    def action_input_check(self,email):
        regex = '[A-Za-z0-9._%#+-]+@[A-Za-z0-9#.-]+\.[A-Za-z#]'
        while True:
            if re.search(regex,email):
                return email
            else:
                print("Incorrect email. ")
                email = input("Email:")


    def check_ending(self,domain):


        rev = domain[::-1]
        end =  rev.split('.')
        txt = end[0]
        return txt[::-1]


    def clear_email(self,email):

        indeks = email.find("@")
        text2 = email[indeks + 1::]
        return text2

    def split_half(self,email):

        dom = email.split('.')
        txt = dom[0]
        return txt


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

    def open(self):
        with open('avaibledomains.txt', 'r') as fl:
            domain_list = fl.read().split("\n")
            self.provider_list = domain_list


        # Credits to https://gist.github.co/tbrianjones
        # https://gist.github.com/tbrianjones/5992856/87f527af7bdd21997722fa65143a9af7bee92583
        with open('mixdomclear.txt', 'r') as fl:
            mix_list = fl.read().split("\n")
            self.full_list= mix_list


