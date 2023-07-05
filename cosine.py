from manim import *

class Myscene(Scene):
    def construct(self):
        axes = Axes()
        
        p1 = MathTex('\pi/2}').scale(0.6).move_to(axes.coords_to_point(PI/2, -0.5))
        p2 = MathTex('\pi').scale(0.6).move_to(axes.coords_to_point(PI, -0.5))
        p3 = MathTex('3\pi/2').scale(0.6).move_to(axes.coords_to_point(3*PI/2, -0.5))
        p4 = MathTex('2\pi').scale(0.6).move_to(axes.coords_to_point(2*PI, -0.5))
        
        p5 = MathTex('-\pi/2}').scale(0.6).move_to(axes.coords_to_point(-PI/2, -0.5))
        p6 = MathTex('-\pi').scale(0.6).move_to(axes.coords_to_point(-PI, -0.5))
        p7 = MathTex('-3\pi/2').scale(0.6).move_to(axes.coords_to_point(-3*PI/2, -0.5))
        p8 = MathTex('-2\pi').scale(0.6).move_to(axes.coords_to_point(-2*PI, -0.5)) 
                
        y_label = axes.get_y_axis_label("y")
        x_label = axes.get_x_axis_label("x")
        
        self.add(p1, p2, p3, 
                  p4, p5, p6,
                  p7, p8, y_label, x_label)
                          
        self.add(axes)
        
        graph = axes.plot(lambda x: np.cos(x), color = BLUE,
            x_range = [-2*PI, 2*PI]                
        )
        self.add(graph)
