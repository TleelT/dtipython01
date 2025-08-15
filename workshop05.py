# คำสั่งรับค่าข้อความ ใช้ฟังก์ชั่น innut()
# ***** ตัวแปร variale คือ ชื่อที่ Dev ตั้งขึ้นมาเอง (เป็นไปตามกฎการตั้งชื่อ)หน้าที่เก็บข้อมูลที่ต้องใช้ในโปรแกรม
# ฟังก์ชั่นที่ใช้แปลงข้อความเป็นตัวเลข ใช้ฟังก์ชั่น int(), float()

fullname = input('ป้อนชื่อ: ')
mid_score = input('ป้อนคะแนนกลางภาค: ')
final_score = input('ป้อนคะแนนปลายภาค: ')
quiz_score = input('ป้อนคะแนนเก็บ: ')
print('------------')
print(f'สวัสดีคุณ : {fullname}')
print(f'คุณสอบได้คะแนนรวม : {mid_score + final_score + quiz_score} คะแนน')
print('------------')
# ใช้ ,
print()
print()
print('------------')
# ใช้ +
print()
print()
print('------------')
# ใช้ format
print()
print()
print('------------')