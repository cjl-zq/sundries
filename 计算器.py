x = ('输入第一个数字：')
y = ('输入第二个数字：')
z = ('输入运算符号：（+、-、*、/）')

match z:
    case '+':
        num = x + y
    case '-':
        num = x - y
    case '*':
        num = x * y
    case '/':
        num = x / y

print('答案是：',num)
