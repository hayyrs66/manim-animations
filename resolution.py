from manim import *

class Equations(Scene):
    def construct(self):

        eq1 = MathTex("\cos^2(x) - \cos(x) - 1 = 1")
        eq2 = MathTex("\cos^2(x) - \cos(x) - 2 = 0")
        eq3 = MathTex("t^2 = \cos^2(x)")
        eq3 = MathTex("t = \cos(x)")
        eq4 = MathTex("t^2 - t - 2 = 0")
        eq5 = MathTex("t = -1, \quad t = 2")
        eq6 = MathTex("\cos(x) = -1")
        eq7 = MathTex("\cos(x) = 2")
        eq8 = MathTex("x = \cos^{-1}(-1)")
        eq9 = MathTex("x = \pi")
        eq10 = MathTex("x = \cos^{-1}(2)")
        eq11 = MathTex("x = \\text{Está fuera del dominio del coseno}")
        
        
        


        self.play(Write(eq11))
        self.wait()
