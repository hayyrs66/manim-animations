from manim import *


class SinWave(Scene):
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
        
        
        
        self.play(Write(p1), Write(p2), Write(p3), 
                  Write(p4), Write(p5), Write(p6),
                  Write(p7), Write(p8))
                  
        self.play(Write(axes))
        

        graph = axes.plot(lambda x: np.sin(x), color = BLUE,
            x_range = [-2*PI, 2*PI]                
        )
        
        self.play(Write(graph), Write(y_label), Write(x_label), run_time=5)
        

        newGraph = axes.plot(lambda x: np.sin(x), color = YELLOW,
            x_range = [-PI/2, 0]                
        )
         
        whiteGraph = axes.plot(lambda x: np.sin(x), color = WHITE,
            x_range = [-2*PI, 2*PI],      
        )
        
        whiteGraph.set_stroke(opacity=0.2)
         
        self.play(Transform(graph, newGraph), run_time=1)
        self.play(Write(whiteGraph))
        self.wait(2)
        
        cutGraph = axes.plot(lambda x: np.sin(x), color = YELLOW,
            x_range = [PI, 3*PI/2]                
        )
        
        cutGraph_2 = axes.plot(lambda x: np.sin(x), color = YELLOW,
            x_range = [3*PI/2, 2*PI]                
        )
        
        # dot creation
        
        moving_dot = Dot(axes.i2gp(graph.t_min, graph), color=WHITE)

        self.add(moving_dot)

        def update_dot(dot):
            dot.move_to(axes.i2gp(moving_dot.get_center()[0], graph))

        moving_dot.add_updater(update_dot)

        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))

        moving_dot.clear_updaters()
       

        self.play(Transform(newGraph, cutGraph), run_time=1)
        self.wait(1)
        self.play(Transform(cutGraph, cutGraph_2), run_time=1)
        self.play(FadeOut(cutGraph_2), run_time=0.7)
        self.play(FadeOut(cutGraph), run_time=0.7)
        self.play(FadeOut(graph), run_time=0.7)
        self.play(FadeOut(newGraph), run_time=0.7)
        self.play(FadeOut(whiteGraph), run_time=0.7)
        self.play(FadeOut(moving_dot), run_time=0.7)

        
        self.wait(1)
        
        sinwave = axes.plot(lambda x: np.sin(x), color = PURPLE,
            x_range = [-2*PI, 2*PI]                
        )
        sinwave_white = axes.plot(lambda x: np.sin(x), color = WHITE,
            x_range = [-2*PI, 2*PI]                
        )
        
        sinwave_white.set_stroke(opacity=0.1)
        
        sinwave_cut = axes.plot(lambda x: np.sin(x), color = PURPLE,
            x_range = [0, 0.25268]                
        )
        
        sinwave_cut2 = axes.plot(lambda x: np.sin(x), color = PURPLE,
            x_range = [PI-0.25268, PI]                
        )
        
        self.play(Write(sinwave))
        self.wait(2)
        
        self.play(Transform(sinwave, sinwave_cut))
        self.wait(1.3)
        self.play(Transform(sinwave_cut, sinwave_cut2))
        self.wait(1.3)
        self.play(Write(sinwave_white))
        self.wait(1)
        self.play(FadeOut(axes))
        self.wait(2)
        
        
        
        
        
        
        
