#rechtschreibung ignorieren
#mehrere vorschläge
#synnonyme
#zacken schnell
#to lower case
#minimum ausgabe an items


#INPUTS
items = [["Cham", "23AcL-32"], ["Langenberg", "sd24-D3"], ["Bad Kötzting", "Sd23UU-2EE"]]
user_input = input("Search: ")


#CONFIGURATION
char_r = 5
char_f = -5


def search(items, score, input):
    return


def score(items, raw_input):
    input = raw_input.lower()

    for item in items:
        count = 0
        word = item[0].lower()
        input_check = ''

        for char in input.lower():
            input_check += char
            if input_check in word:
                count += char_r

        print(count)





score(items, user_input)
