metro = int(input('Insira o valor em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f'{metro} metros vale:\n{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm.')
