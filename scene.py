from manim import *
import numpy as np

class SystolicArray(Scene):
	def construct(self):
		fontsize = 100
		square1 = Square()
		square2 = Square()
		square3 = Square()
		square4 = Square()

		end = Text("Code in the description", slant=ITALIC)
		end.move_to(UP*10)
		A = VGroup(Text('A', font_size=fontsize, font="sans", color = PURPLE_A))
		B = VGroup(Text('B', font_size=fontsize, font="sans", color = PURPLE_A))
		C = VGroup(Text('C', font_size=fontsize, font="sans", color = PURPLE_A))
		D = VGroup(Text('D', font_size=fontsize, font="sans", color = PURPLE_A))

		E = VGroup(Text('E', font_size=fontsize, font="sans", color = BLUE_C))
		F = VGroup(Text('F', font_size=fontsize, font="sans", color = BLUE_C))
		G = VGroup(Text('G', font_size=fontsize, font="sans", color = BLUE_C))
		H = VGroup(Text('H', font_size=fontsize, font="sans", color = BLUE_C))

		square1.move_to(LEFT+UP*2)
		square2.next_to(square1, RIGHT)
		square3.next_to(square1, DOWN)
		square4.next_to(square3, RIGHT)

		B.next_to(square1, LEFT, buff=0.9)
		A.next_to(B, LEFT, buff = 0.9)
		D.next_to(A, DOWN, buff = 0.9)
		C.next_to(D, LEFT, buff = 0.9)
		matrix1 = VGroup(A, B, C, D)
		

		G.next_to(square1, UP, buff = 0.9)
		E.next_to(G, UP, buff = 0.9)
		H.next_to(E, RIGHT, buff = 0.9)
		F.next_to(H, UP, buff = 0.9)
		matrix2 = VGroup(E, F, G, H)

		BG = VGroup(Text('BG', font_size=50, font="sans", color = TEAL_C))
		BG.next_to(square3, UP*5)

		AE = VGroup(Text('+AE', font_size=50, font="sans", color=TEAL_C))
		AE.next_to(BG, DOWN)

		BH = VGroup(Text('BH', font_size=50, font='sans', color=TEAL_C))
		BH.next_to(square4, UP*5)

		DG = VGroup(Text('DG', font_size=50, font='sans', color=TEAL_C))
		DG.next_to(square1, DOWN*2)

		AF = VGroup(Text('+AF', font_size=50, font='sans', color=TEAL_C))
		AF.next_to(BH, DOWN)
		CE = VGroup(Text('+CE', font_size=50, font='sans', color=TEAL_C))
		CE.next_to(DG, DOWN)

		DH = VGroup(Text('DH', font_size=50, font='sans', color=TEAL_C))
		DH.next_to(square2, DOWN*2)

		CF = VGroup(Text('+CF', font_size=50, font='sans', color=TEAL_C))
		CF.next_to(DH, DOWN)

		
		self.play(Create(square1), Create(square2), Create(square3), Create(square4))
		self.play(Write(matrix1[0]), Write(matrix1[1]), Write(matrix1[2]), Write(matrix1[3]), Write(matrix2[0]), Write(matrix2[1]), Write(matrix2[2]), Write(matrix2[3]))
		
		matrix1.remove(B)
		matrix2.remove(G)

		self.play(Transform(VGroup(B, G), BG), matrix1.animate.shift(RIGHT), matrix2.animate.shift(DOWN))

		matrix1.remove(A)
		matrix1.remove(D)
		matrix2.remove(E)
		matrix2.remove(H)

		self.play(Transform(VGroup(A, E), AE), Transform(VGroup(BG[0][0], H), BH), Transform(VGroup(BG[0][1], D), DG),  matrix1.animate.shift(RIGHT), matrix2.animate.shift(DOWN))

		matrix1.remove(C)
		matrix2.remove(F)
		
		
		_B = VGroup(Text('B', font_size=fontsize, font="sans", color = PURPLE_A))
		_B.next_to(square2, RIGHT, buff=0.9)
		_G = VGroup(Text('G', font_size=fontsize, font="sans", color = BLUE_C))
		_G.next_to(square3, DOWN, buff = 0.9)
		_matrix1 = VGroup(_B)
		_matrix2 = VGroup(_G)
		
		self.play(Transform(VGroup(AE[0][1], F), AF), Transform(VGroup(AE[0][2], C), CE), Transform(VGroup(DG[0][0], BH[0][1]), DH), ReplacementTransform(BH[0][0], _B), ReplacementTransform(DG[0][1], _G))
		
		_A = VGroup(Text('A', font_size=fontsize, font="sans", color = PURPLE_A))
		_D = VGroup(Text('D', font_size=fontsize, font="sans", color = PURPLE_A))
		_E = VGroup(Text('E', font_size=fontsize, font="sans", color = BLUE_C))
		_H = VGroup(Text('H', font_size=fontsize, font="sans", color = BLUE_C))
		_A.next_to(square2, RIGHT, buff = 0.9)
		_D.next_to(square4, RIGHT, buff = 0.9)
		_E.next_to(square3, DOWN, buff = 0.9)
		_H.next_to(square4, DOWN, buff = 0.9)
		

		self.play(Transform(VGroup(CE[0][1], AF[0][1]), CF), ReplacementTransform(AF[0][1], _A), ReplacementTransform(DH[0][0], _D), ReplacementTransform(DH[0][1], _H), ReplacementTransform(CE[0][2], _E), _matrix1.animate.shift(RIGHT*1.5), _matrix2.animate.shift(DOWN*1.5))
		_matrix1.add(_A, _D)
		_matrix2.add(_E, _H)
		_C = VGroup(Text('C', font_size=fontsize, font="sans", color = PURPLE_A))
		_F = VGroup(Text('F', font_size=fontsize, font="sans", color = BLUE_C))
		_C.next_to(square4, RIGHT, buff = 0.9)
		_F.next_to(square4, DOWN, buff = 0.9)
		self.play(ReplacementTransform(CF[0][0], _C), ReplacementTransform(CF[0][1], _F), _matrix1.animate.shift(RIGHT*1.5), _matrix2.animate.shift(DOWN*1.5))
		self.play(FadeIn(end))
		self.wait()