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

        cone_group = VGroup(cone, interface, agua, oleo).to_edge(LEFT, buff=1.5)

        self.play(Create(cone_group))

        self.wait(2)

        # ===========================
        # Informações iniciais
        # ===========================

        info = MathTex(
            r"\text{Interface na metade da altura: }",
            r"\frac{h}{2}"
        ).to_edge(RIGHT, buff=1.5).shift(UP*0.15)

        self.play(Write(info))
        self.wait(2)

        # ===========================
        # Volume da água
        # ===========================

        self.play(FadeOut(info))

        titulo2 = Tex("Volume da água").to_edge(UP, buff=0.7)

        eq1 = MathTex(
            r"r=\frac{R}{2}"
        )

        eq2 = MathTex(
            r"V_{agua}",
            "=",
            r"\frac13\pi\left(\frac R2\right)^2\left(\frac h2\right)"
        )

        eq3 = MathTex(
            r"V_{agua}=",
            r"\frac1{24}\pi R^2h"
        )

        agua_group = VGroup(eq1, eq2, eq3).arrange(DOWN, buff=0.25).next_to(titulo2, DOWN, buff=0.35).shift(RIGHT*1.0)

        self.play(ReplacementTransform(titulo, titulo2))
        self.play(Write(agua_group))

        self.wait(3)

        # ===========================
        # Volume do óleo
        # ===========================

        self.play(
            FadeOut(agua_group)
        )

        titulo3 = Tex("Volume do óleo").to_edge(UP, buff=0.7)

        eq4 = MathTex(
            r"V_{cone}",
            "=",
            r"\frac13\pi R^2h"
        )

        eq5 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi R^2h-\frac1{24}\pi R^2h"
        )

        eq6 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac7{24}\pi R^2h"
        )

        oleo_group = VGroup(eq4, eq5, eq6).arrange(DOWN, buff=0.25).next_to(titulo3, DOWN, buff=0.35).shift(RIGHT*1.0)

        self.play(ReplacementTransform(titulo2,titulo3),
                  Write(oleo_group))

        self.wait(3)

        # ===========================
        # Novo cone de óleo
        # ===========================

        self.play(
            FadeOut(oleo_group)
        )

        titulo4 = Tex("Após escoar toda a água").to_edge(UP, buff=0.7)
        self.play(ReplacementTransform(titulo3,titulo4))

        eq7 = MathTex(
            r"x=",
            r"\text{altura do óleo}"
        )

        eq8 = MathTex(
            r"r=\frac{R}{h}x"
        )

        eq9 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi\left(\frac{R}{h}x\right)^2x"
        )

        eq10 = MathTex(
            r"V_{oleo}",
            "=",
            r"\frac13\pi R^2\frac{x^3}{h^2}"
        )

        escoar_group = VGroup(eq7, eq8, eq9, eq10).arrange(DOWN, buff=0.25).next_to(titulo4, DOWN, buff=0.35).shift(RIGHT*1.0)

        self.play(Write(escoar_group))

        self.wait(3)

        # ===========================
        # Igualando volumes
        # ===========================

        self.play(
            FadeOut(escoar_group)
        )

        titulo5 = Tex("Igualando os volumes").to_edge(UP, buff=0.7)

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

        igualando_group = VGroup(e1, e2, e3, e4, e5).arrange(DOWN, buff=0.18).next_to(titulo5, DOWN, buff=0.28).shift(RIGHT*1.2)

        self.play(Write(igualando_group))
        self.wait(3)

        # ===========================
        # Resultado Final
        # ===========================

        final_answer = MathTex(r"x = \frac{\sqrt[3]{7}}{2}h")
        final_label = Tex("Resposta").scale(0.8)
        final_group = VGroup(final_label, final_answer).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        caixa = SurroundingRectangle(final_answer, color=YELLOW, buff=0.3)

        self.play(
            FadeOut(igualando_group),
            FadeOut(titulo5)
        )
        self.play(Write(final_group))
        self.play(Create(caixa))

        self.wait(4)