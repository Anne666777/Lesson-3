my_sum = 0
fin = False
while not fin:
    my_num = input("Enter the numbers separated by a space. To exit, press 'Q': ")
    my_list = my_num.split()
    for elem in my_list:
        if elem == 'Q':
            fin = True
            break
        else:
            my_sum += float(elem)
    print('Received sum:', my_sum)
