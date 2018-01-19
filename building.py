class Building():
    def __init__(self, left, height, right):
        self.left = left
        self.height = height
        self.right = right

    def __str__(self):
        return "{} {} {}".format(self.left, self.height, self.right)