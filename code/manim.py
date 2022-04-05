from manimlib import *


class FlyingDot(Scene):
    def construct(self):
        number_plane = NumberPlane(
            (-10, 10),
            (-5, 5),
            background_line_style={
                "stroke_color": BLUE,  # Цвет линии
                "stroke_width": 2,  # Ширина линии
                "stroke_opacity": 1  # Прозрачность
            },
            faded_line_ratio=1  # Кол-во линий в одном квадрате
        )
        self.add(number_plane)

