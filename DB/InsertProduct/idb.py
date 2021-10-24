import random as rd
import lorem as lr

# clean_brand()
data_file = open('../insert_product.sql', 'w', encoding='UTF8')
insert_prefix = 'INSERT INTO SanPham(MaSP, TenSP, SoLuongTon, MoTa, Gia) VALUES ('
product = open('product.txt', 'r', encoding='UTF8').read().split('\n')
brand = open('brand.txt', 'r', encoding='UTF8').read().split('\n')
order = open('order.txt', 'r', encoding='UTF8').read().split('\n')
name_dict = {}


def clean_brand():
    brand_read = open('brand.txt', 'r')
    clean = '\n'.join(brand_read.read().split())
    brand_write = open('brand.txt', 'w')
    brand_write.write(clean)


def get_id(i):
    return 'SP' + (5 - len(str(i))) * '0' + str(i)


def get_price():
    return rd.randint(2, 300) * 100000 + (1 if rd.random() > 0.5 else 0) * 90000 + (1 if rd.random() > 0.5 else 0) * 9000


def is_exist_name(p, b, o):
    return name_dict.get(f'{p}{b}{o}') != None


def get_name():
    p = rd.randint(0, len(product) - 1)
    b = rd.randint(0, len(brand) - 1)
    o = rd.randint(0, len(order) - 1)
    while is_exist_name(p, b, o):
        p = rd.randint(0, len(product) - 1)
        b = rd.randint(0, len(brand) - 1)
        o = rd.randint(0, len(order) - 1)
    name_dict[f'{p}{b}{0}'] = True
    return f'{product[p]} {brand[b]} phiên bản thứ {order[o]}'


def get_num_inv():
    return rd.randint(0, 100)


def get_des():
    return lr.sentence()[:30]


nop = 10000
empty_des = nop // 3

for i in range(0, nop):
    iden = get_id(i)
    name = get_name()
    num_inv = get_num_inv()
    des = 'NULL'
    if empty_des > 0:
        empty_des -= 1
        des = f"'{get_des()}'"
    price = get_price()
    data_file.write(
        f"{insert_prefix}'{iden}',N'{name}',{num_inv},{des},{price})\n")
