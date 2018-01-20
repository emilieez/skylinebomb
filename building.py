class Building():
    coords = {}

    def __init__(self, left, height, right):
        self.left = left
        self.height = height
        self.right = right

        Building.coords[(left, right)] = height

    def get_height(self, base):
        return Building.coords[base]

    def __str__(self):
        return "{} {} {}".format(self.left, self.height, self.right)
