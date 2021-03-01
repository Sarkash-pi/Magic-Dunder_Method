# dunder or magic method

# x = [1,2,3,4]

# # it does same thing in the back
# print(dir(x))
# print(x.__dir__())
# print(2+2)
# print(int.__add__(2,2))

from todo import Todo

s_todo = Todo(name='Sarkash')
t_todo = Todo(name='Tina')

s_todo.add('take the dogs out')
s_todo.add('have breakfast')
s_todo.add('do nothing then')

t_todo.add('company with Sarkash')


print(s_todo > t_todo)
print(s_todo < t_todo)