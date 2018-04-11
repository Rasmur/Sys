import openpyxl

wb = openpyxl.load_workbook(filename = 'oprosy.xlsx')
sheet = wb['Лист1']

line = [[]]
cells = sheet['A4': 'J30']

i = 0

for c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 in cells:
    line.append(line)

    line[i].append(c1.value)
    line[i].append(c2.value)
    line[i].append(c3.value)
    line[i].append(c4.value)
    line[i].append(c5.value)
    line[i].append(c6.value)
    line[i].append(c7.value)
    line[i].append(c8.value)
    line[i].append(c9.value)
    line[i].append(c10.value)

    i =+ 1


# a1 = sheet['A1']
# a2 = sheet['A2']
# a3 = sheet.cell(row=3, column=1)
#
# print(a1.value)
# print(a2.value)
# print(a3.value)
