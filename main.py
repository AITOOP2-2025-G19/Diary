from diaries.DiarySample import DiarySample
from diaries.KoshimizuDiary import KoshimizuDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
           KoshimizuDiary() ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()