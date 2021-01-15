#rechtschreibung ignorieren
#mehrere vorschläge
#synnonyme
#zacken schnell
#to lower case
#minimum ausgabe an items
#oe to ö

import time


#INPUTS
items = [["Cham", "23AcL-32"], ["Langenberg", "sd24-D3"], ["Bad Kötzting", "Sd23UU-2EE"], ["Chemnitz", "Sd23UU-2499sE"]]
user_input = input("Search: ")


#CONFIGURATION
char_r = 5
char_first = 7
word_comp = 1


def search(items, input, only_id, amount, fill_empty):
    score_list = score(items, input)
    output = []
    if amount > len(score_list):
        amount = len(score_list)

    if only_id:
        for index in range(amount):
            if (not fill_empty) & (score_list[index][2] == 0):
                break
            output.append(score_list[index][1])
    else:
        for index in range(amount):
            if (not fill_empty) & (score_list[index][2] == 0):
                break
            output.append(score_list[index])
    return output


def score(items, raw_input):
    input = raw_input.lower()
    new_list = []

    for item in items:
        count = 0
        count_1 = 0
        count_2 = 0
        word = item[0].lower()
        input_check = ''

        for char in input.lower():
            input_check += char

            #Phrase in word
            if input_check in word:
                count_1 = 0
                count_1 += char_r * len(input_check) + word_comp
                
                #TODO: split word on space and check first
                word_check_split = word.split()
                for i in word_check_split:
                    if i.find(input_check) == 0:
                        count_1 += char_first

            #Phrase without one char in word
            elif len(input_check) >= 3:
                for index in range(len(input_check)):
                    to_check = input_check[:index] + input_check[(index + 1):]
                    if to_check in word:
                        count_2 = 0
                        count_2 += char_r * len(input_check) - char_r

                        word_check_split = word.split()
                        for i in word_check_split:
                            if i.find(input_check) == 0:
                                count_2 += char_first

        if count_1 >= count_2:
            count = count_1
        else:
            count = count_2

        #Add count and sort list
        item.insert(2, count)
        if not new_list:
            new_list.append(item)
        else:
            lower_gap = count - new_list[0][2]
            higher_gap = new_list[-1][2] - count

            if lower_gap < 0:
                new_list.append(item)
            elif higher_gap < 0:
                new_list.insert(0, item)
            else:
                if lower_gap <= higher_gap:
                    for e in new_list:
                        if count <= e[2]:
                            new_list.insert(e[2], item)
                            break

                else:
                    for index, e in reversed(list(enumerate(new_list))):
                        if count >= e[2]:
                            new_list.insert(index + 1, item)
                            break

    return new_list





#start_time = time.time()

print(search(items, user_input, False, 3, True))

#print((time.time() - start_time), "seconds")