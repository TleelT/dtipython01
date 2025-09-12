#โปรแกรมตรวจสอบรถว่าผ่านเกณฑ์ของการตรวจสอบค่าคาร์บอนไดซ์ออกไซน์หรือ 
# โดยหากค่าคาร์บอนไดซ์ออกไซน์มีค่าเกินกว่า 678.55 ให้แสดงข้อความว่า “ไม่ผ่าน”  
# หากน้อยกว่า 678.55 ให้แสดงข้อความ “ผ่าน” โดยให้รับชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดซ์ออกไซน์ที่วัดได้ 
# ทางแป้นพิมพ์

# feature การทำงานจากโจทย์ 
# รับค่า ชื่อเจ้าของ ทะเบียนรถ และปริมาณก๊าซคาร์บอนไดออกไซน์ที่วัดได้
# ตรวจสอบก๊าซ
# แสดงผลว่าผ่าน ไม่ผ่าน
# แสดงชื่อโปรแกรม 

def show_program_name() : 
    print('-----------------------')
    print(' ตรวจสอบรถ ')
    print('-----------------------')

def input_car_info() : 
    car_owner = input(' ป้อนชื่อเจ้าของรถ ')
    car_number = input('ป้อนทะเบียนรถ : ')
    car_carbon = float( input('ป้อนปริมาณก๊าซคาณืบอนไดออกไซน์ : '))
    return car_owner, car_number,  car_carbon

def show_result(car_owner, car_number,  car_carbon, result) : 
    print(f'คุณ {car_owner} ทะเบียนรถ { car_number}')
    print(f'ก๊าซ วัดได้ { car_carbon} สรุป {result}')

def check_carbon(car_owner, car_number, car_carbon) : 
    if car_carbon > 678.55 :
        show_result(car_owner, car_number,  car_carbon, 'ไม่ผ่าน')
    else : 
        # ผ่าน
        show_result(car_owner, car_number,  car_carbon, 'ผ่าน')

show_program_name()
car_owner, car_number, car_carbon = input_car_info()
print('-----------------------')
check_carbon(car_owner, car_number, car_carbon)
print('-----------------------')