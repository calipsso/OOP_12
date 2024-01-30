class LinkedList:
    def __init__(self):
        self.head = None

    def vloz(self, prvok):
        if self.head is None: # je hlavicka prazdna
            self.head = prvok # ak ano hlavicka je prvok
        else:
            aktualny = self.head
            while aktualny.next:
                aktualny = aktualny.next
            aktualny.next = prvok

    def vypis(self):
        aktualny = self.head
        print(aktualny.data)
        while aktualny.next:
            aktualny = aktualny.next
            print(aktualny.data)
    def check(self,meno):
        aktualny = self.head # zistujem ci je to ten prvy
        if aktualny.data == meno:
            return True
        while aktualny.next:
            aktualny = aktualny.next
            if aktualny.data == meno:
                return True
        return False
    # def vymenit(self, meno):
    #     aktualny = self.head  # zistujem ci je to ten prvy
    #     while aktualny.next:
    #         aktualny = aktualny.next
    #         if aktualny.data == meno:



class Prvok:
    def __init__(self, data):
        self.data = data
        self.next = None


mojLinked = LinkedList()
# prvok1 = Prvok("Milan")
# mojLinked.vloz(prvok1)
# prvok2 = Prvok("Jozo")
# mojLinked.vloz(prvok2)
# prvok3 = Prvok("Fero")
# mojLinked.vloz(prvok3)
mojLinked.vypis()
#print("test")

print(mojLinked.check("Milan"))