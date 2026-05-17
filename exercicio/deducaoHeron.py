from manim import *
import math

class DeducaoFormulaHeron(Scene):
    def construct(self):

        titulo = Text("Dedução da Fórmula de Heron", font_size=40)
        self.play(Write(titulo))
        self.wait(1)
        self.play(titulo.animate.to_edge(UP))

        # Coordenadas do triângulo
        A = LEFT * 5 + DOWN * 2
        B = RIGHT * 1 + DOWN * 2
        C = LEFT * 2 + UP * 2

        # Triângulo
        triangulo = Polygon(A, B, C, color=BLUE)

        # Pontos
        pontoA = Dot(A)
        pontoB = Dot(B)
        pontoC = Dot(C)

        # Labels dos vértices
        labelA = MathTex("A").next_to(pontoA, DOWN)
        labelB = MathTex("B").next_to(pontoB, DOWN)
        labelC = MathTex("C").next_to(pontoC, UP)

        # Lados
        lado_a = MathTex("a").move_to((B + C) / 2 + RIGHT * 0.3)
        lado_b = MathTex("b").move_to((A + C) / 2 + LEFT * 0.3)
        lado_c = MathTex("c").move_to((A + B) / 2 + DOWN * 0.3)

        self.play(
            Create(triangulo),
            FadeIn(pontoA, pontoB, pontoC),
            Write(labelA),
            Write(labelB),
            Write(labelC),
            Write(lado_a),
            Write(lado_b),
            Write(lado_c),
        )

        self.wait(2)

        # Altura
        H = np.array([-2, -2, 0])

        altura = DashedLine(C, H, color=YELLOW)
        angulo = RightAngle(
            Line(H, B),
            Line(H, C),
            length=0.2,
            color=YELLOW
        )

        label_h = MathTex("h").next_to(altura, LEFT)

        self.play(Create(altura), Create(angulo), Write(label_h))
        self.wait(2)

        # Segmentos da base
        x_label = MathTex("x").next_to((A + H) / 2, DOWN)
        c_x_label = MathTex("c-x").next_to((H + B) / 2, DOWN)

        self.play(Write(x_label), Write(c_x_label))
        self.wait(2)

        # Equações
        eq1 = MathTex(
            "h^2 + x^2 = b^2"
        ).scale(0.9)

        eq2 = MathTex(
            "h^2 + (c-x)^2 = a^2"
        ).scale(0.9)

        eq_group = VGroup(eq1, eq2).arrange(DOWN, aligned_edge=LEFT)
        eq_group.to_edge(RIGHT)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(2)

        # Desenvolvendo
        eq3 = MathTex(
            "h^2 + c^2 - 2cx + x^2 = a^2"
        ).scale(0.9).to_edge(RIGHT)

        self.play(
            Transform(eq2, eq3)
        )
        self.wait(2)

        # Substituição
        eq4 = MathTex(
            "h^2 = b^2 - x^2"
        ).scale(0.9).to_edge(RIGHT)

        self.play(
            Transform(eq1, eq4)
        )
        self.wait(2)

        # Resolver x
        eq5 = MathTex(
            "b^2 - x^2 + c^2 - 2cx + x^2 = a^2"
        ).scale(0.8).to_edge(RIGHT)

        self.play(
            FadeOut(eq2),
            Transform(eq1, eq5)
        )
        self.wait(2)

        eq6 = MathTex(
            "x = \\frac{b^2 + c^2 - a^2}{2c}"
        ).scale(0.9).to_edge(RIGHT)

        self.play(Transform(eq1, eq6))
        self.wait(2)

        # Área
        area1 = MathTex(
            "A = \\frac{c \\cdot h}{2}"
        ).scale(0.9)

        area1.next_to(eq6, DOWN, aligned_edge=LEFT, buff=0.15)
        area1.shift(RIGHT * 0.05)

        self.play(Write(area1))
        self.wait(2)

        # Fórmula final
        formula_final = MathTex(
            "A = \\sqrt{p(p-a)(p-b)(p-c)}"
        ).scale(1.2).set_color(WHITE)

        definicao_p = MathTex(
            "p = \\frac{a+b+c}{2}"
        ).scale(1)

        grupo_final = VGroup(formula_final, definicao_p).arrange(DOWN)
        grupo_final.to_edge(RIGHT)

        self.play(
            FadeOut(eq1),
            FadeOut(area1),
            FadeOut(x_label),
            FadeOut(c_x_label),
            FadeOut(label_h),
            FadeOut(altura),
            FadeOut(angulo),
        )

        self.play(
            triangulo.animate.shift(LEFT * 0.5),
            pontoA.animate.shift(LEFT * 0.5),
            pontoB.animate.shift(LEFT * 0.5),
            pontoC.animate.shift(LEFT * 0.5),
            labelA.animate.shift(LEFT * 0.5),
            labelB.animate.shift(LEFT * 0.5),
            labelC.animate.shift(LEFT * 0.5),
            lado_a.animate.shift(LEFT * 0.5),
            lado_b.animate.shift(LEFT * 0.5),
            lado_c.animate.shift(LEFT * 0.5),
        )

        self.wait(1)

        self.play(Write(formula_final))
        self.wait(1)
        self.play(Write(definicao_p))

        self.wait(4)