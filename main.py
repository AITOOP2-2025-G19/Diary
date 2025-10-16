from diaries.DiarySample import DiarySample
from diaries.YuriDiary import YuriDiary 
from diaries.TKTKTDiary import TKTKTDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),
            YuriDiary(), 
            TKTKTDiary(),]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()