class Jar:
    def __init__(self, capacity=12, size =0):
        # since default set to 12, not necessarily to limit in if again
        if capacity < 0:
            raise ValueError("wrong")
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return '🍪' * self._size

    # add n to jar, should not more than capacity
    def deposit(self, n):
        self._size = self._size + n
        if self._size  <= self._capacity:
            return self._size
        else:
            raise ValueError("Too many cookies!")

    # remove n from jar
    def withdraw(self, n):
        if self._size >= n:
            self._size = self._size - n
            return self._size
        else:
            raise ValueError("Not enough cookies!")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(5)
    print(jar)
    jar.withdraw(1)
    print(jar)


if __name__ == "__main__":
    main()

