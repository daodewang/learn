'''
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


def f(a):
    a.append(1)
    print(a)


f(pairs)
print(pairs)



def bool_return():
    try:
        a=1
        print('try')
        return 1/0
    except:
        print('except')
    else:
        print('else')
    finally:
        print('final')

print(bool_return())


s = input('请输入除数:')
try:
    result = 20 / int(s)
    print('20除以%s的结果是: %g' % (s, result))
except ValueError:
    print('值错误，您必须输入数值')
except ArithmeticError:
    print('算术错误，您不能输入0')
else:
    print('没有出现异常')
b=7

def f(a):
    print(a+b)

f(2)
print(b)

class MyClass:
    i = 12345

    def __f(self):
        return 'hello world'

x = MyClass()
print(id(MyClass.i))
print(id(x.i))
print(id(MyClass._MyClass__f))
x.f=100
print(id(x.f))
print(type(x))
'''

# IO
name = 'Liming'
print('my name is %s.' % name)
print(f'my name is {name!s}.')
age = eval(input('input your age\n'))
print(age)