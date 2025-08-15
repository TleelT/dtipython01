# คำสั่งแสดงผลข้อมูลใดๆ หลายประเภทใน print() เดียว เขียนได้ 4 วิธี
# วิธีที่ 1 ใช้ , (ตรงที่ , เวลาแสดงผลจะเว้น 1 space)
print('DTI',999,'Bangna',10+20,True,'Hi',158.45)

# วิธีที่ 2 ใช้ + (ข้อมูลไหนที่ไม่ใช่ string ต้องทำให้เป็น string ก่อนด้วยฟังก์ชั่น str())
print('DTI' + str(9999) + 'Bangna' + str(10+20) + str(True) + 'Hi' + str(158.45))
print('DTI' + str(9999) + 'Bangna' + str(10+20) + ' ' + str(True) + 'Hi' + str(158.45))

print('DTI {} Bsngna {} {} Hi {} '.format(999,10+20,True,158.45))

print(f'DTI {999} Bangna {10+20} {True} Hi {158.45}')