import matplotlib.pyplot as plt

class Segment:
    """
    Each piece of the fractal is one 'segment', whether it's a single line (at the base) or made up
    of smaller segments.
    line -- A 2D array of colummn vectors representing points on a grid. The two points together
            represent one line segment.
    """
    def __init__(self, line):
        self.line = line
        self.segments = []
        self.straight = True
        if line[1][0] == line[1][1]:
            self.horizontal = True
        else:
            self.horizontal = False

    def fractalize(self):
        """
        Breaks up the segment into eight smaller lines if the segment is a straight line. If the segment
        is made up of segments already, then .fractalize is called on each segment. So, everytime
        .fractalize is called on the main_segment/orginal line, it breaks up each smallest line in the
        fractal into eight smaller lines.
        """
        # Get the endpoints of the segments line to calculate the endpoints of each smaller segment
        x1 = self.line[0][0]
        x2 = self.line[0][1]
        y1 = self.line[1][0]
        y2 = self.line[1][1]

        if self.straight:
            if self.horizontal:
                # ul is the length of one the smaller lines that is being created.
                ul = (x2-x1) / 4
                x1_ul = x1 + ul
                x2__ul = x2 - ul
                x1_2ul = x1 + ul + ul
                y1_ul = y1 + ul
                y1__ul = y1 - ul
                y2__ul = y2 - ul
                seg1 = Segment( [[x1,     x1_ul],  [y1,     y1]] )
                seg2 = Segment( [[x1_ul,  x1_ul],  [y1,     y1_ul]] )
                seg3 = Segment( [[x1_ul,  x1_2ul], [y1_ul,  y1_ul]] )
                seg4 = Segment( [[x1_2ul, x1_2ul], [y1_ul,  y1]] )
                seg5 = Segment( [[x1_2ul, x1_2ul], [y1,     y1__ul]])
                seg6 = Segment( [[x1_2ul, x2__ul], [y1__ul, y2__ul]] )
                seg7 = Segment( [[x2__ul, x2__ul], [y2__ul, y2]] )
                seg8 = Segment( [[x2__ul, x2],     [y2,     y2]] )
                
            else:
                ul = (y2-y1) / 4
                x1_ul = x1 + ul
                x2_ul = x2 + ul
                x1__ul = x1 - ul
                y1_ul = y1 + ul
                y1__ul = y1 - ul
                y1_2ul = y1 + ul + ul
                y2__ul = y2 - ul
                seg1 = Segment( [[x1,     x1],     [y1,     y1_ul]] )
                seg2 = Segment( [[x1,     x1__ul], [y1_ul, y1_ul]] )
                seg3 = Segment( [[x1__ul, x1__ul], [y1_ul, y1_2ul]] )
                seg4 = Segment( [[x1__ul, x1],     [y1_2ul, y1_2ul]] )
                seg5 = Segment( [[x1,     x1_ul],  [y1_2ul, y1_2ul]] )
                seg6 = Segment( [[x1_ul,  x1_ul],  [y1_2ul, y2__ul]] )
                seg7 = Segment( [[x2_ul,  x2],     [y2__ul, y2__ul]] )
                seg8 = Segment( [[x2,     x2],     [y2__ul, y2]] )

            self.segments = [seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8]
            self.straight = False

        else:
            for segment in self.segments:
                segment.fractalize()

def plot_fractal(seg):
    """
    Once the fractal is made to the desired number of iterations, plot_fractal recursively goes
    through each segment and plots it if it's straight, and calls itself it again on each segment
    if the it's not just a line.
    """
    if seg.straight:
        plt.plot(seg.line[0], seg.line[1], color=(0,0,0))
    else:
        for seg in seg.segments:
            plot_fractal(seg)

def make_fractal(first_line, iterations):
    """Calls .fractalize on the original line segment a number of times equal to iterations."""
    main_segment = Segment(first_line)
    for i in range(iterations):
        main_segment.fractalize()
    return main_segment

first_line = [[0, 4], [1, 1]]
main_segment = make_fractal(first_line, 4)
plot_fractal(main_segment)
plt.show()