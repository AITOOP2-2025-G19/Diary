from diaries.AbstractDiary import AbstractDiary
class DiarySample(AbstractDiary):
    def get_date(self):
        return "2024-10-16"
    def get_summary(self):
        return "今日はおにぎりを食べた"
    def get_author(self):
        return "Koshimizu"