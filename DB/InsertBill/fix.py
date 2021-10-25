from math import prod
import random


def readData():
    product_id = []
    price = []
    f = open("E:\HTML\SanPham.txt", errors="ignore")
    for line in f:
        info = line.split("INSERT INTO SanPham(MaSP, TenSP, SoLuongTon, MoTa, Gia) VALUES ")
        data = info[-1].split(",")
        product_id.append(data[0][2:-1])
        price.append(int(data[-1][:-2]))
    return product_id, price


def readFromFile():
    current_product = []
    for i in range(1,6):
        f = open(f"CT_HoaDon#{i}.txt", "r")
        for line in f:
            if line == "GO\n":
                continue
            info = line.split("INSERT [dbo].[CT_HoaDon] ([MaHD], [MaSP], [SoLuong], [GiaBan], [GiaGiam], [ThanhTien]) VALUES ")
            data = info[-1].split(", ")
            current_product.append(data[1][2:-1])
    return current_product


def writeData(product_id, price, current_product):
    i = 1
    for j in range(6, 11):
        f = open(f"CT_HoaDon#{j}.txt", "w")
        while i <= (j-6+1)*100000:
            quantity = random.randint(1, 10)
            sale = random.randint(1, 5)
            index = random.randint(0, 9999)
            while current_product[i-1] == product_id[index]:
                index = random.randint(0, 9999)
            price_before = int(price[index] * sale * 0.1)
            price_after = int(price[index] * sale * 0.01)
            f.write("INSERT [dbo].[CT_HoaDon] ([MaHD], [MaSP], [SoLuong], [GiaBan], [GiaGiam], [ThanhTien]) VALUES ")
            f.write(f"(N'HD{(6 - len(str(i))) * '0' + str(i)}', N'{product_id[index]}', {quantity}, {price_before}, {price_after}, {quantity*(price_before-price_after)})\n")
            if i % 100 == 0:
                f.write("GO\n")
            i += 1
        f.close()


current_product = readFromFile()
product_id, price = readData()
writeData(product_id, price, current_product)

