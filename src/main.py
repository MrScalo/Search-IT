#rechtschreibung ignorieren
#mehrere vorschläge
#synnonyme
#zacken schnell
#to lower case
#minimum ausgabe an items
#oe to ö


#INPUTS
items = [["Cham", "23AcL-32"], ["Langenberg", "sd24-D3"], ["Bad Kötzting", "Sd23UU-2EE"]]
user_input = input("Search: ")


#CONFIGURATION
char_r = 5
char_first = 2


def search(items, input):
    print(score(items, input))
    


def score(items, raw_input):
    input = raw_input.lower()
    new_list = []

    for item in items:
        count = 0
        word = item[0].lower()
        input_check = ''

        for char in input.lower():
            input_check += char

            #Phrase in word
            if input_check in word:
                count += char_r
                if word[0] == input_check[0]:
                    count += char_first

            #Phrase without one char in word
            elif len(input_check) >= 3:
                for index in range(len(input_check)):
                    to_check = input_check[:index] + input_check[(index + 1):]
                    if to_check in word:
                        count += char_r

        #Add count and sort list
        item.insert(2, count)
        if not new_list:
            new_list.append(item)
        else:
            lower_gap = count - new_list[0][2]
            higher_gap = new_list[-1][2] - count

            if lower_gap <= 0:
                new_list.append(item)
            elif higher_gap <= 0:
                new_list.insert(0, item)
            else:
                if lower_gap <= higher_gap:
                    for index in new_list:
                        if count <= new_list[index][2]:
                            new_list.insert(index, item)
                            break

                else:
                    for index, e in reversed(list(enumerate(new_list))):
                        if count >= e[2]:
                            new_list.insert(index + 1, item)
                            break

    return new_list







search(items, user_input)

