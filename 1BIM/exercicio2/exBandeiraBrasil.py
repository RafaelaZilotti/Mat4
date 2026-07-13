from manim import *

class BandeiraBrasil(Scene):
    def construct(self):

        titulo = Text(
            "Exercício da Bandeira do Brasil",
            font_size=40
        ).to_edge(UP)

        self.play(Write(titulo))
        self.wait(1)

        dados = VGroup(
            MathTex(r"\text{Retângulo: } 2\,m \times 1{,}40\,m"),
            MathTex(r"\text{Distância do losango às bordas: } 17\,cm = 0{,}17\,m"),
            MathTex(r"r = 35\,cm = 0{,}35\,m"),
            MathTex(r"\pi = \frac{22}{7}")
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8)

        dados.next_to(titulo, DOWN, buff=0.15).to_edge(LEFT)

        self.play(FadeIn(dados))
        self.wait(2)

        retangulo = Rectangle(
            width=6,
            height=4.2,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=1
        )

        losango = Polygon(
            [0, 1.6, 0],
            [2.4, 0, 0],
            [0, -1.6, 0],
            [-2.4, 0, 0],
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=1
        )

        circulo = Circle(
            radius=1.05,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1
        )

        bandeira = VGroup(retangulo, losango, circulo)
        bandeira.shift(RIGHT * 0.6 + DOWN * 0.7)

        self.play(DrawBorderThenFill(retangulo))
        self.play(DrawBorderThenFill(losango))
        self.play(DrawBorderThenFill(circulo))

        self.wait(1)

        self.play(
            FadeOut(dados),
            bandeira.animate.next_to(titulo, DOWN, buff=0.15).to_edge(LEFT, buff=0.08)
        )

        #   Exercicio a)
        item_a = Text(
            "a) Área pintada de verde",
            font_size=34
        ).next_to(titulo, DOWN, buff=0.15).to_edge(RIGHT).shift(LEFT * 0.05)

        self.play(Write(item_a))
        self.wait(0.5)

        # Área do retângulo
        area_ret = MathTex(
            r"A_{ret} = 2 \times 1{,}40"
        ).scale(0.8)
        
        area_ret_result = MathTex(
            r"A_{ret} = 2{,}8\,m^2"
        ).scale(0.8)

        area_ret.next_to(item_a, DOWN, aligned_edge=LEFT, buff=0.4)
        area_ret_result.next_to(area_ret, DOWN, aligned_edge=LEFT, buff=0.1)

        self.play(Write(area_ret))
        self.play(Write(area_ret_result))
        self.wait(1)

        # Dimensões do losango
        dimensoes_losango = MathTex(
            r"D = 2 - 2(0{,}17) = 1{,}66\,m"
        ).scale(0.8)

        dimensoes_losango2 = MathTex(
            r"d = 1{,}40 - 2(0{,}17) = 1{,}06\,m"
        ).scale(0.8)

        dimensoes = VGroup(
            dimensoes_losango,
            dimensoes_losango2
        ).arrange(DOWN, aligned_edge=LEFT)

        dimensoes.next_to(area_ret_result, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(dimensoes))
        self.wait(1)

        # Área do losango
        area_losango = MathTex(
            r"A_{losango} = \frac{1{,}66 \times 1{,}06}{2}"
        ).scale(0.8)

        area_losango2 = MathTex(
            r"A_{losango} = 0{,}8798\,m^2"
        ).scale(0.8)

        grupo_losango = VGroup(
            area_losango,
            area_losango2
        ).arrange(DOWN, aligned_edge=LEFT)

        grupo_losango.next_to(dimensoes, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(grupo_losango))
        self.wait(2)

        # Área verde
        area_verde = MathTex(
            r"A_{verde} = 2{,}8 - 0{,}8798"
        ).scale(0.8)

        area_verde2 = MathTex(
            r"\boxed{A_{verde} = 1{,}92\,m^2}"
        ).scale(0.9)

        grupo_verde = VGroup(
            area_verde,
            area_verde2
        ).arrange(DOWN, aligned_edge=LEFT)

        grupo_verde.next_to(grupo_losango, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(grupo_verde))
        self.wait(3)

            # Exercicio b)
        self.play(
            FadeOut(
                VGroup(
                    area_ret,
                    area_ret_result,
                    dimensoes,
                    grupo_losango,
                    grupo_verde,
                    item_a
                )
            )
        )

        item_b = Text(
            "b) Porcentagem da área amarela",
            font_size=34
        ).next_to(titulo, DOWN, buff=0.15).to_edge(RIGHT).shift(RIGHT * 0.5)

        self.play(Write(item_b))
        self.wait(1)

        # Área do círculo
        area_circulo = MathTex(
            r"A_{circ} = \frac{22}{7}(0{,}35)^2"
        ).scale(0.8)

        area_circulo2 = MathTex(
            r"A_{circ} = 0{,}385\,m^2"
        ).scale(0.8)

        grupo_circulo = VGroup(
            area_circulo,
            area_circulo2
        ).arrange(DOWN, aligned_edge=LEFT)

        grupo_circulo.next_to(item_b, DOWN, aligned_edge=LEFT, buff=0.3)

        self.play(Write(grupo_circulo))
        self.wait(2)

        # Área amarela
        area_amarela = MathTex(
            r"A_{amarela} = 0{,}8798 - 0{,}385"
        ).scale(0.8)

        area_amarela2 = MathTex(
            r"A_{amarela} = 0{,}4948\,m^2"
        ).scale(0.8)

        grupo_amarela = VGroup(
            area_amarela,
            area_amarela2
        ).arrange(DOWN, aligned_edge=LEFT)

        grupo_amarela.next_to(grupo_circulo, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(grupo_amarela))
        self.wait(2)

        # Porcentagem
        porcentagem = MathTex(
            r"\% = \frac{0{,}4948}{2{,}8} \times 100"
        ).scale(0.8)

        porcentagem2 = MathTex(
            r"\boxed{\% \approx 17{,}67\%}"
        ).scale(0.9)

        grupo_porcentagem = VGroup(
            porcentagem,
            porcentagem2
        ).arrange(DOWN, aligned_edge=LEFT)

        grupo_porcentagem.next_to(grupo_amarela, DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(Write(grupo_porcentagem))
        self.wait(4)

        # RESPOSTAS FINAIS
        respostas = VGroup(
            Text("Resposta final:", font_size=34),
            MathTex(r"a)\; 1{,}92\,m^2"),
            MathTex(r"b)\; 17{,}67\%")
        ).arrange(DOWN)

        respostas.scale(0.9)
        respostas.move_to(ORIGIN)

        self.play(
            FadeOut(
                VGroup(
                    item_b,
                    grupo_circulo,
                    grupo_amarela,
                    grupo_porcentagem,
                    bandeira,
                    dados
                )
            )
        )

        self.play(Write(respostas))
        self.wait(5)