#Sistema vacacional RVPI
print("=============================")
print("Sistema vacasional de 'RVPI' ")
print("============================= \n")

inf_trabajador = input("Coloca tu nombre completo: ")
inf_2 = input("Introduce la clave de area: ")
inf_3 = float(input("Introduce el tiempo que llevas con nosotros: "))

#Area de Atencion al cliente.

if inf_2 == "P12345":
    print("\nArea de trabajo 'Atencion al cliente' ")


    if inf_3 == 1 and inf_3 < 2:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 6 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 2 and inf_3 <= 6:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 14 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 7:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 20 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    else:
        print("Los sentimos " + inf_trabajador + " Aun no cumples con los resquisitos de la empresa")
        print("No tienes derecho a vacaciones.")



#Area de la logistica.

elif inf_2 == "R12345":
    print("\nArea de trabajo 'Logistica' ")


    if inf_3 == 1 and inf_3 < 2:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 7 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 2 and inf_3 <= 6:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 15 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 7:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 22 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    else:
        print("Los sentimos " + inf_trabajador + " Aun no cumples con los resquisitos de la empresa")
        print("No tienes derecho a vacaciones.")



#Area de la gerencia.

elif inf_2 == "V12345":
    print("\nArea de trabajo 'Gerencia' ")


    if inf_3 == 1 and inf_3 < 2:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 10 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 2 and inf_3 <= 6:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 20 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    elif inf_3 >= 7:
        print("Hola" " " + inf_trabajador + " " "Gracias por pertenecer a nuestra familia." )
        print("Correspondes a 30 dias de vacaciones.")
        print("Que disfrutes tus vacaciones.")

    else:
        print("Los sentimos " + inf_trabajador + " Aun no cumples con los resquisitos de la empresa")
        print("No tienes derecho a vacaciones.")

else:
    print("Area no registrada. ")

 