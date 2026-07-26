import time
focus_minutes = int(input("집중할 시간을 입력하세요:"))

focus_Seconds = focus_minutes * 60

while focus_Seconds > 0:
    minutes = focus_Seconds // 60
    
    seconds = focus_Seconds % 60

    print(f"{minutes:02d}:{seconds:02d}")
    
    time.sleep(1)
   
    focus_Seconds-=1

print("타이머가 종료되었습니다")