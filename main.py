class Polynomial:
    class Node:
        def __init__(self, coeff, power, next=None):
            self.coeff, self.power, self.next = coeff, power, next

    def __init__(self):
        self.head = None

    def add_term(self, coeff, power):
        if coeff == 0: return
        new = self.Node(coeff, power)
        if not self.head or self.head.power < power:
            new.next, self.head = self.head, new
        else:
            cur = self.head
            while cur.next and cur.next.power > power:
                cur = cur.next
            if cur.power == power: cur.coeff += coeff
            else:
                new.next, cur.next = cur.next, new

    def __add__(self, other):
        res, a, b = Polynomial(), self.head, other.head
        while a or b:
            if not b or (a and a.power > b.power):
                res.add_term(a.coeff, a.power); a = a.next
            elif not a or (b and b.power > a.power):
                res.add_term(b.coeff, b.power); b = b.next
            else:
                res.add_term(a.coeff + b.coeff, a.power)
                a, b = a.next, b.next
        return res

    def __mul__(self, other):
        res = Polynomial()
        a = self.head
        while a:
            b = other.head
            while b:
                res.add_term(a.coeff * b.coeff, a.power + b.power)
                b = b.next
            a = a.next
        return res

    def __eq__(self, other):
        a, b = self.head, other.head
        while a and b:
            if a.coeff != b.coeff or a.power != b.power: return False
            a, b = a.next, b.next
        return not a and not b

    def __str__(self):
        cur, s = self.head, []
        while cur:
            s.append(f"{cur.coeff}x^{cur.power}")
            cur = cur.next
        return " + ".join(s) if s else "0"
