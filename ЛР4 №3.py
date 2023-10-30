class Room:
    def __init__(self, lenght, width, height, num_of_windows, window_height,
                 window_width, num_of_doors, door_height, door_width):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.num_of_windows = num_of_windows
        self.window_height = window_height
        self.window_width = window_width
        self.num_of_doors = num_of_doors
        self.door_height = door_height
        self.door_width = door_width

    def calculate_wall_area(self):
        wall_area = self.lenght * self.height
        total_wall_area = 2 * wall_area + 2 * self.width * self.height

        total_wall_area -= self.num_of_windows * self.window_width * self.window_height
        total_wall_area -= self.num_of_doors * self.door_width * self.door_height

        return total_wall_area

room = Room(4, 5, 3, 1, 0.5, 0.5,
            1, 2, 1.5)

total_wall_area = room.calculate_wall_area()
print("Общая площадь стены:", total_wall_area)