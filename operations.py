from manim import *

class Equations(Scene):
    def construct(self):
        equation_1 = MathTex("2\pi - \\frac{\pi}{2} = \\frac{3\pi}{2}")
        equation_1.move_to(ORIGIN)

        self.play(Write(equation_1))
        self.wait(1)
        self.play(FadeOut(equation_1))
        self.wait(1)

        equation_2 = MathTex("x = \sin^{-1}\left(\\frac{1}{4}\\right)")
        equation_2.move_to(ORIGIN)

        self.play(Write(equation_2))
        self.wait(1)

        equation_2_transformed = MathTex("x = 0.25268 + 2k\pi")
        equation_2_transformed.move_to(ORIGIN)

        self.play(Transform(equation_2, equation_2_transformed))
        self.wait(1)
        self.play(FadeOut(equation_2))
        self.wait(1)

        equation_3 = MathTex("x = \pi - \sin^{-1}\left(\\frac{1}{4}\\right)")
        equation_3.move_to(ORIGIN)

        self.play(Write(equation_3))
        self.wait(1)

        equation_3_transformed = MathTex("x = 2.88891 + 2k\pi")
        equation_3_transformed.move_to(ORIGIN)

        self.play(Transform(equation_3, equation_3_transformed))
        self.wait(1)
        self.play(FadeOut(equation_3))
        self.wait(1)

        equations_list = MathTex(r"x = \frac{3\pi}{2} + 2k\pi,", r"x = 0.25268 + 2k\pi,", r"x = 2.8881 + 2k\pi",
                                r"K \in \mathbb{Z}")
        equations_list.arrange(DOWN, center=True)

        self.play(Write(equations_list))
        self.wait(2)
