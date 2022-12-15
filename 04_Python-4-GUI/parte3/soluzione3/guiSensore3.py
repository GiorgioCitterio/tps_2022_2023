import serial
import struct
import matplotlib.pyplot as plt
IDCORRETTO = "BE"
DESTINATARIOCORRETTO = "D031"

arduino = serial.Serial('COM3', 9600)
y = []
#y1 = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
x = []

for i in range(20):
    val = arduino.read(32)
    pack = struct.unpack("2s 4s 4s 2s 4s 16s", val)
    print(pack)
    id=pack[0].decode()
    mittente=pack[1].decode()
    destinatario=pack[2].decode()
    tipo=pack[3].decode()
    valoreSensore=pack[4].decode()
    vuoto=pack[5].decode()
    if (id==IDCORRETTO)and(destinatario==DESTINATARIOCORRETTO):
        print("id e destinatario corretti, valore del sensore = "+valoreSensore)
        y.append(int(valoreSensore))
        x.append(i)
    else:
        print("pacchetto scartato")

plt.plot(x, y, marker="o",color = 'red')
plt.title("Il grafico dei valori del sensore")
plt.xlabel("X - Secondi")
plt.ylabel("Y - Valori sensore")
plt.axes([0, 15, 0, 1023])
plt.show()