import matplotlib.pyplot as plt

class Segment:

    def __init__(self, line):
        self.line = line
        self.segments = []
        self.straight = True
        self.horizontal = set_horizontalness()
        self.forward = set_forwardness()

    def fractalize(self):
          # Get the endpoints of the segments line to calculate the endpoints of each smaller segment
        x1 = self.line[0][0]
        x2 = self.line[0][1]
        y1 = self.line[1][0]
        y2 = self.line[1][1]

        if self.straight:
            if self.horizontal:
                ul = (x2 - x1) / 3
                t_height = ((3 ** 0.5)/2) * ul
                seg1 = Segment( [[x1,      x1 + ul],       [y1, y1]])
                seg2 = Segment( [[x1 + ul, x1 + (3/2)*ul], [y1, y1 + t_height]])
                seg3 = Segment( [[x1 +     (3/2)*ul],      [y1 + t_height, y1]])
                seg4 = Segment( [[x1 +     2*ul, x2],      [y1, y1]])

            elif self.forward:
                pass
            elif not self.forward:
                pass

            self.segments = [seg1, seg2, seg3, seg4]
            self.straight = False

        # If segment isn't already straight, call .fractalize on each segment
        else:
            for segment in self.segments:
                segment.fractalize()


def plot_fractal(seg):
    if seg.straight:
        plt.plot(seg.line[0], seg.line[1])
    else:
        for seg in seg.segments:
            plot_fractal(seg)

def make_fractal(first_line, iterations):
    pass

first_line = [[0, 4], [1, 1]]
main_segment = Segment(first_line)
main_segment.fractalize()

plot_fractal(main_segment)

plt.show()