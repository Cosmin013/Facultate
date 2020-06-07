
class State:

    def __init__(self, b, nm1, nc1, bp=1, nm2=0, nc2=0):
        self.__b = b
        self.__nm1 = nm1
        self.__nc1 = nc1
        self.__nm2 = nm2
        self.__nc2 = nc2
        self.__bp = bp

    def is_final(self):
        if self.__nc1 == 0 and self.__nm1 == 0:
            return True
        else:
            return False

    def transition(self, mm, cm):
        ns = State(self.__b, self.__nm1 + mm, self.__nc1 + cm, 3 - self.__bp, self.__nm2 - mm, self.__nc2 - cm)
        return ns

    def validation(self, mm, cm):
        ns = self.transition(mm, cm)
        if 0 < ns.__nm1 < ns.__nc1:
            return False
        elif 0 < ns.__nm2 < ns.__nc2:
            return False
        elif abs(mm + cm) > ns.__b or cm + mm == 0:
            return False
        elif mm >= 0 and cm >= 0 and mm + cm > 0 and ns.__bp == 2:
            return False
        elif mm <= 0 and cm <= 0 and mm + cm < 0 and ns.__bp == 1:
            return False
        elif ns.__nm1 < 0 or ns.__nm2 < 0 or ns.__nc1 < 0 or ns.__nc2 < 0:
            return False
        return True

    def get_b(self):
        return self.__b

    def get_bp(self):
        return self.__bp

    def get_nm1(self):
        return self.__nm1

    def get_nc1(self):
        return self.__nc1

    def __eq__(self, other):
        if isinstance(other, State):
            if self.__b != other.__b:
                return False
            elif self.__nc1 != other.__nc1:
                return False
            elif self.__nc2 != other.__nc2:
                return False
            elif self.__nm1 != other.__nm1:
                return False
            elif self.__nm2 != other.__nm2:
                return False
            elif self.__bp != other.__bp:
                return False
            return True
        else:
            return False

    def __str__(self):
        s = "(" + str(self.__b) + "," + str(self.__nm1) + "," + str(self.__nc1) + "," + str(self.__bp) + "," + str(self.__nm2) + "," + str(self.__nc2) + ")"
        return s
