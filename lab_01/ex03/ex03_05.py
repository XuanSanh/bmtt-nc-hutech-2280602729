def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict
#Nhap danh sach tu nguoi dung
input_string = input("Nhap danh sach ca tu, cach nhau bang dau cach: ")
world_list = input_string.split()

#Su dung ham va in ket qua
so_lan_xuat_hien = dem_so_lan_xuat_hien(world_list)
print("So lan xuat hien cua cac phan tu: ",so_lan_xuat_hien)