movie_database = {
        "Action": ["Mad Max: Fury Road", "John Wick", "The Dark Knight"],
        "Comedy": ["Superbad", "The Grand Budapest Hotel", "The Hangover"],
        "Drama": ["The Shawshank Redemption", "Forrest Gump", "The Pursuit of Happyness"],
        "Romance": ["The Notebook", "Pride and Prejudice", "La La Land"],
        "Sci-Fi": ["Inception", "Interstellar", "The Matrix"],
        "Horror": ["The Conjuring", "Get Out", "A Quiet Place"],
    }

# name = input('Your name: ')
# gender = input('Your gender: ')
# age = int(input('Your age: '))

# genre = input('Your favorite genre: ')
# genre_Upper = genre.capitalize()

# if genre_Upper == 'Action':
#     print('gay')
# else:
#     print('nut')







# new_name = input('Type new name: ')

# names.append(new_name)
# print(names)

# first = int(input('Type first number: '))
# second = int(input('Type second number: '))

# print(names[first:second])





# names = ['Ali', 'Atay', 'Iman', 'Aidin', 'Aimonchock', 'Abai']



# print(len(names))

'''delete'''
# names.remove('Abai')
# deleted = names.pop(2)
# print(deleted)
# del names[0:2]
# names.clear()

'''add'''
# names.append('Alihan')
# names.insert(1, 'Aidar')
# names.extend(['Arsen', 'Aziret', 'Ali'])
# names += ['Aiza', 'Aisha', 'Faiza']


'''edit'''
# names[0], names[2] = names[-1], names[1]
# names[1] = 'Aspirin'
# names[1:3] = ['Cheloveck', 'Amogus']
# print(names)
# names.sort(reverse=True)
# print(names)





# names.append('Daniil')
# names.insert(2, 'Tolik')
# names.extend(['Barsbek', 'Ivan'])
# names += (['Arsen', 'Aziret'])    



# numbers = [1488, 23, 46, 18, 52, 69]
# numbers.sort
# print(numbers)
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))




# names = ['Ali', 'Iman', 'Aidin', 'Daniil']
# new_names = names.copy()

# new_names[1] = 'Atay'
# print(names)
# print(new_names)

# print(names == new_names)
# print(names is new_names)
# print(id(names))
# print(id(new_names))
# names.append('Tolik')
# print(names)
# print(names.count('Tolik'))




# eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,. ?!0123456789+-/*"
# rus = "йцукенгшщзхъфывапролджэячсмитьбю ?!0123456789+-/*"

# while True:
#     word = input('\n Type word: (exit)').lower()
#     if word == 'exit':
#         break
#     for i in word:
#         if i in rus:
#             print(eng[rus.index(i)], end='')
#         else:
#             print(rus[eng.index(i)], end='')




# print(eng.index('r'))




# days = ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun']
# expenses = []
# for day in days:
#     expenses.append(int(input(f'tag expenses for "{day.upper()}": ')))

# print('this is summ: ', sum(expenses))
# print('this is middle: ', sum(expenses) / (len(days)))






# asks = [1, 2, 3, 4, 5 ,6 ,7 ,8, 9 ,10]
# points = []

# for ask in asks:
#     points.append(int(input(f'type your balls for {ask} question: ')))
    
# print(sum(points))


# asks = 10
# max_points = 100

# answers = []

# for i in range(1, asks+1):
#     answers.append((i, int(input(f'Enter your points for {i} ask: '))))
   




'''циклы'''
# expenses = 0
# counter = 1

# while counter != 7+1:
#     print(expenses)
#     answer = input('Print expenses or "exit ')
#     if answer.isnumeric():
#         answer = int(answer)
#         expenses += answer
#     elif answer == 'exit':
#         print('exit...')
#         break 
#     else:
#         print('print number or exit')
#     counter += 1
# print('Here are your expenses:', expenses)
# print(expenses / counter)


# n = 5

# while n >= 0:
#     print(n)
#     n -= 1





# for number in range(1, 20):
#     print(number)


# counter = 0
# expenses = 0

# for day in range(1, 8):
#     print(counter)
#     counter += int(input(f'print expenses for {day} day or exit: '))
# print(counter)

# text = input('type text: ')
# number = int(input('Type a number: '))

# for number in range(1, number + 1):
#     print(text)

# while number > 0:
#     print(text)
#     number -= 1




# number = int(input('Напишите сколько раз будете вводить число: '))
# aboba = -1
# result = 0



# for numbers in range(number):
#     a = int(input('type: '))
#     aboba *= -1
#     result += aboba * number
# print(result)


# a = int(input())
# b = -1
# c = 0
# for i in range(a):
#     name = int(input())
#     b *= -1  
#     c += b * name
# print(c)

# expenses = 0
# counter = 1

# while counter != 7+1:
#     print(expenses)
#     answer = input('Print expenses or "exit ')
#     if answer.isnumeric():
#         answer = int(answer)
#         expenses += answer
#     elif answer == 'exit':
#         print('exit...')
#         break 
#     else:
#         print('print number or exit')
#     counter += 1
# print('Here are your expenses:', expenses)
# print(expenses / counter)



# number = int(input('НАпиши зайбал: '))
# for i in range (0, number + 1):
#     print(f'куб числа {i} равен {i**3}')



# n = int(input('Напиши зайбела: '))
# g = 1
# for i in range(1, n + 1):
#     g *= i 
# print(g)




# while True:
#     a = int(input())
#     if a == 0:
#         break
#     else:
#         print(a)

# while True:
#     a = input()
#     if a == ' ':
#         break
#     else:
#         print(a)    

# test = input('type text: ')
# number = int(input('type number: '))

# for i in range(number):
#     print(test)



# number = int(input())
# zvezda = '*'
# for i in range(number):
#     print(zvezda)
#     zvezda += '*'
    



# while True:
#     height = int(input())
#     if height == '!':
#         break
#     else:
#         height = int(input())
    
# if height < 190 and height > 150:
#     print(height)


# min_height = 150
# max_height = 180

# while True:
#     text = input('\n')
#     lines_count = text.count('\n') + 1
#     if text == 'Спасибо':
#         print(lines_count)
#     else:
#         text = input('\n')



student = {
    'name': 'Ali',
    'age': 15,
    'married': False,
    'Hobby': ['chess', 'gym', 'english']
}




'''add'''
# student['height'] = 1.80
# student["Hobby"].append('Basketball')
'''edit'''
# student["age"] += 1
# student["married"] = True
'''delete'''
# del student["name"]
# delete = student.pop('age')


# for i in student:
#     print(i, ':', student[i])


# print(student)