betettosz=float(input("Adja meg a betett pénzősszeget:"))
kamat=float(input("Adja meg a kamatot (%,-ban):"))
kamatv=kamat/100
ev=int(input("Adja meg hány évre akarja leköttetni: "))

kamatoskamat=betettosz*(1+kamatv)**ev



print("Képződött kamat:",round(kamatoskamat,2),"Ft")

