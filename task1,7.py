class PhoneBook:

    def __init__(self):
        self.size = 10
        self.table = []
        for i in range(self.size):
            self.table.append([])

    def hash_function(self, name):
        total = 0
        for char in name:
            total += ord(char)
        return total % self.size

    def add_contact(self, name, phone):
        index = self.hash_function(name)
        self.table[index].append([name, phone])

    def get_contact(self, name):
        index = self.hash_function(name)
        for contact in self.table[index]:
            if contact[0] == name:
                return contact[1]
        return "Контакт не знайдено"

    def remove_contact(self, name):
        index = self.hash_function(name)
        for contact in self.table[index]:
            if contact[0] == name:
                self.table[index].remove(contact)

    def count_contacts(self):
        count = 0
        for bucket in self.table:
            count += len(bucket)
        return count


book = PhoneBook()
book.add_contact("Іван", "0971111111")
book.add_contact("Олег", "0662222222")

print(book.get_contact("Іван"))
book.remove_contact("Олег")

print(book.count_contacts())
