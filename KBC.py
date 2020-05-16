print('Hello, welcome to ABC')

ans = input('Are you ready to play (y/n): ')
score = 0
total_q = 10

if ans.lower() == 'y':
    ans = input("1. Who is India's first prime minister?(Surname only) ")
    if ans.lower() == 'nehru':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input("2. Who is Apple phone company founder's first name? ")
    if ans.lower() == 'steve':
        score += 1
        print('Correct')
    elif ans.lower() == 'ronald':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('3. When was state Telangana formed date and year? (Ex: 20May2010) ')
    if ans.lower() == '2june2014':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input("4. What is India's second capital? ")
    if ans.lower() == 'nagpur':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input('5. When was first world war started? (Ex: 20May2010) ')
    if ans.lower() == '28july1914':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

print('Thank you for playing, you got',score, "questions correct.")
mark  = (score/total_q) * 100

print("Your score is Marks:", str(mark) + '%')
print('goodbye')
















