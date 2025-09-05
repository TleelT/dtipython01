# คำสั่ง break, contine *** ที่อยูใน Loop
# berak หากถุกทำงาน จะถือว่าจบ Loop ทันที
# continue หากถูกทำงาน จะถือว่าจบรอบนั้นทันที แล้วให้ไปรอบต่อไปเลย

for i in range(1, 10):
    if i == 5:
        break   # หยุดทันทีเมื่อเจอ 5
    print(i)