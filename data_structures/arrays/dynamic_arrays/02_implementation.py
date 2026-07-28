'''
DYNAMIC ARRAY IMPLEMENTATION
'''
# ------------------------------------------------------------------------------
# python's built-in list
# ------------------------------------------------------------------------------
print("====================")
print("Example 1:")
print("====================")

arr = []

# grow array with append
arr.append(10)
arr.append(20)
arr.append(30)

# access
print(arr[1]) # 20
print(f"arr[1]: {arr}")

# modify
arr[1] = 50

# remove from end of list
arr.pop()

print(f"pop last item: {arr}")

# ------------------------------------------------------------------------------
# operations with arrays
# ------------------------------------------------------------------------------
print("====================")
print("Example 2:")
print("====================")

# initialize with values
fruits = ['apple', 'banana', 'coconut']
print(fruits)

# iterate through array
for fruit in fruits:
    print(fruit)

# insert at an index
fruits.insert(2, 'cherry')
print(f"insert at index 2: {fruits}")

# remove by value
fruits.remove('coconut')
print(f"remove coconut: {fruits}")

# remove by index
removed = fruits.pop(1)
print(f"removed: {removed}")
print(f"fruits: {fruits}")

# search
numbers = [10, 20, 30]
print(f"is there a 20 in the array: {20 in numbers}")
print(f"index of 30: {numbers.index(30)}")

# ------------------------------------------------------------------------------
# manual dynamic array implementation
# ------------------------------------------------------------------------------
print("====================")
print("Example 3:")
print("====================")
class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.data = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize()

        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_data = [None] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    def get(self, index):
        if index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def __str__(self):
        return str(self.data[:self.size])


arr = DynamicArray()

arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)

print(arr)
print(arr.get(2))