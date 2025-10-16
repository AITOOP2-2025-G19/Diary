from diaries.DiarySample import DiarySample
from diaries.TKTKTDiary import TKTKTDiary
from diaries.YuriDiary import YuriDiary 
from diaries.KoshimizuDiary import KoshimizuDiary

diaries = [DiarySample(),
           YuriDiary(), 
           TKTKTDiary(),
           KoshimizuDiary() ,
          ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()