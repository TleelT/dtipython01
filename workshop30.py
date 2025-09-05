# =========================================================
# 💥💥 สุดยอดเกมทายตัวเลข 1-100 แบบสุ่มเทพที่สุดในโลก 💥💥
# =========================================================

import time
import sys
import random  # สำหรับสุ่มตัวเลข

def slow_print(text, delay=0.03):
    """ฟังก์ชันพิมพ์ทีละตัวอักษรเหมือน cinematic"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # ขึ้นบรรทัดใหม่

print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
slow_print("**** ยินดีต้อนรับสู่เกมส์ทายตัวเลข ****", 0.05)
print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟\n")

target_number = random.randint(1, 100)  # สุ่มตัวเลข 1-100

while True:
    try:
        guess = int(input("🔹 ป้อนตัวเลขที่ต้องการทาย (1-100): "))
    except ValueError:
        slow_print("⚠️ กรุณาป้อนตัวเลขเท่านั้น! ⚠️", 0.03)
        continue

    if guess == target_number:
        slow_print("\n🎉💥 ยินดีด้วยคุณทายถูก! 💥🎉", 0.05)
        print("🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟")
        break
    elif guess < target_number:
        slow_print("⚡ คุณทายผิด ตัวเลขที่ป้อนน้อยไป ⚡", 0.03)
    else:
        slow_print("🔥 คุณทายผิด ตัวเลขที่ป้อนมากไป 🔥", 0.03)

    print("-----------------------------------------\n")
    time.sleep(0.3)  # เพิ่ม effect เล็ก ๆ