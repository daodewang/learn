'''
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
__import__('os').system('dir')
def f(a):
    a.append(1)
    print(a)

f(pairs)
print(pairs)

b=7

def f(a):
    print(a+b)

f(2)
print(b)


# IO-input
name = 'Liming'
print('my name is %s.' % name)
print(f'my name is {name!s}.')
age = eval(input('input your age\n'))
print(age)

# IO-file
f = open('1.jpg', 'rb')
#s = f.read(4)
for s in f:
    print(s)
    print(f.tell())

f.close()



# IO-json
import json
f = open('testj.json', 'r')
#l = [123,'123',[123,'123']]
s = json.load(f)
print(s)
print(type(s))
#f.write(s)
f.close()



# try
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

# class
class MyClass:
    i = 12345

    def __f(self):
        return 'hello world'

x = MyClass()
#x._f()
MyClass.bb=12345
x.aa = '123'
print(x._MyClass__f())



def fn(self, name='world'):
    print('Hello, %s.' % name)

dct = {'hello':fn, 'i':10}
Hello = type('Hello', (object,), dct)

#He = type('Hello')
print(type(Hello))
h = Hello()
print(h.i)
''''''
MyClass.ff = fn
x.ff()



class ListMetaclass(type):
  def __new__(cls, name, bases, attrs):
    attrs['add'] = lambda self, value: self.append(value)
    return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass


# generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
'''

import re

input_str = 'I LIKE Python3 and Pyth i like Python2.7'
pattern = r'(P|p)yth(on)'
match_python = re.findall(pattern, input_str)
print(match_python)

s = input_str

match = re.search(pattern, s)
if match:
    print(match)