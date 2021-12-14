from decimal import *

if __name__ == '__main__':
    getcontext().prec = 50
    start = Decimal(2)
    while True:
        b = start
        res = ["2"]
        for i in range(1, 100):
            b = Decimal(int(b)) * (b - Decimal(int(b)) + Decimal(1))
            res.append(str(int(b)))
        res_float = Decimal(res[0] + "." + "".join(res[1:]))
        if start > res_float:
            start = (start + res_float) / Decimal(2)
        elif res_float > start:
            start = (res_float + start) / Decimal(2)
        if str(start)[:26] == str(res_float)[:26]:
            print(str(start)[:26])
            break
