from building import Building


class Skyline:
    def __init__(self):
        self.sky_vector = []
        return

    def add(self, new_building):
        # pad the sky vector with zeros so we can add new heights to the end
        for posn in range(len(self.sky_vector), new_building.right):
            self.sky_vector.append(0)

        # scan left to right and update height if > old_height
        for posn in range(new_building.left, new_building.right):
            if new_building.height >= self.sky_vector[posn]:
                self.sky_vector[posn] = new_building.height

        # add a trailing 0
        self.sky_vector.append(0)

    def __str__(self):
        sky_string = ''
        current_height = 0
        for posn, height in enumerate(self.sky_vector):
            if height != current_height:
                sky_string += str(posn) + ' ' + str(height) + ' '
                current_height = height
        return sky_string.strip()
