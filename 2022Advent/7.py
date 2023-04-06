f = open("inputs/7input.txt", "r").read().splitlines()


# Implement Tree
class Tree:
    def __init__(self, data, parent):
        self.children = []
        self.data = data
