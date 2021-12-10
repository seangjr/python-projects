def num_name():
    """
    numberpad = {
        0 : '',
        1 : '',
        2 : 'ABC',
        3 : 'DEF',
        4 : 'HGI',
        5 : 'JKL',
        6 : 'MNO',
        7 : 'QRS',
        8 : 'TUV',
        9 : 'WXYZ',
    }
    ^^ old object data structure
    """

    """
    basically this part below is the nested list data structure

    how to access the data in a nested list is basically like this:

        foo = [
            [bar1, bar2],
            [bar3, bar4],
        ]

        bar1 = foo[0][0]
        bar2 = foo[0][1]
        bar3 = foo[1][0]
        bar4 = foo[1][1]

        if you manage to catch on the pattern, the first index (foo ->[]<-[])
        selects the inner list

        foo = [
            ->[bar1, bar2]<- ,
            [bar3, bar4]
        ]

        the second index (foo[]->[]<-) selects the item in the inner list

        foo = [
            [->bar1<-, bar2],
            [...]
        ]

        hope this comment makes sense :P
    """
    numberpad_arr = [
        [''],
        [''],
        ['ABC'],
        ['DEF'],
        ['HGI'],
        ['JKL'],
        ['MNO'],
        ['QRS'],
        ['TUV'],
        ['WXYZ']
    ]
    

    numberInput = input("Enter Number : ")
    numberInput = [int(i) for i in numberInput]

    result = ['']
    boolValue = True
    for x in numberInput:
        if (x == 1 or x == 0 or len(numberInput) != 8):
            boolValue = False
            print("Invalid phone number for words")
            break
        else:
            letters = numberpad_arr[x][0]
            result = [prefix + letter for prefix in result for letter in letters]
    if(boolValue == True):
        return print(*result,sep='\n')

num_name()
