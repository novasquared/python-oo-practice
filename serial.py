class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    """
    init function
    - property to store starting number
    - counter = 0

    generate
    - every time an instance is created
        increment counter and return sum

    """
    def __init__(self, start):
        """ 
            initialize self.start to start
            count to 0
        """
        self.start = start
        self.counter = 0
    
    def generate(self):
        """
            add start to counter and return sum
        """
        sum = self.start + self.counter
        self.counter += 1
        
        return sum

    def reset(self):
        """
            reset counter to 0 to reset serial numbers
        """
        self.counter = 0