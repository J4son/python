import xlrd,xlwt,xlutils
#fichier = xlrd.open_workbook(filename="/Users/brur/Desktop/inventaire_total.xls")


from xlrd import open_workbook
wb = open_workbook("/Users/brur/Desktop/inventaire_total.xls")
for s in wb.sheets():
    print ('Sheet:',s.name)
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (','.join(values))
    print
