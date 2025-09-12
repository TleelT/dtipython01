# parameter คือ ตัวแปรประเภทนึงที่เขียนอยุ่ในวงเล็บหลังชื่อ Function และจะใช้ได้เฉพาะในฟังชั่นนั้นๆเท่านั้น
# return คือ คำสั่ง ที่ใช่ส่งค่าข้อมูลใดๆ กับไปยังจุดที่เรียกใช้ฟังชั่น/คำสั่ง Ruturn เป็นการบบอกว่า function นั้นๆทำงานจบแล้ว

# 1. no parameter no return
'''
def func_name() :
    คำสี่ง
    คำสั่ง 
    ........
'''
def func_a() :
    print('hello...')
    print('Hi...')

def func_b() : 
    print('Wow...')

print('bye bye... ')
func_a( ) #call function 
func_a( )
func_a( )
func_b( )
func_b( )