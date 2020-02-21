import math

book,lib,deadline=list(map(int,input().split()))

score_list=list(map(int,input().split()))

#dict of scores
d=dict()
for x in range(len(score_list)):
    d[x]=score_list[x]

#greedy ratio is based on (no. of books)/(ship of book)-sign_up_day
ratio_greedy=[]

#library params
book_in_library=[]
sign_up_publish=[]
ship_book=[]
books=[]
id=[]

count_libraries=0

#We have taken the input
for x in range(lib):
    book_lib,sign_up,ship=list(map(int,input().split()))

    if sign_up>=deadline: #then ignore library
        continue
    else:
        #create ratio based on ratio_greedy
        ratio_greedy.append(book_lib/ship-sign_up)
        #store book of library in that index
        book_in_library.append(input().split())
        id.append(x)
        books.append(book_lib)
        ship_book.append(ship)
        sign_up_publish.append(sign_up)
        count_libraries+=1

#printing the library count
print(count_libraries)


for x in range(count_libraries):

    min_val=0
    pos=0
    for y in range(1,len(sign_up_publish)):
        get_val=sign_up_publish[y]
        if get_val==min_val:
            if ratio_greedy[y]>ratio_greedy[pos]:
                min_val=get_val
                pos=y
        if get_val<min_val:
            min_val=get_val
            pos=y


    print(id[pos],' ',len(book_in_library[pos]))
    print(' '.join(book_in_library[pos]))

    #perform deletions on that position
    del(id[pos])
    del(book_in_library[pos])
    del(ship_book[pos])
    del(books[pos])
    del(sign_up_publish[pos])
    del(ratio_greedy[pos])
