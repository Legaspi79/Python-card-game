class Player:
    def __init__(self, name):
        self.name = name



    def character_menu(self):
        print(self.name)



def character_creation():
    # affinity_list = ["Water", "Wind", "Fire", "Earth"]
    name = input("what is your name ")

    # for i in affinity_list:
    #     print(i)
    # choice = int(input("Choose your affinity: "))
    return name


returned = character_creation()

P1 = Player(returned[0])
print(f"{P1.name}")