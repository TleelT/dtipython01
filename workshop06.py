#Operator ตัวดำเนินการ
# 1. Arithemetic Opt. เครื่องหมายคำนวณ 
# + - * /  **(exponential)  %(mode) //(floor)
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3) #หารปกติ
print(10 % 3) #หารเอาเาศษ
print(10 // 3) #หารสามส่วน Mod กับ floor ไม่เอาทศนิยม
print(10 ** 3)
print('******************')
# 2. Comparison Opt เครือ่หงมายเปรียบเทียบ ผลลัพธ์ True or False
# == , != , > , < , >= , <=
print(10 >= 25) # False
print(999 < 555) # Flase
print('Rayong' >= ' Ranong ') # True
# 3. logical Opt เครื่องหมายตรรกะ 
# not , and , or
# ข้อมูลที่จะใช้กับเครื่องหมายนี้มีแค่ True and False  (boolean) และผลลัพธ์ True/False (boolean)
print(not True)
print(not False)
print('******************')
print(True and True) #True
print(True and False) #False
print(False and False) #False
print(False and False) #False
print('******************')
print(True or True) #True
print(True or False) #True
print(False or False) #False
print(False or False) #False