class MYClass:
    def __init__(self, name):
        self.name = 'saud'
        self.age = 29
        self.hobby = 'none'

    def any_method(self):
        print('Anything')


obj = MYClass('saud')

obj.anything = 'anything'

dictin = obj.__dict__


for item in dictin:
    print(f"{item}:{dictin[item]}")


