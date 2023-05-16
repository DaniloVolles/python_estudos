# Digite um programa que converta distâncias em metros em suas potências

d = float(input("Digite uma distância em metros: "))

mm = d * 1000
cm = d * 100
dm = d * 10
dam = d / 10
hm = d / 100
km = d / 1000


print("{} metros equivalem à:".format(d))
print("{:.4f}mm, {:.4f}cm e {:.4f}dm.".format(mm, cm, dm))
print("{:.4f}dam, {:.4f}hm e {:.4f}km.".format(dam, hm, km))