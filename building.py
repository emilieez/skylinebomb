class Building:
    coords = {}

    def __init__(self, left, height, right):
        self.left = left
        self.height = height
        self.right = right

        Building.coords[(left, right)] = height
