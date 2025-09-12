# 2. have parameter no return 
'''
def func_name(param,param,param.....) :
    คำสั่ง 
    คำสั่ง
    ........
'''

def fun_c( xx ) :
    print(f'สวัสดี {xx}')

def func_d( num1, num2, num3, xx )  :
    sum = num1 + num2 + num3 + xx
    print(f'Sum of 4 number is: {sum}')

fun_c('สมชาย') # ข้อมูลที่ส่งให้ parameter เรียก argument
fun_c('สมใจ')

print('--------------------')
func_d( 10, 20 , 30 , 40 )