# 4. have parameter have returns
'''
def func_name(param,param,param.....) :
    คำสั่ง 
    คำสั่ง
    ........
    return คำที่ต้องการส่งกลับ
'''

def sum_number(n1, n2, n3) : 
    total = n1 + n2 + n3
    return total

def welcome(name) : 
    message = 'Hello' + name
    return message, ' DTI-SAU'

print(sum_number(1,2,3))

# print(welcome('pong')) ไม่ควรเขียนแบบนี้

print(welcome('pong'))

print(sum_number(10,20,30))

data1, data2  = welcome('Mod')
print(data1)
print(data2)