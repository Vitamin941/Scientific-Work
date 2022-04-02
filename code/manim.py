from manim import *


class Axes(Scene):

    def construct(self):
        my_plane = NumberPlane()
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        self.wait(10)