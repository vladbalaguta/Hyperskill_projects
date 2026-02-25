M = 0.0

while True:
    print('Enter an equation')
    equation = input().split()

    if len(equation) != 3:
        print("Invalid format. Use: number operator number")
        continue

    try:
        if equation[0] == 'M':
            equation[0] = M
        if equation[2] == 'M':
            equation[2] = M

        a = float(equation[0])
        b = float(equation[2])
    except ValueError:
        print('Do you even know what numbers are? Stay focused!')
        continue

    operator = equation[1]
    result = 0
    msg = ''
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
    messages = {
        10: msg_10,
        11: msg_11,
        12: msg_12
    }

    if a.is_integer() and a in range(-10, 11) and b.is_integer() and b in range(-10, 11):
        msg += msg_6
    if (a == 1 or b == 1) and operator == '*':
        msg += msg_7
    if (a == 0 or b == 0) and (operator == '*' or operator == '-' or operator == '+'):
        msg += msg_8
    if operator not in ['+', '-', '*', '/']:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue

    if operator == '+':
        result = a + b
        if msg != '':
            msg = msg_9 + msg
            print(msg)
        print(result)
    elif operator == '-':
        result = a - b
        if msg != '':
            msg = msg_9 + msg
            print(msg)
        print(result)
    elif operator == '*':
        result = a * b
        if msg != '':
            msg = msg_9 + msg
            print(msg)
        print(result)
    elif operator == '/':
        if b == 0:
            if msg != '':
                msg = msg_9 + msg
                print(msg)
            print("Yeah... division by zero. Smart move...")
            continue
        else:
            result = a / b
            if msg != '':
                msg = msg_9 + msg
                print(msg)
            print(result)
    while True:
        store_result = input('Do you want to store the result? (y / n):')
        if store_result == 'y':
            if result.is_integer() and result in range(-10, 11):
                msg_index = 10
                while True:
                    answer = input(messages[msg_index])
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            M = result
                            break
                    elif answer == 'n':
                        break
                break
            else:
                M = result
                break
        elif store_result == 'n':
            break

    continue_calculation = input('Do you want to continue calculations? (y / n):')
    if continue_calculation == 'y':
        continue
    elif continue_calculation == 'n':
        break




