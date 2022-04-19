print("Ingrese su nombre de tarjeta")
nombre_tarjeta = input()

print("Ingrese la tasa de interes")
tasa_interes = input()

print("Ingrese la deuda actual")
deuda = input()

print("Ingrese el pago a realizar")
pago= input()
while pago > deuda:
    print("Monto no valido. Ingrese de nuevo")
    pago= input()


print("Ingrese el monto del nuevo cargo")
cargo= input()


interes_mensual = int(tasa_interes)/12
deuda_recalculada = (int(deuda) - int(pago))*( 1 + int(interes_mensual)) 
nueva_deuda = deuda_recalculada + int(cargo)

print("Hola " + str(nombre_tarjeta))
print("interes_mensual " + str(interes_mensual))
print("deuda_recalculada " + str(deuda_recalculada))
print("nueva_deuda " + (nueva_deuda))
print("Gracias por su pago. La deuda del proximo mes es de: " + str(nueva_deuda))