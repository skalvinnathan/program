#high level loop 100   loop with 100 loop inside and 100 loop inside that
#and print the result       
i=0
while i<100:
    j=0
    while j<100:
        k=0
        while k<100:
            print(i,j,k)
            k=k+1
        j=j+1
    i=i+1

