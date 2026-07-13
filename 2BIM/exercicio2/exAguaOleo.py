from manim import *

class Exercicio10(Scene):
    def construct(self):

        # ===========================
        # Título
        # ===========================

        titulo = Title("Exercício 10 - EsPCEx (Cone com Água e Óleo)")
        self.play(Write(titulo))
        self.wait()

        # ===========================
        # Desenho do cone
        # ===========================

        topo_esq = LEFT*2 + UP*2
        topo_dir = RIGHT*2 + UP*2
        vertice = DOWN*2

        cone = VGroup(
            Line(topo_esq, vertice),
            Line(topo_dir, vertice),
            Line(topo_esq, topo_dir)
        )

        interface = DashedLine(
            LEFT*1 + ORIGIN,
            RIGHT*1 + ORIGIN
        )

        agua = Text("Água", font_size=30).move_to(DOWN*1)
        oleo = Text("Óleo", font_size=30).move_to(UP*1)

        self.play(Create(cone))
        self.play(Create(interface))
        self.play(FadeIn(agua), FadeIn(oleo))

        self.wait(2)

        # ===========================
        # Informações iniciais
        # ===========================

        info = MathTex(
            r"\text{Interface na metade da altura: }",
            r"\frac{h}{2}"
        ).to_edge(RIGHT)

        self.play(Write(info))
        self.wait(2)

        # ===========================
        # Volume da água
        # ===========================

        self.play(FadeOut(info))

        titulo2 = Tex("Volume da água").to_edge(UP)

        self.play(ReplacementTransform(titulo, titulo2))

        eq1 = MathTex(
            r"r=\frac{R}{2}"
        )

        eq2 = MathTex(
            r"V_{agua}",
            "=",
            r"\frac13\pi\left(\frac R2\right)^2\left(\frac h2\right)"
        ).next_to(eq1,DOWN)

        eq3 = MathTex(
            r"V_{agua}=",
            r"\frac1{24}\pi R^2h"
        ).next_to(eq2,DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.play(Write(eq3))

        self.wait(3)

        # ===========================
        # Volume do óleo
        # ===========================

        self.play(
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3)
        )

        titulo3 = Tex("Volume do óleo").to_edge(UP)

        self.play(ReplacementTransform(titulo2,titulo3))

        eq4 = MathTex(
            r"V_{cone}",
            "=",
            r"\frac13\pi R^2h"
        )

        eq5 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi R^2h-\frac1{24}\pi R^2h"
        ).next_to(eq4,DOWN)

        eq6 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac7{24}\pi R^2h"
        ).next_to(eq5,DOWN)

        self.play(Write(eq4))
        self.play(Write(eq5))
        self.play(Write(eq6))

        self.wait(3)

        # ===========================
        # Novo cone de óleo
        # ===========================

        self.play(
            FadeOut(eq4),
            FadeOut(eq5),
            FadeOut(eq6)
        )

        titulo4 = Tex("Após escoar toda a água").to_edge(UP)
        self.play(ReplacementTransform(titulo3,titulo4))

        eq7 = MathTex(
            r"x=",
            r"\text{altura do óleo}"
        )

        eq8 = MathTex(
            r"r=\frac{R}{h}x"
        ).next_to(eq7,DOWN)

        eq9 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi\left(\frac{R}{h}x\right)^2x"
        ).next_to(eq8,DOWN)

        eq10 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi R^2\frac{x^3}{h^2}"
        ).next_to(eq9,DOWN)

        self.play(Write(eq7))
        self.play(Write(eq8))
        self.play(Write(eq9))
        self.play(Write(eq10))

        self.wait(3)

        # ===========================
        # Igualando volumes
        # ===========================

        self.play(
            FadeOut(eq7),
            FadeOut(eq8),
            FadeOut(eq9),
            FadeOut(eq10)
        )

        titulo5 = Tex("Igualando os volumes").to_edge(UP)

        self.play(ReplacementTransform(titulo4,titulo5))

        e1 = MathTex(
            r"\frac13\pi R^2\frac{x^3}{h^2}",
            "=",
            r"\frac7{24}\pi R^2h"
        )

        e2 = MathTex(
            r"\frac{x^3}{h^2}",
            "=",
            r"\frac78h"
        ).next_to(e1,DOWN)

        e3 = MathTex(
            r"x^3",
            "=",
            r"\frac78h^3"
        ).next_to(e2,DOWN)

        e4 = MathTex(
            r"x",
            "=",
            r"\sqrt[3]{\frac78}h"
        ).next_to(e3,DOWN)

        e5 = MathTex(
            r"x",
            "=",
            r"\frac{\sqrt[3]{7}}{2}h"
        ).next_to(e4,DOWN)

        self.play(Write(e1))
        self.wait()

        self.play(Write(e2))
        self.wait()

        self.play(Write(e3))
        self.wait()

        self.play(Write(e4))
        self.wait()

        self.play(Write(e5))

        self.wait(3)

        # ===========================
        # Resultado Final
        # ===========================

        caixa = SurroundingRectangle(e5,color=YELLOW)

        resultado = Tex(
            "Resposta"
        ).next_to(caixa,UP)

        self.play(Create(caixa))
        self.play(Write(resultado))

        self.wait(4)