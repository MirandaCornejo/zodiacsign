# Ejercicio 2- signo zodiacal
dia= int(input("Ingresa el dia de tu nacimiento:"));
mes= int(input("Ingresa el numero de mes de tu nacimiento:"));
if (dia<=21 or dia>=19) and (mes==3 or mes==4):
    print("Aries");
elif (dia<=20 or dia>=20) and (mes==4 or mes==5):
    print("Tauro");
elif (dia<=21 or dia>=20) and (mes==5 or mes==6):
    print("Geminis");
elif (dia<=21 or dia>=22) and (mes==6 or mes==7):
    print("Cancer");
elif (dia<=23 or dia>=22) and (mes==7 or mes==8):
    print("Leo");
elif (dia<=23 or dia>=22) and (mes==8 or mes==9):
    print("Virgo");
elif (dia<=23 or dia>=22) and (mes==9 or mes==10):
    print("Libra");
elif (dia<=23 or dia>=21) and (mes==10 or mes==11):
    print("Escorpio");
elif (dia<=22 or dia>=21) and (mes==11 or mes==12):
    print("Sagitario");
elif (dia<=22 or dia>=21) and (mes==12 or mes==1):
    print("Capricornio");
elif(dia<=20 or dia>=18) and (mes==1 or mes==2):
    print("Acuario");
elif(dia<=19 or dia>=20) and (mes==2 or mes==3):
    print("Piscis");

    
    