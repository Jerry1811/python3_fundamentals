age = int(input('How old are you?\n'))

decades = age // 10
years = decades % 10

print('You are ' + str(decades) + " decades and " + str(years) + ' years old.')
