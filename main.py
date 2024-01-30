import json
import pickle
class Student():
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"Student sa vola {self.name} z krajiny {self.country} a ma {self.age}"

    # def vloz_do_suboru(self, nazov_suboru):
    #     with open(nazov_suboru, "wb") as file:
    #         pickle.dump(self, file)
    #
    # @staticmethod
    # def vytvor_zo_suboru(nazov_suboru):
    #     with open(nazov_suboru, "rb") as file:
    #         return pickle.load(file)
    #

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__)

    def uloz_do_suboru(self, nazov):
        with open(nazov, "w") as file:
            file.write(self.to_json())

patrik = Student("Patrik", 30, "Slovakia")
milan = Student("Milan", 40, "CZ")

patrik.studentov_kamos = milan
patrik.uloz_do_suboru("patrik.json")

#print(patrik)
# serialized = pickle.dumps(patrik)
# print(serialized)
#
# patrik_obnoveny = pickle.loads(serialized)
# print(patrik_obnoveny)
#patrik.vloz_do_suboru("patrik.txt")
#patrik_zo_suboru = Student.vytvor_zo_suboru("patrik.txt")
#rint(patrik_zo_suboru)







# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def vloz(self, prvok):
#         if self.head is None: # je hlavicka prazdna
#             self.head = prvok # ak ano hlavicka je prvok
#         else:
#             aktualny = self.head
#             while aktualny.next:
#                 aktualny = aktualny.next
#             aktualny.next = prvok
#
#     def vypis(self):
#         if self.head is None:
#             print("Zoznam je prazdny")
#         else:
#             aktualny = self.head
#             print(aktualny.data)
#             while aktualny.next:
#                 aktualny = aktualny.next
#                 print(aktualny.data)
#     def check(self,meno):
#         aktualny = self.head # zistujem ci je to ten prvy
#         if aktualny.data == meno:
#             return True
#         while aktualny.next:
#             aktualny = aktualny.next
#             if aktualny.data == meno:
#                 return True
#         return False
#     # def vymenit(self, meno):
#     #     aktualny = self.head  # zistujem ci je to ten prvy
#     #     while aktualny.next:
#     #         aktualny = aktualny.next
#     #         if aktualny.data == meno:
#
#
#
# class Prvok:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# mojLinked = LinkedList()
# # prvok1 = Prvok("Milan")
# # mojLinked.vloz(prvok1)
# # prvok2 = Prvok("Jozo")
# # mojLinked.vloz(prvok2)
# # prvok3 = Prvok("Fero")
# # mojLinked.vloz(prvok3)
# mojLinked.vypis()
# #print("test")


