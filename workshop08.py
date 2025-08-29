# Operator precedence
# สร้างโปรแกรมรับข้อมูลจำนวนเต็ม 5 จำนวนจากผู้ใช้
# และคำนวณหาผลรวม และค่าเฉลี่ยของข้อมูลที่รับเข้ามา
# เป็นเท่าใด แล้วแสดงผลทางหน้าจอ
# สูตร  
# ผลรวม = เลขตัวที่1 + เลขตัวที่2 + เลขตัวที่3 + เลขตัวที่4 + เลขตัวที่5
# ค่าเฉลี่ย = ผลรวมของเลข 5 จำนวน / 5
# ============================
# Program  Average  5  Number
# ============================
# Enter number 1 : <input>
# Enter number 2 : <input>
# Enter number 3 : <input>
# Enter number 4 : <input>
# Enter number 5 : <input>
# ============================
# Sum of 5 number is : <output>
# Average of 5 number is : <output>
# ============================

print('==================')
print(' Program SUM-Average 5 Number')
print('==================')
num1 = int( input('Enter number 1 : ') )
num2 = int( input('Enter number 2 : ') )
num3 = int( input('Enter number 3 : ') )
num4 = int( input('Enter number 4 : ') )
num5 = int( input('Enter number 5 : ') )
print('==================')

sum = num1 + num2 + num3 + num4 + num5
avg = sum / 5

print(f'Sum of 5 number is: {sum}')
print(f'Average of 5 number is: {avg}')
print('==================')