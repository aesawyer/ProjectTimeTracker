import xlwt


def export_xls():
    book = xlwt.Workbook(encoding='utf-8')
    sh = book.add_sheet('sheet1')

    col_names = ["Date", "Topic", "Time"]

    for c in range(len(col_names)):
        sh.write(0, c, col_names[c])

    data = []
    file = open("outputlog.txt", "r")
    for x in file:
        data.append(x)

    for o in range(len(data)):
        sh.write(o+1, 0, data[o])

    book.save('myfile.xls')
