from Chapter5Projects import CNT

P = CNT()
P.a = 1
P.b = 5.5
print(P)

Q = CNT(2.4, 7.1)
print(Q)
print(Q.magnitude())

class ComplexNumber(CNT):
    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)
        

R = ComplexNumber(P.a, P.b)+ComplexNumber(Q.a, Q.b)
print(R)

queue = [1, 2, 4, 5]
queue.enqueue[4]
print(queue)
queue.dequeue()
print(queue)
