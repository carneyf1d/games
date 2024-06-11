from faker import Faker

class NameAnonymizer:

    def __init__(self):
        fake = Faker()
        self.fakeName = fake.name()
    
    def get_fakeName(self):
        return self.fakeName
    
    def set_fakeName(self, fakeName):
        self.fakeName = fakeName

if __name__ == "__main__":
    anonName = NameAnonymizer()
    print("Your anonymous name is ", anonName.get_fakeName)
    newName = input("Enter a new name you'd like to be called...")
    anonName.set_fakeName(newName)
    print("Your new anonymous name is ", anonName.get_fakeName)
    


