'''
@property methods should be light, do slow or complex work using normal methods
'''
class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms < 0:
            raise ValueError('%f must be > 0' % ohms)
        if hasattr(self, '_ohms'):
            raise AttributeError('Cannot set attribute')
        self._ohms = ohms

r1 = VoltageResistance(1e3)
r2 = BoundedResistance(1e3)
r1.voltage = 10
r2.ohms = 10
print('%5r amps and %1f' % (r1.current, r2.current))
