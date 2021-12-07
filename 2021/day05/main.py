import re

line_regex = r'(.*),(.*) -> (.*),(.*)'

class Line:
    def as_set(self):
        coord_list = []
        for x in range(self.x1, self.x2 + 1):
            for y in range(self.y1, self.y2 + 1):
                coord_list.append((x,y))
        self.line_set = set(coord_list)

    def __init__(self, text_line):
        matches = re.findall(line_regex, text_line)
        coord_list = list(matches[0])
        if coord_list[0] < coord_list[2] or coord_list[1] < coord_list[3]:
            self.x1 = int(coord_list[0])
            self.y1 = int(coord_list[1])
            self.x2 = int(coord_list[2])
            self.y2 = int(coord_list[3])
        else:
            self.x1 = int(coord_list[2])
            self.y1 = int(coord_list[3])
            self.x2 = int(coord_list[0])
            self.y2 = int(coord_list[1])
    
    def is_line_straight(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def is_lines_crossing(self, line_2, busy_dict):
        intersection_list = list(self.line_set.intersection(line_2.line_set))
        for busy_point in intersection_list:
            if busy_point not in busy_dict:
                busy_dict[busy_point] = 1


def part_1():
    line_segments = []

    # initiate list
    #with open("input_test.txt") as _file:
    with open("input.txt") as _file:
        for text_line in _file:
            line_seg = Line(text_line)
            if line_seg.is_line_straight():
                line_seg.as_set()
                line_segments.append(line_seg)

    # find line crossings
    busy_dict = {}
    number_of_lines = len(line_segments)
    for i in range(number_of_lines):
        for j in range(i+1, number_of_lines):
            print(i, j)
            line_segments[i].is_lines_crossing(line_segments[j], busy_dict)
    
    return len(busy_dict)


print(part_1()) # 6676 wrong answer