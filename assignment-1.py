#Section 1: Variables and Types
name = "Gianna"
age = 24
height = 163
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2: User Input and Math
user_name = input("What is your name? ")
user_yob = int(input("What year were you born in? "))
print(f'Hi {user_name}, you are approximately {2026-user_yob} years old.')

#Section 3: Type Conversion and f-strings
number_1 = float(input("Enter a number: "))
number_2 = float(input("Enter another number: "))
print(f'{number_1} x {number_2} = {number_1*number_2}')

#Section 4: Formatted Receipt
print("="*27)
print("        ", "RECEIPT")
print("="*27)

item = "Apple Juice"
price = .99
quantity = 3
total = round(price*quantity,2)
print(f'Item: {item}')
print(f'Price: {price}')
print(f'Quantity: {quantity}')

print("-"*27)
print(f'Total: {total}')
print("="*27)


#Section 5: Mini-Project -- Profile Card
user_name = input("What is your name? ")
hometown = input("What is your hometown? ")
hobby = input("What is your favorite hobby? ")
fun_fact= input("What is a fun fact about yourself? ")
user_yob = int(input("What year were you born in? "))

print("╔","═"*35,"╗")
print(" "*9, "PROFILE: ", user_name, " "*12)
print("╚","═"*35,"╝")

print(f'Hometown: {hometown}')
print(f'Hobby: {hobby}')
print(f'Fun fact: {fun_fact}')
print(f'Age: {2026-user_yob}')



