import xlsxwriter

def writer(parametr):
    book = xlsxwriter.Workbook("Output_test.xlsx")
    page = book.add_worksheet("data")

    row, column = 0, 0
    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 20)
    page.set_column("D:D", 20)
    page.set_column("E:E", 20)
    page.set_column("F:F", 20)
    page.set_column("G:G", 20)

    for item in parametr:
        page.write(row, column, item.name)
        page.write(row, column+1, item.wired)
        page.write(row, column+2, item.microphone)
        page.write(row, column+3, item.mp)
        page.write(row, column+4, item.resolutions_amount)
        page.write(row, column+5, str(item.resolutions))
        page.write(row, column+6, item.usb_type)

        row += 1

    
    book.close()