# Calcule a quantidade de tinta necessária para pintar uma parede. 1l de tinta, pinta 2m² de área.

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))

area = altura * largura

print("A sua parede mede {}x{} e a sua área é {}m².".format(largura, altura, area))

tinta = area/2
print("Serão necessários {}l de tinta para pintar essa parede.".format(tinta))
