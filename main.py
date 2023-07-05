from manim import *

class TransformEquations(Scene):
    def construct(self):

        expression1 = "-\\frac{\pi }{2}"
        expression2 = "+\\frac{\pi }{2}=0"

        expression3 = "0"
        expression4 = "+\\frac{\pi }{2}=\\frac{\pi }{2}"

        expression5 = "\\frac{\pi }{2}"
        expression6 = "+\\frac{\pi }{2}=\pi"

        expression7 = "\pi"
        expression8 = "+\\frac{\pi }{2}=\\frac{3\pi }{2}"

        expression9 = "\\frac{3\pi }{2}"
        expression10 = "+\\frac{\pi }{2}=2\pi"

        equation_1 = MathTex(expression1 + "" + expression2)
        equation_2 = MathTex(expression3 + "" + expression4)
        equation_3 = MathTex(expression5 + "" + expression6)
        equation_4 = MathTex(expression7 + "" + expression8)
        equation_5 = MathTex(expression9 + "" + expression10)

        self.play(Write(equation_1))
        
        self.play(Transform(equation_1, equation_2))
        self.play(FadeOut(equation_1, equation_2), run_time=0.3)
        
        self.play(Write(equation_3))

        self.play(Transform(equation_3, equation_4))
        self.play(FadeOut(equation_3, equation_4), run_time=0.3)

        self.play(Write(equation_5))

        self.wait(1)
