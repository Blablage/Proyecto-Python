import usuario as usr
import tarjeta as tjt

#tarjeta1 = tjt.tarjeta()
#tarjeta2 = tjt.tarjeta()

usuario1 = usr.usuario('Gerardo')

usuario1.agregar_tarjeta('credito')
usuario1.multiples_reportes()

usuario1.agregar_tarjeta('credito')
usuario1.multiples_reportes()

usuario1.eliminar_tarjeta_x_nombre("Uno")
usuario1.eliminar_tarjeta_x_nombre("Tres")

usuario1.multiples_reportes()

queryTarjeta = usuario1.get_index_lista_tarjetas("Dos")
usuario1.lista_tarjetas[queryTarjeta].abonar_tarjeta()
usuario1.lista_tarjetas[queryTarjeta].captura_nuevo_cargo()
#print(usuario1.lista_tarjetas[0].nombre_tarjeta)

usuario1.multiples_reportes()

usuario1.agregar_tarjeta('servicio')
queryTarjeta = usuario1.get_index_lista_tarjetas("Cuatro")
usuario1.lista_tarjetas[queryTarjeta].abonar_tarjeta()
usuario1.lista_tarjetas[queryTarjeta].pago_recurrente()

usuario1.multiples_reportes()
