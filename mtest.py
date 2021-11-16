import json

with open("m.json") as jsondata:
    data = json.load(jsondata)
    fil = data["filiali"]

filiale = input("Numero della filiale: \n")
if filiale not in fil:
    raise ValueError("Nessuna filiale trovata")
print(fil[filiale]["title"])
    
numerocassa = input("Numero della cassa: \n")
for val in fil[filiale]["cassa"]:
    if numerocassa not in fil[filiale]["cassa"]:
            raise ValueError("Nessuna cassa trovata")
print(fil[filiale]["cassa"][numerocassa])
print("Nome di rete: ", fil[filiale]["cassa"][numerocassa][0])

print("ciao")


# if 'data' not in data['to']:
#     raise ValueError("No data for target")
# for dest in data['to']['data']:
#     if 'id' not in dest:
#         continue
#     targetId = dest['id']
#     print("to_id:", targetId)