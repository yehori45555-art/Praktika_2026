class Deque:

    def __init__(self):
        self.items = []
    def add_front(self, item):
        self.items.insert(0, item)
    def add_rear(self, item):
        self.items.append(item)
    def remove_front(self):
        return self.items.pop(0)
    def remove_rear(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(phrase: str) -> bool:

    dq = Deque()
    cleaned = ""

    for char in phrase:

        if char.isalnum():
            cleaned += char.lower()

    for char in cleaned:
        dq.add_rear(char)

    while len(dq.items) > 1:
        front = dq.remove_front()
        rear = dq.remove_rear()

        if front != rear:
            return False
    return True

text = input("Введіть фразу: ")

if is_palindrome(text):
    print("Це паліндром")
else:
    print("Це не паліндром")
