#test for function
#def first_function(a,b,c):
#    a=a+c;
#    b=a-c;
#    print(a,b,c);

def sale_car(price,colour='red',brand='camry',is_second_hand=True,length=4000,hight=2000):
    print('price:',price,
        'colour:',colour,
        'brand:',brand,
        'is_second_hand:',is_second_hand,
        'length:',length,
        'hight:',hight)
    return length+hight
print(sale_car(1000))

