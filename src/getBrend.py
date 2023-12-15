import xlsxwriter
import openpyxl

# Открываем файл Excel для чтения
workbook = openpyxl.load_workbook('result.xlsx')

# Получаем первый лист
sheet = workbook.active

# Создаем новый файл Excel для записи
new_workbook = xlsxwriter.Workbook('result1.xlsx')
new_sheet = new_workbook.add_worksheet()

# Получаем все значения из столбца A, начиная со второй строки
column_a_values = [cell.value for cell in sheet['A'][1:]]

# Записываем второе слово из столбца A в столбец B
for index, value in enumerate(column_a_values, start=1):
    second_word = value.split()[1]
    new_sheet.write(index, 0, value)
    new_sheet.write(index, 1, second_word)

# Закрываем файлы
new_workbook.close()
workbook.close()