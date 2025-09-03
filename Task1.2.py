def abc(x,th):
    x2=list(filter(lambda a:a>th,x))
    print(x2)

input_list=[1,5,10,3,8]   
threshold=5
abc(input_list,threshold)