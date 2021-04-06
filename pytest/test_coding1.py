import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.append('../')
import coding1
from ttt import t, F

def test_hello():
  print('*****' + str(t.ids))
  coding1.say_hello('JSH')

print(t.div(4,2))
# print(t.div(4,0))

with open('t.txt', 'w') as f:
  f.write('abc')

with F('t2.txt') as f:
  f.write('2222')
  f.write('end')

with open('t2.txt', 'r') as f:
  print(f.readlines())
# with open('t2.txt', 'r') as f:
#   while True:
#     print(f.readline()