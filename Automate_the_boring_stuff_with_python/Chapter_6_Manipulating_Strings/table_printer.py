
def printTable(listData):
    
    colWidth = 0
    for i in range(len(listData)):
        for j in listData[i]:
            if (len(j)) > colWidth:
                colWidth = len(j)

    list1, list2, list3 = listData
    for i in range(len(list1)):
        print(f"{list1[i].rjust(colWidth, " ")} {list2[i].rjust(colWidth, " ")} {list3[i].rjust(colWidth, " ")}")
    
tableData = [["apples", "oranges", "cherries", "banana", "mangoes", "plums"],
             ["Alice", "Bob", "Carol", "David", "Brendan", "Alex"],
             ["dogs", "cats", "moose", "goose", "pig", "bird"]]


printTable(tableData)

 