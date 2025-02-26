def fun1():
    print('This is Fun1()')

def fun2():
    print('This is Fun2()')

def fun3():
    print('This is Fun3()')

function_name = input('Enter function name:')
functions = {
    'fun1' : fun1,
    'fun2' : fun2,
    'fun3' : fun3
}
if function_name in functions:
    functions[function_name]()
#OR
#exec(function_name + '()')