user_input = input("Type your age: ")
user_input_type = type(user_input)
# print(user_input, user_input_type)
age = int(user_input)
age_type = type( age );
# print( age_type )

if(age == 20):
    print('You are 20')    
elif(age > 20):
    print('old')
else:
    print('young')

for(int i = 0; i < 10; i++){
    print (i);
}

for x in range(10):
    print (x)