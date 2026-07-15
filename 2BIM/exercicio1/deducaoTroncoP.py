from manim import *

class DeducaoTroncoPiramide(Scene):

    def construct(self):

        # =======================================================
        # TÍTULO
        # =======================================================

        titulo = Tex(
            "Dedução da Fórmula do Tronco da Pirâmide"
        ).scale(0.8).to_edge(UP, buff=0.7)

        self.play(Write(titulo))
        self.wait(1)
        self.play(FadeOut(titulo))

        # =======================================================
        # DESENHO DA PIRÂMIDE
        # =======================================================

        A = UP * 3

        B1 = LEFT * 2 + DOWN * 2
        B2 = RIGHT * 2 + DOWN * 2
        B3 = RIGHT * 1.2 + DOWN * 3
        B4 = LEFT * 1.2 + DOWN * 3

        base = Polygon(
            B1, B2, B3, B4,
            color=BLUE
        )

        arestas = VGroup(
            Line(A, B1),
            Line(A, B2),
            Line(A, B3),
            Line(A, B4)
        )

        piramide = VGroup(base, arestas)

        self.play(Create(piramide))
        self.wait(2)

        # =======================================================
        # PLANO DE CORTE
        # =======================================================

        C1 = interpolate(A, B1, 0.45)
        C2 = interpolate(A, B2, 0.45)
        C3 = interpolate(A, B3, 0.45)
        C4 = interpolate(A, B4, 0.45)

        corte = Polygon(
            C1, C2, C3, C4,
            color=YELLOW,
            fill_opacity=0.35
        )

        self.play(FadeIn(corte))

        texto = Tex(
            "Plano paralelo à base"
        ).scale(0.8).to_edge(RIGHT)

        self.play(Write(texto))

        self.wait(2)

        # =======================================================
        # TRONCO
        # =======================================================

        self.play(FadeOut(texto))

        tronco = VGroup(

            Polygon(
                C1, C2, C3, C4,
                color=YELLOW
            ),

            Polygon(
                B1, B2, B3, B4,
                color=BLUE
            ),

            Line(C1, B1),
            Line(C2, B2),
            Line(C3, B3),
            Line(C4, B4)

        )

        self.play(Create(tronco))

        self.wait(2)

        # =======================================================
        # DEFINIÇÕES
        # =======================================================

        self.play(
            FadeOut(piramide),
            FadeOut(tronco),
            FadeOut(corte)
        )

        definicoes = VGroup(

            MathTex(
                r"S_B",
                "=",
                r"\text{área da base maior}"
            ),

            MathTex(
                r"S_b",
                "=",
                r"\text{área da base menor}"
            ),

            MathTex(
                r"H",
                "=",
                r"\text{altura da pirâmide completa}"
            ),

            MathTex(
                r"h",
                "=",
                r"\text{altura da pirâmide menor}"
            ),

            MathTex(
                r"k",
                "=",
                r"H-h",
                r"\quad\text{(altura do tronco)}"
            )

        ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

        self.play(Write(definicoes))

        self.wait(3)

        # =======================================================
        # SEMELHANÇA
        # =======================================================

        self.play(FadeOut(definicoes))

        titulo2 = Tex(
            "Semelhança de Pirâmides"
        )

        s2 = MathTex(
            r"\frac{S_b}{S_B}",
            "=",
            r"\left(\frac{h}{H}\right)^2"
        )

        s3 = MathTex(
            r"\frac{h}{H}",
            "=",
            r"\sqrt{\frac{S_b}{S_B}}",
            "=",
            r"\frac{\sqrt{S_b}}{\sqrt{S_B}}"
        )

        s4 = MathTex(
            r"h",
            "=",
            r"H\frac{\sqrt{S_b}}{\sqrt{S_B}}"
        )

        semelhanca_group = VGroup(titulo2, s2, s3, s4).arrange(DOWN, buff=0.25).move_to(UP * 0.05)

        self.play(Write(semelhanca_group))

        self.wait(4)

        # =======================================================
        # VOLUMES
        # =======================================================

        self.play(
            FadeOut(semelhanca_group[1:])
        )

        titulo3 = Tex(
            "Volumes das Pirâmides"
        )

        self.play(
            ReplacementTransform(titulo2, titulo3)
        )

        v1 = MathTex(
            r"V_{\text{maior}}",
            "=",
            r"\frac13S_BH"
        )

        v2 = MathTex(
            r"V_{\text{menor}}",
            "=",
            r"\frac13S_bh"
        )

        v3 = MathTex(
            r"V_{\text{tronco}}",
            "=",
            r"V_{\text{maior}}-V_{\text{menor}}"
        )

        volumes_group = VGroup(titulo3, v1, v2, v3).arrange(DOWN, buff=0.25).move_to(UP * 0.05)

        self.play(Write(volumes_group[1:]))

        self.wait(4)

        # =======================================================
        # SUBSTITUINDO h
        # =======================================================

        self.play(
            FadeOut(v1),
            FadeOut(v2),
            FadeOut(v3)
        )

        titulo4 = Tex(
            "Substituindo a altura da pirâmide menor"
        )

        self.play(
            ReplacementTransform(titulo3, titulo4)
        )

        e1 = MathTex(
            r"V",
            "=",
            r"\frac13",
            r"\left(",
            r"S_BH",
            "-",
            r"S_bH\frac{\sqrt{S_b}}{\sqrt{S_B}}",
            r"\right)"
        )

        e2 = MathTex(
            r"V",
            "=",
            r"\frac{H}{3}",
            r"\left(",
            r"S_B",
            "-",
            r"\frac{S_b^{3/2}}{\sqrt{S_B}}",
            r"\right)"
        )

        substituicao_h_group = VGroup(titulo4, e1, e2).arrange(DOWN, buff=0.25).move_to(UP * 0.05)

        self.play(Write(substituicao_h_group[1:]))

        self.wait(4)

        # =======================================================
        # ELIMINANDO H
        # =======================================================

        self.play(
            FadeOut(e1),
            FadeOut(e2)
        )

        titulo5 = Tex(
            "Usando a relação  $k=H-h$"
        )

        self.play(
            ReplacementTransform(titulo4, titulo5)
        )

        e3 = MathTex(
            r"k",
            "=",
            r"H",
            r"\left(",
            r"1-\frac{\sqrt{S_b}}{\sqrt{S_B}}",
            r"\right)"
        )

        e4 = MathTex(
            r"H",
            "=",
            r"\frac{k\sqrt{S_B}}{\sqrt{S_B}-\sqrt{S_b}}"
        )

        eliminando_H_group = VGroup(titulo5, e3, e4).arrange(DOWN, buff=0.25).move_to(UP * 0.05)

        self.play(Write(eliminando_H_group[1:]))

        self.wait(4)

        # =======================================================
        # SUBSTITUINDO H
        # =======================================================

        self.play(
            FadeOut(e3),
            FadeOut(e4)
        )

        titulo6 = Tex(
            "Substituindo $H$ na expressão do volume"
        )

        self.play(
            ReplacementTransform(titulo5, titulo6)
        )

        r1 = MathTex(
            r"V",
            "=",
            r"\frac{k}{3}",
            r"\cdot",
            r"\frac{S_B^{3/2}-S_b^{3/2}}{\sqrt{S_B}-\sqrt{S_b}}"
        )

        r2 = MathTex(
            r"S_B^{3/2}-S_b^{3/2}",
            "=",
            r"(\sqrt{S_B}-\sqrt{S_b})",
            r"(S_B+\sqrt{S_BS_b}+S_b)"
        )

        r3 = MathTex(
            r"V",
            "=",
            r"\frac{k}{3}",
            r"\left(",
            r"S_B+\sqrt{S_BS_b}+S_b",
            r"\right)"
        )

        substituicao_H_group = VGroup(titulo6, r1, r2, r3).arrange(DOWN, buff=0.25).move_to(UP * 0.05)

        self.play(Write(substituicao_H_group[1:]))

        self.wait(3)

        # =======================================================
        # RESULTADO FINAL
        # =======================================================

        resultado = MathTex(
            r"\boxed{V_{\text{tronco}}=\frac{k}{3}\left(S_B+\sqrt{S_BS_b}+S_b\right)}"
        ).scale(1.25)

        conclusao = Tex(
            "Fórmula do Volume do Tronco de Pirâmide"
        ).scale(0.8)

        final_group = VGroup(conclusao, resultado).arrange(DOWN, buff=0.3).move_to(ORIGIN)

        caixa = SurroundingRectangle(
            resultado,
            color=YELLOW,
            buff=0.2
        )

        self.play(
            FadeOut(substituicao_H_group),
            FadeOut(titulo6)
        )

        self.play(Write(final_group))
        self.play(Create(caixa))

        self.wait(5)
        