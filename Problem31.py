
class Coins:

    def __init__(self, coins, coinbase):
        self.coins = coins
        self.coinbase = coinbase

    def value(self):
        sum = 0
        for i in range(len(self.coins)):
            sum += self.coins[i]*self.coinbase[i]
        return sum

    def addUpTo(self, max):
        carry = True
        for i in range(len(self.coins)):
            if carry:
                self.coins[i] += 1
                carry = False
            if self.value() > max:
                self.coins[i] = 0
                carry = True
        return carry

    def __str__(self):
        return str(self.value())

def findCombinations(c, val):
    paths = 0
    while not c.addUpTo(val):
        if c.value() ==  val:
            paths += 1
    return paths

pounds = [1, 2, 5, 10, 20, 50, 100, 200]
c = Coins([0, 0, 0, 0, 0, 0, 0, 0], pounds)
print(findCombinations(c, 200))
