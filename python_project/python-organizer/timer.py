
import time

remaining_time = int(input("시간을 입력하세요:"))

while remaining_time > 0:
    print(round(remaining_time,1))

    time.sleep(0.1)

    remaining_time -= 0.1

print("타이머가 종료되었습니다")