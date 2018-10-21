class TempConverter:
    def convert_to_celcius(self, value, units):
        if units is 'f':
            return (value - 32) * 5/9
        elif units is 'k':
            return value - 273.15
        else:
            raise ValueError('Invalid')

    def convert_to_fahrenheit(self, value, units):
        if units is 'c':
            return (value * 9/5) + 32
        elif units is 'k':
            return (value - 273.15) * (9 / 5) + 32
        else:
            raise ValueError('Invalid')

    def convert_to_kelvin(self, value, units):
        if units is 'f':
            return (value - 32) * (5 / 9) + 273.15
        elif units is 'c':
            return value + 273.15
        else:
            raise ValueError('Invalid')
