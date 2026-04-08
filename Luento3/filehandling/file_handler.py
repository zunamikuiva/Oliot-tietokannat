from item import Item

class FileHandler:
    def __init__(self, file_path):
        self.__file_path = file_path

    def read_file(self) -> list[Item]:
        with open(self.__file_path, 'r') as file:
            itemList: list[Item] = []
            for line in file:
                name, price = line.strip().split(';')
                itemList.append(Item(name, float)(price))
            return itemList
        
    def write_file(self, content):
        with open(self.__file_path, 'w') as file:
            file.write(content)
    
    def append_to_file(self, content):
        with open(self.__file_path, 'a') as file:
            file.write(f"{content.name};{content.price}\n")