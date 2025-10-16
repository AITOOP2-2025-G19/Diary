from diaries.DiarySample import DiarySample
from diaries.TKTKTDiary import TKTKTDiary
from diaries.YuriDiary import YuriDiary 
from diaries.KoshimizuDiary import KoshimizuDiary
from diaries.KitagawaDairy import KitagawaDairy

diaries = [DiarySample(),
           YuriDiary(), 
           TKTKTDiary(),
           KoshimizuDiary() ,
           KitagawaDiary(),
          ]



for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()