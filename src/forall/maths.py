
import numpy as np
import sympy as sp

def make(obj, exp):
    for arg in range(obj.args):
        print(arg.random())




class Addition(object):
    def __init__(self):
        self.args = [None] * 2
        self.solution = None

    def __getitem__(self, key):
        return self.args[key]

    def __setitem__(self, key, value):
        self.args[key] = value
        self.solve()

    def __repr__(self):
        pass

    def make(self, addends, solution):
        pass

    def solve(self):
        try:
            self.solution = self.args[0] + self.args[1]
        except TypeError:
            pass

    def expression(self):
        return '%s + %s' % (sp.latex(self.args[0]), sp.latex(self.args[1]))

    def equation(self, x=None):
        s = '%s + %s = ' % (sp.latex(self.args[0]), sp.latex(self.args[1]))
        if x is None:
            return s
        s += sp.latex(x)
        return s

    def solved(self):
        return '%s + %s = %s' % (sp.latex(self.args[0]), sp.latex(self.args[1]), sp.latex(self.solution))


class Random(object):
    def __call__(cls, min, max, dx):
        return None

class Uniform(Random):
    def __call__(cls, min, max, dx):
        return np.random.rand() * (max - min) + min

class UniformInteger(Uniform):
    def __call__(cls, min, max, dx):
        return int(np.random.rand() * (max - min) / dx) * dx + min




class Number(object):
    base = 10
    min = None
    max = None
    dx = 1.
    features = None
    def __init__(self):
        self.features = set()
        self._random = Random()

    def __iter__(self):
        self.n = None
        return self

    def __next__(self):
        if self.n is None:
            self.n = self.min
        else:
            self.n += self.step

        if self.n == self.max:
            raise StopIteration
        return self.n

    def random(self):
        """
        dist: generate a random variable on a distribution of [0, 1)
        """
        return self._random(self.min, self.max, self.step)

    def __repr__(self):
        return '<%s %s-%s>' % (self.__class__.__name__, self.min, self.max)

def SingleDigit(obj=None):
    obj.min = 0
    obj.max = obj.base
    obj.step = 1
    obj.features.add('SingleDigit')

    if issubclass(UniformInteger, obj._random.__class__):
        obj._random = UniformInteger()
    else:
        raise Exception("Tried to subclass to UniformInteger from %s" % obj._random.__class__.__name__)
    return obj

def addition2(limit):
    a = int(np.random.randint(0, limit))
    b = int(np.random.randint(0, limit))
    if np.random.rand() < 0.9:
        ques = "%d + %d = " % (a, b)
    else:
        ques = "%d more than %d = " % (a, b)
    sol = a + b
    q = Question(ques, sol)
    return q

def subtraction(limit):
    a = int(np.random.randint(0, limit))
    b = int(np.random.randint(0, limit))
    a, b = max([a, b]), min([a, b])
    if np.random.rand() < 0.9:
        ques = "%d - %d = " % (a, b)
    else:
        ques = "Take %d away from %d = " % (b, a)
    sol = a - b
    q = Question(ques, sol)
    return q

def multiplication(limit):
    a = int(np.random.randint(0, limit))
    b = int(np.random.randint(0, limit))
    if np.random.rand() < 0.9:
        ques = "%d x %d = " % (a, b)
    else:
        ques = "%d groups of %d = " % (a, b)
    sol = a * b
    q = Question(ques, sol)
    return q

