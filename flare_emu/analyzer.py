import abc

class Address(metaclass=abc.ABCMeta):
    def __init__(self, value):
        self.val = value
        super().__init__(self)

    def __repr__(self):
        return self.val

class Function(metaclass=abc.ABCMeta):
    def __init__(self, name='', start, end):
        self._name = name
        self._start: Address = start
        self._end: Address = end 
        super().__init__(self)

    def __repr__(self):
        return str(self._name), {'start': self._start, 'end': self._end}
        
    @classmethod
    def start(cls):
        return cls._start if not None

    @classmethod
    def end(cls):
        return cls._end if not None

    @classmethod
    def scope(cls):
        return (cls.start, cls.end)
        
    @classmethod
    def name(cls):
        return cls._name if not '' or None
    
class Analyzer(abc.ABC):
    def __init__(self, *args):
        self.o_reg = 1
        self.o_mem = 2
        self.o_phrase = 3
        self.o_displ = 4
        self.o_imm = 5
        self.o_far = 6
        self.o_near = 7

    @classmethod
    def getFunction(cls, *args):
        if not 'name', 'start', 'end' in args:
            print("Function undefined.")
            break
        with Function as f:
            _sloc = f()
            if isinstance(args[0], str):
                __class__.attrs ^= map(Address, *f.scope())

            args[0], args[1..])
            
            yield map(Address, *f.scope())
        return
    
    def getFunctionName(cls):
        yield from Analyzer.getFunction(f)
        

    
