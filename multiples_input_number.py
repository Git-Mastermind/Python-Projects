def multiples_of_input_number(number):
    multiples = []
    if number < 1 or number > 100:
        print('Invalid domain')
    else:
        for i in range(1,101):
            if i % number == 0:
                multiples.append(i)
        print(multiples)

#multiples_of_input_number(int(input('Enter a number between 1 and 100: ')))

def count_vowels(sentence):
    sentence = sentence.lower()
    input_sentence = list(sentence)
    vowels = []
    for i in range(len(sentence)):
        if input_sentence[i] == 'a' or input_sentence[i] == 'e' or input_sentence[i] == 'i' or input_sentence[i] == 'o' or input_sentence[i] == 'u':
            vowels.append(input_sentence[i])
    print(vowels)
    print(f'There are {len(vowels)} vowels')

#count_vowels('I eat apples')

def lucky_number_checker(number):
    digits_sum = 0
    for digit in str(number):
        digits_sum += int(digit)
    if digits_sum == 7:
        print('Lucky number!')
    else:
        print('Not so lucky...')

# lucky_number_checker(int(input('Enter a number: ')))

def password_strength_checker(input_password):
    password = list(input_password)
    has_letter = False
    has_digit = False
    for char in password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True
    if len(password) >= 8 and '!' in password or '@' in password or '#' in password and has_letter and has_digit:
        print('Strong Password!') 
    else:
        print('Weak Password')

# password_strength_checker(input('Enter a password: '))   

def task_manager():
    tasks = []
    options = print('''
    1: Add Task
    2: View Tasks
    3: Mark Task as Done
    4: Delete Task
    5: Quit''')
    print(options)
    options_choice = int(input('Choose one of the options: '))
    while options_choice != 5:
        options_choice = int(input('Choose one of the options: '))
        if options_choice == 1:
            add_task = input('What is the name of the task you would like to add? ')
            tasks.append(add_task)
        elif options_choice == 2:
            print(tasks)
        elif options_choice == 3:
            mark_as_done = int(input('At what index item would you like to mark as done(start with 0) '))
            tasks.remove(mark_as_done)
        elif options_choice == 4:
            delete_task = int(input('At what index item would you like to remove an item(start with 0) '))
            tasks.remove(delete_task)
        elif options_choice == 5:
            break

task_manager()