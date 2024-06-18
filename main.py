from fpdf import FPDF
from fpdf.table import TableSpan
from Employee import Employee

mike = Employee(salary=40_000,
                work_days=22,
                work_hours=176,
                tax_rate=13,
                bonus=10_000,
                business_trip_money=4000
)


TABLE_DATA = [
    ["Начислено",   TableSpan.COL,      TableSpan.COL,      TableSpan.COL ,   "Удержано",       TableSpan.COL],
    ["",            "Подлежат оплате",  TableSpan.COL,      "Сумма, руб.",          "Вид удержаний",  "Сумма, руб. "],
    ["",            "Дни",              "Часы",             TableSpan.ROW,    TableSpan.ROW,    TableSpan.ROW],
    ["Оклад",       str(mike.work_days), str(mike.work_hours),   str(float(mike.salary)),          f"НДФЛ(ставка {str(mike.tax_rate)})", str(int(mike.salary_taxes))],
    ["Премии",      str(mike.work_days),     str(mike.work_hours),   str(float(mike.bonus)),          f"НДФЛ(ставка {str(mike.tax_rate)})", str(int(mike.bonuses_taxes))],
    ["Оплачиваемый отпуск", "--", "--", "--", "--", "--"],
    ["Больничные пособия", "--", "--", "--", "--", "--"],
    ["Прочие начисления", "Компенсация неиспользованого отпуска", "--", str(mike.weekend_money), f"НДФЛ(ставка {str(mike.tax_rate)})", str(mike.weekend_money_taxes)],
    [TableSpan.ROW, "Оплата труда в период командировки", "--", str(mike.business_trip_money), f"НДФЛ(ставка {str(mike.tax_rate)}) за суточные выше лимита", str(mike.business_trip_money_taxes)],
    [TableSpan.ROW, "Академический отпуск", "--", str(mike.academy), "НДФЛ(ставка 13%)", str(mike.academy_taxes)],
    [TableSpan.ROW, "Надбавка за выслугу лет", "--", str(mike.plus), "НДФЛ(ставка 13%)", str(mike.pluses_taxes)],
    ["Всего начислено, руб.", TableSpan.COL, TableSpan.COL, str(mike.total_invoice), "Всего удержано, руб.", str(mike.all_taxes)],
    ["Общий облагаемый доход, руб.", TableSpan.COL, TableSpan.COL, str(mike.salary_w_taxes), TableSpan.COL, TableSpan.COL],

]

pdf = FPDF(format='letter', unit='in')
pdf.add_page()
pdf.add_font('DejaVuSansCondensed', "B", fname='./DejaVuSansCondensed-Bold.ttf')
pdf.set_font("DejaVuSansCondensed", 'B', size=10)
with pdf.table(text_align="LEFT") as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)
pdf.output('payment.pdf')