kw = eval(input('So kw tieu thu:\n'))
gia_50 = 1484
gia_51_100 = 1533
gia_101_200 = 1786
gia_201_300 = 2242
gia_301_400 = 2503
gia_401 = 2587

if kw < 51:
    tien_dien = kw*gia_50
elif kw < 101:
    tien_dien = 50*gia_50 + (kw-50)*gia_51_100
elif kw < 201:
    tien_dien = 50*gia_50 + 50*gia_51_100 + (kw-100)*gia_101_200
elif kw < 301:
    tien_dien = 50*gia_50 + 50*gia_51_100 + 100*gia_101_200 + (kw-200)*gia_201_300
elif kw < 401:
    tien_dien = 50*gia_50 + 50*gia_51_100 + 100*gia_101_200 + 100*gia_201_300 + (kw-300)*gia_301_400
else:
    tien_dien = 50*gia_50 + 50*gia_51_100 + 100*gia_101_200 + 100*gia_201_300 + 100*gia_301_400 + (kw-400)*gia_401
    
print('Tien dien phai tra = %i' %(tien_dien))