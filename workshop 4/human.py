class Human:
    #name=  "Esra"
    #built-in
    #constructor
    def __init__(self,name):
        self.name= name
        print("Bir human instance'i üretildi.")
    def __str__(self):
        return f"STTR Fonksiyonunda dönen değer : {self.name}"
        
    def talk(self,sentence):
        name="Songül"
        print(f"{self.name}:{sentence}")
    def walk(self): #içine self diye parametre yazmazsak çalışmıyor. başka birseyde yazılabilir ama community de self kullanılıyor
        print(f"{self.name} is walking..")