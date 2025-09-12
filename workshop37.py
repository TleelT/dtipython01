#โปรแกรมซึ่งรับชื่อ และปีเกิดของผู้ใช้โปรแกรมทางแป้นพิมพ์ โดยหากอายุมีค่าตั้งแต่ 55
# ปีขึ้นไป ให้แสดงข้อความว่า "คุณแก่แล้ว..." หากไม่ถึงให้แสดงข้อความ "คุณยังไม่แก่..." ทางหน้าจอ
# ต้องการ 4 ฟังก์ชั่น

# =========================================
#  🌸 โปรแกรมตรวจสอบอายุผู้ใช้ 🌸
# =========================================

def show_program_name():
    print("💫" * 15)
    print("      🌷 โปรแกรมตรวจสอบอายุ 🌷")
    print("💫" * 15)

def input_user():
    name = input("🖊️ ป้อนชื่อของคุณ: ")
    birth_year = int(input("📅 ป้อนปีเกิด (พ.ศ.): "))
    return name, birth_year

def calculate_age(birth_year):
    current_year = 2568  # สามารถเปลี่ยนเป็นปีปัจจุบันจริง ๆ ได้
    return current_year - birth_year

def check_age(name, age):
    print("✨" * 15)
    print(f"👤 คุณ {name} อายุ {age} ปี")
    if age >= 55:
        print("⚠️ คุณแก่แล้ว... แต่ยังดูดีอยู่เสมอ 💖")
    else:
        print("🌟 คุณยังไม่แก่... สดใสเหมือนเดิม 😎")
    print("✨" * 15)

# เริ่มโปรแกรม
show_program_name()
name, birth_year = input_user()
age = calculate_age(birth_year)
check_age(name, age)