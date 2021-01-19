#EXAMPLE DATA
example_items = [["Germany", "23AcL-32"], ["France", "sd24-D3"], ["England", "Sd23UU-2EE"], ["Italy", "bo23r-2499sE"], ["Spain", "S2HleUU-as3sE"]]
example_input = "Fra"


class Search_it:
    def __init__(self, items, inputs):
        self.items = items
        self.inputs = inputs

    #Standart variables
    only_id = False
    amount = 5
    fill_empty = False

    #CONFIGURATION
    __char_r = 5
    __char_first = 7
    __word_comp = 1
    __umlauts = [['oe', 'ue', 'ae', 'ss'], ['ö', 'ü', 'ä', 'ß']]

    def search(self):
        score_list = self.__score()
        output = []
        if self.amount > len(score_list):
            self.amount = len(score_list)

        if self.only_id:
            for index in range(self.amount):
                if (not self.fill_empty) & (score_list[index][2] == 0):
                    break
                output.append(score_list[index][1])
        else:
            for index in range(self.amount):
                if (not self.fill_empty) & (score_list[index][2] == 0):
                    break
                output.append(score_list[index])
        return output


    def __score(self):
        inputs = self.inputs.lower()
        inputs = self.__remove_umlauts(inputs)

        new_list = []

        for item in self.items:
            count = 0
            count_1 = 0
            count_2 = 0
            input_check = ''
            word_possible = True
            word = item[0].lower()
            
            word = self.__remove_umlauts(word)

            for char in inputs.lower():
                if word_possible:
                    input_check += char

                    #Phrase in word
                    if input_check in word:
                        count_1 = 0
                        count_1 += self.__char_r * len(input_check) + self.__word_comp
                            
                        #Split word on space and check first char
                        word_check_split = word.split()
                        i = 0
                        for e in word_check_split:
                            if e.find(input_check) == 0:
                                count_1 += self.__char_first
                                if i == 0:
                                    count_1 += 1
                            i += 1

                    #Phrase without one char in word
                    elif len(input_check) >= 3:
                        for index in range(len(input_check)):
                            to_check = input_check[:index] + input_check[(index + 1):]
                            if to_check in word:
                                count_2 = 0
                                count_2 += self.__char_r * len(input_check) - self.__char_r

                                #Split word on space and check first char
                                word_check_split = word.split()
                                i = 0
                                for e in word_check_split:
                                    if e.find(input_check) == 0:
                                        count_1 += self.__char_first
                                    if i == 0:
                                        count_1 += 1
                                    i += 1
                            else:
                                word_possible = False
                    else:
                        word_possible = False

            if count_1 >= count_2:
                count = count_1
            else:
                count = count_2


            #Add item to new_list and sort it
            item.insert(2, count)
            new_list.append(item)
        def takeCount(elem):
            return elem[2]
        new_list.sort(key=takeCount, reverse=True)

        return new_list


    def __remove_umlauts(self, word):
        i = 0
        for u in self.__umlauts[0]:
            if u in word:
                word = word.replace(u, self.__umlauts[1][i])
            i +=1
        return word
