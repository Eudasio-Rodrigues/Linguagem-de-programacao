#Implemente uma classe figuraGeométrica que calcule o perímetro e área de figuras diferentes.

class figuraGeometrica:
    def __init__(self,lado, base, altura ):
        self.lado = lado
        self.base = base
        self.altura = altura
       
    def quadrado(self):
        perimetro = 4 *self.lado
        area = self.lado *self.lado
        print(f"Quadrado")
        print(f"Perimetro:{perimetro}\nArea:{area}\n")

    def retangulo(self):
        perimetro = 2 * (self.base + self.altura)
        area = self.base * self.altura
        print(f"Retangulo")
        print(f"Perimetro:{perimetro}\nArea:{area}\n")

    def triangulo(self):
        perimetro = 3 * self.lado
        area = (self.base * self.altura) / 2
        print(f"Triangulo")
        print(f"Perimetro:{perimetro}\nArea:{area}\n")

figurageometrica = figuraGeometrica(4, 6, 3)
figurageometrica.quadrado()
figurageometrica.retangulo()
figurageometrica.triangulo()