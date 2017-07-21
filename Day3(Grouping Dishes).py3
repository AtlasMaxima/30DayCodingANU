dishe1 = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
          ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
          ["Quesadilla", "Chicken", "Cheese", "Sauce"],
          ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

dishe2 = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
            ["Chicken Curry", "Chicken", "Curry Sauce"],
            ["Fried Rice", "Rice", "Onions", "Nuts"],
            ["Salad", "Spinach", "Nuts"],
            ["Sandwich", "Cheese", "Bread"],
            ["Quesadilla", "Chicken", "Cheese"]]


def grouping_dishes(dishes):
    bighashtablelist = []
    bighashtable = {}
    for index, dish in enumerate(dishes):
        hashtable = {}
        dish_name = dish[0]
        for ingred in dish[1:]:
            if ingred not in hashtable:
                hashtable[ingred] = 1
            else:
                hashtable[ingred] += 1
        bighashtable[dish_name] = hashtable

        bighashtablelist.append(bighashtable[dish_name])

    biganswerlist = []

    for dish in dishes:
        dish_name = dish[0]
        for ingred in dish[1:]:
            #print(ingred.upper())
            inneranswerlist = []
            inneranswerlist.append(ingred)
            for key, value in bighashtable.items():
                #print("Key:", key, ", Value:", value)
                if ingred in value:
                    #print(ingred.upper(), "in", value, "and the dish name is ", key.upper())
                    inneranswerlist.append(key)
            if len(inneranswerlist) > 2:
                # print()
                # print(inneranswerlist)
                biganswerlist.append(inneranswerlist)
        #         print()
        # print()

    # print("BIGLIST:", biganswerlist)
    new_k = []
    for ele in biganswerlist:
        if ele not in new_k:
            new_k.append(ele)
    biganswerlist = new_k

    answerbiglist = []
    biganswerlist.sort()
    for list in biganswerlist:
        dish_name = list[0]
        # print(list)
        ingredlist = list[1:]
        ingredlist.sort()
        # print("dish name:", list[0], ingredlist)
        ingredlist.insert(0, dish_name)
        new_list = ingredlist[:]
        answerbiglist.append(new_list)
    return answerbiglist

print(grouping_dishes(dishe2))

