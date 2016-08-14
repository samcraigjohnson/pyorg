"""
Helpful functions to deal with org-files
"""


class Location(object):
    """ Class to store a location inside of a org-file """

    def __init__(self, heading=None, at_top=True):
        self.heading = heading
        self.at_top = at_top

    def __str__(self):
        return "<Location heading='{}' at_top={}>".format(
            self.heading,
            self.at_top
        )

    def find_line_number_and_level(self, lines):
        """ Return line number of location in file """
        if not self.heading:
            if self.at_top:
                return 0, 1
            else:
                return len(lines) - 1, 1

        level = 0
        found_heading = False
        for i, line in enumerate(lines):

            # TODO handle at_top == False
            if found_heading and self.get_level(line) > 0:
                return i-1, level+1

            if self.heading in line:
                found_heading = True
                level = self.get_level(line)

        raise "Location not found"

    def get_level(self, line):
        if len(line) == 0 or not '*' == line[0]:
            return -1
        return len(line.split(' ')[0])

def add_todo(org_file, task, location=None):
    """ Add a TODO to a file """

    if not location:
        location = Location()

    with open(org_file, 'r') as f:
        lines = f.read().split('\n')
        line_num, level = location.find_line_number_and_level(lines)

    level_format = '*' * level
    todo = "{} TODO {}".format(level_format, task)

    lines.insert(line_num, todo)

    with open(org_file, 'w') as f:
        f.write('\n'.join(lines))
