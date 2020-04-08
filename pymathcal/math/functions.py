from .constants import e


class log:

    def __init__(self, x, base=10):
        self.x = x
        self.base = base
        self.log = self.__log__(self.base)
        self.binary = self.__log__(2)
        self.common = self.__log__(10)
        self.natural = self.__log__(e)

    def __float__(self):
        return self.log

    def __str__(self):
        return str(float(self))

    def __log__(self, base):
        # return binary log of x with base = 2
        [val, dec] = [0, 0]
        while True:
            if dec > 10:
                break
            else:
                a = base ** val
                if a == self.x:
                    return float(val)
                elif a >= self.x:
                    val = val - (10 ** -dec)
                    dec = dec + 1
                val = val + (10 ** -dec)
        return round(val, 8)
