# return คือ คำสั่ง ที่ใช่ส่งค่าข้อมูลใดๆ กลับไปยังจุดที่เรียกใช้ฟังชั่น/คำสั่ง Return เป็นการบบอกว่า function นั้นๆทำงานจบแล้ว

# 3. no parameter have return
'''
def func_name() :
    คำสั่ง 
    คำสั่ง
    ........
    return ข้อมูลที่ต้องการส่งกลับ
'''

def func_e() :
    print('Hello...')
    return 'Hi...'

def func_f() :
    return 'Wow...', 'Wooo...', 99999

print(func_e())

xx = func_e()
print(xx)

a, b, c = func_f()
print(a)
print(b)
print(c)