from diaries.DiarySample import DiarySample
from diaries.TKTKTDiary import TKTKTDiary
from diaries.KitagawaDiary import KitagwaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),TKTKTDiary(),KitagwaDiary(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()