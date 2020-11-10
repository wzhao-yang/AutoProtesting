class Calc:
    # steps 1
    def add(self, a: int, b: int) -> int:
        return a + b

    # steps2

    def add1(self, a: int, b: int) -> int:
        return a + b

    def div(self, a, b):
        try:
            return a / b
        except(ZeroDivisionError, ValueError):
            return "请检查数据，不能含有0"

    #  两个数相乘
    def MUL(self, a, b):
        return a * b
