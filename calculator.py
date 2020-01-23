ans = input('Hello! Are you here for calculating?(y/n): ')

if ans == 'y':
     num1 = int(input('Input 1st number: '))
     method = input("Input symbol +,*,-,/ : ")
     num2 = int(input('Input 2nd number: '))

     if (method == '+'):
          ans1 = num1 + num2
     elif (method == '-'):
          ans1 = num1 - num2
     elif (method == '*'):
          ans1 = num1 * num2
     elif (method == '/'):
          ans1 = num1 / num2
     print('Your Answer is =', ans1)

elif ans == 'n':
     print("Oh, you're not going ahead... OK.")
     quit()



