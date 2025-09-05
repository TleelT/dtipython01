# คำสั่ง match-case
# ใช้สำหรับพิสูจน์ตรวจสอบหลายครั้ง คล้าย if-elif-else
'''
match expression/ตัวแปร :
    case ค่า | ค่า | ... :
        คําสั่ง
    case ค่า | ค่า | ... :
        คําสั่ง
    case ค่า | ค่า | ... :
        คําสั่ง
    case ค่า | ค่า | ... :
        คําสั่ง
    case _ :
        คำสั่ง
'''
xx = 123456
 
match xx :
    case 10 | 20 :
        print('Hello.....')
        print('Wow.....')
    case 100 :
        print('Hi......')
    case 555 | 666 | 777 | 888 :
        print('Hey......')
        print('Hum......')
    case _ :
        print('Bye bye...')