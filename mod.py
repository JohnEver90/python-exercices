
def run():
    monto = input("¿Cuál es el monto en nuevos soles a cambiar?: ") 
    bill_200 = int(monto)/200
    bill_100 = (int(monto)%200)/100
    bill_50 = (int(monto)%100)/50
    bill_20 = (int(monto)%50)/20
    bill_10 = (int(monto)%20)/10
    mon_5 = (int(monto)%10)/5
    mon_2 = (int(monto)%5)/2
    mon_1 = (int(monto)%2)/1
    print("Los billetes q recibiria serian de: "+ str(int(bill_200)) +" de 200; "+ str(int(bill_100))+" de 100; " + str(int(bill_50))+" de 50; "+ str(int(bill_20)) +" de 20; "+ str(int(bill_10)) +" de 10; ")
    print("Y en monedas: "+ str(int(mon_5)) +" de 5; "+ str(int(mon_2)) +" de 2; Y "+ str(int(mon_1)) +" de un sol; ")



if __name__ == "__main__":
    run()
