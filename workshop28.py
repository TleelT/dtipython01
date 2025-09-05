# =========================================
# โปรแกรมคำนวณแบบเท่ ๆ 😎
# =========================================

from datetime import datetime
import time

print('💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥')
print('       🔹 ระบบคำนวณอายุพนักงาน 🔹')
print('💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n')

while True:
    emp_name = input('🤵 ชื่อพนักงาน: ')
    if emp_name.upper() == 'SAU':
        print('\n🔥 ระบบหยุดทำงาน... ขอบคุณที่มาเยือน DTI-SAU 🔥')
        break
    
    emp_year = int(input('📆 ปีเกิด (พ.ศ.): '))
    # คำนวณอายุ
    current_year = datetime.now().year + 543  # ปรับเป็น พ.ศ.
    emp_age = current_year - emp_year
    
    # แสดงผลแบบเท่ ๆ
    print('\n✨💪 ผลลัพธ์สุดเท่ของคุณ 💪✨')
    print('---------------------------------')
    print(f'👤 ชื่อ: {emp_name.upper()}')
    print(f'🎂 เกิดปี: {emp_year}')
    print(f'🕶 อายุ: {emp_age} ปี')
    print('---------------------------------')
    
    # ใส่ข้อความหล่อ ๆ
    if emp_age < 25:
        print("⚡ คุณคือดาวรุ่งไฟแรง! Keep rocking! ⚡")
    elif emp_age < 40:
        print("🔥 ความเท่ระดับมือโปร! 🔥")
    else:
        print("💎 ประสบการณ์ล้ำค่า! สุขภาพดี ๆ นะ! 💎")
    
    print('\n💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥\n')
    time.sleep(0.5)  # เพิ่ม effect หน่วงเวลาเล็กน้อย

print('\n📞 หากมีปัญหาโทร. 1111 คิด 500 บาท 😎')
print('💥 ขอบคุณที่ใช้บริการโปรแกรมของเรา DTI-SAU 💥')