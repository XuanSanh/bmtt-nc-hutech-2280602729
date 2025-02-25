#Tao danh sach rong
j=[]
#Duyet qua tat ca cac so tu 2000 den 3200
#Kiem tra xem i co chia het cho 7 va la boi so cua 5 khong?
for i in range (2000,3201):
    if(i % 7 == 0) and (i % 5 !=0):
        j.append(str(i))
print (','.join(j))

