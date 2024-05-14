#(Готово) путешествие в будущем
#(Готово) есть пустые поля/поле заполнено пробелами
#(Готово) " не " в полях
#(Готово) дата окончания путешествия раньше чем дата начала путешествия
#(Готово) цифры в полях страны и города
#(Готово) Проверка на двойной пробел
#(Готово) Добавить \n

# уведомление с подтверждением

# c = check_logical_error("Coutry","city","geogr_obg","13-06-2024", "12-06-2024", "comment", "ocenca", "active")
# c.check_timedelta()
# c.check_empty_input()
# c.check_no_in_input()
# c.check_num_in_input
# c.check_on_future()
# c.add_n()
# print(c.error)

import datetime

class check_logical_error():
    def __init__(self, country, city, geogr_obg, date_start, date_end, comment, ocenca, active):
        self.country = country
        self.city = city
        self.geogr_obg = geogr_obg
        self.date_start = date_start
        self.date_end = date_end
        self.comment = comment
        self.ocenca = ocenca
        self.active = active
        self.error = []

    def check_timedelta(self):
        if self.date_start!="" or self.date_end!="":
            d1 = [int(x) for x in self.date_start.split("-")]
            d2 = [int(x) for x in self.date_end.split("-")]
            date_start = datetime.date(year=d1[2], month=d1[1], day=d1[0])
            date_end = datetime.date(year=d2[2], month=d2[1], day=d2[0])
            if date_end-date_start<datetime.timedelta(0):
                self.error.append("Дата окончания путешествия не может быть раньше начала путешествия!")
            elif date_end-date_start==datetime.timedelta(0):
                self.error.append("Дата окончания путешествия не может совпадать с началом путешествия!")

    def check_empty_input(self):
        if self.country=="" or self.country.count(" ")==len(self.country): self.error.append("Поле «Страна» должно быть заполнено!")
        if self.city=="" or self.city.count(" ")==len(self.city): self.error.append("Поле «Город» должно быть заполнено!")
        if self.geogr_obg=="" or self.geogr_obg.count(" ")==len(self.geogr_obg): self.error.append("Поле «Географический объект» должно быть заполнено!")
        if self.comment=="" or self.comment.count(" ")==len(self.comment): self.error.append("Поле «Комментарий» должно быть заполнено!")
        if self.date_start=="" or self.date_start.count(" ")==len(self.date_start): self.error.append("Поле «дата начала путешествия» должно быть заполнено!")
        if self.date_end=="" or self.date_end.count(" ")==len(self.date_end): self.error.append("Поле «Дата окончания путешествия» должно быть заполнено!")

    def check_no_in_input(self):
        if " нет " in self.country.lower() or \
            " no " in self.country.lower() or \
            " не " in self.country.lower() or\
            "нет " in self.country.lower() or \
            "no " in self.country.lower() or \
            "не " in self.country.lower(): self.error.append("Поле «Страна» не должно иметь частицы «не»/«нет»/«no»!")
        if " нет " in self.city.lower() or \
            " no " in self.city.lower() or \
            " не " in self.city.lower() or \
            "нет " in self.city.lower() or \
            "no " in self.city.lower() or \
            "не " in self.city.lower(): self.error.append("Поле «Город» не должно иметь частицы «не»/«нет»/«no»!")
        if " нет " in self.geogr_obg.lower() or \
            " no " in self.geogr_obg.lower() or \
            " не " in self.geogr_obg.lower() or \
            "нет " in self.geogr_obg.lower() or \
            "no " in self.geogr_obg.lower() or \
            "не " in self.geogr_obg.lower(): self.error.append("Поле «Географический объект» не должно иметь частицы «не»/«нет»/«no»!")

    def check_on_future(self):
        if self.date_start!="" or self.date_end!="":
            d1 = [int(x) for x in self.date_start.split("-")]
            d2 = [int(x) for x in self.date_end.split("-")]
            date_start = datetime.date(year=d1[2], month=d1[1], day=d1[0])
            date_end = datetime.date(year=d2[2], month=d2[1], day=d2[0])
            if date_start-datetime.date.today()>=datetime.timedelta(0):
                self.error.append("Ошибка в поле «Дата начала путешествия»: путешествие не может быть в будущем!")
            if date_end-datetime.date.today()>datetime.timedelta(0):
                self.error.append("Ошибка в поле «Дата окончания путешествия»: путешествие не может быть в будущем!")
    
    def check_num_in_input(self):
        def check(name):
            numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for n in numbers:
                if n in name:return True
            else: return False
        if check(self.country): self.error.append(f"В поле «Страна» не может быть цифр!")
        if check(self.city): self.error.append(f"В поле «Город» не может быть цифр!")
        if check(self.geogr_obg): self.error.append(f"В поле «Географический объект» не может быть цифр!")

    def add_n(self):
        for i in range(len(self.error)):
            self.error[i]=self.error[i]+"\n"