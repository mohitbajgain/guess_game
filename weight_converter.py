# # Weight Converter
while True:
    weight= int(input('Please enter your weight:'))
    unit= input('Enter K for kg(s) or L for Lb(s):')

    
    if unit.upper()=='K':
        converted= weight/0.45
        print(f'you can {converted} pounds')
    elif unit.upper()=='L':
        converted=weight*0.45
        print('You are ',converted,'kilos')
    else:
        print('I had told (k) for kg or (L) for Lbs')
        print('\n')



    


    