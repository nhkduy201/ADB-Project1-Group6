from random import randrange
from datetime import timedelta, datetime
from random import randint


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


def get_date():
    start_date = datetime.strptime('5/1/2020 12:01 AM', '%m/%d/%Y %I:%M %p')
    end_date = datetime.strptime('6/30/2021 11:59 PM', '%m/%d/%Y %I:%M %p')
    return random_date(start_date, end_date)


def writeToScript(bill_id, customer_id, total_bill):
    f = open("HoaDon.txt", "w")
    for i in range(500000):
        index = randint(0, 99999)
        f.write("INSERT INTO HoaDon (MaHD, MaKH, NgayLap, TongTien) VALUES ")
        f.write(f"('{bill_id[i]}', '{customer_id[index]}', '{get_date()}', '{total_bill[i]}')\n")
        if (i+1) % 10000 == 0:
            f.write("GO\n")
        i += 1
    f.close()


def readData(total_bill):
    index = 0
    for i in range(1, 11):
        f = open(f"CT_HoaDon#{i}.txt", "r")
        for line in f:
            if line == "GO\n":
                continue
            info = line.split("INSERT [dbo].[CT_HoaDon] ([MaHD], [MaSP], [SoLuong], [GiaBan], [GiaGiam], [ThanhTien]) VALUES ")
            data = info[-1].split(', ')
            total_bill[index] += int(data[-1][:-2])
            index += 1
        if index == 500000:
            index = 0
        f.close()


customer_id = []
bill_id = []
total_bill = []
i = 1

while i <= 500000:
    zero = 6 - len(str(i))
    if i <= 100000:
        tmp = 5 - len(str(i-1))
        customer_id.append('KH' + '0' * tmp + str(i-1))
    bill_id.append('HD' + '0' * zero + str(i))
    total_bill.append(0)
    i += 1
readData(total_bill)
writeToScript(bill_id, customer_id, total_bill)