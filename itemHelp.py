import resetScreen


def item_help():
    resetScreen.reset_screen(True)
    print("Each item is defined by three properties. Number of containers, groups and uses. Eg. for tomatoes, \n"
          "one \"container\" is one \"box\" of tomatoes and therefore the unit name is \"box(es)\". Inside of \n"
          "each \"box\" there are sub-groups of items known as \"groups\". One \"tomato\" is equal to one \n"
          "group of tomatoes therefore the unit is \"tomato(es)\". This is because we subdivide tomatoes even \n"
          "further. each group of tomatoes / each tomato includes several \"uses\" (ie tomato slices, but the \n"
          "program does not care or need to know what this is called). Sometimes this number is to be approximated. \n"
          "For lettuce for example, we assume that each box of lettuce includes 8 bags(always true), and that each \n"
          "bag of lettuce includes 200 units of lettuce(approximated). You will also be asked how many uses are in \n"
          "one group, and how many groups are in one container for your specific item. The system tracks each item \n"
          "by the number of groups because it is the smallest unit besides uses(and it assumes there is no \n"
          "individual \"uses\" of an item laying around intended to be used(ie. a single chicken nugget))\n")
    input("Press enter to continue. ")
