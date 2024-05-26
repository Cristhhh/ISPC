Algoritmo TiendaISPC
	
		
		// Declaración de variables en Array
		Dimension productos[10] 
		Dimension precios[10] 
		Dimension carrito[10] <- 0 // Inicialización del carrito
		Definir opcion, cantidad_productos, indice Como Entero
		Definir total Como Real
		cantidad_productos = 0
		
		// Menú principal
		Mientras Verdadero Hacer
			Escribir "Menú:"
			Escribir "1. Registrar producto"
			Escribir "2. Mostrar productos"
			Escribir "3. Agregar producto al carrito"
			Escribir "4. Realizar compra"
			Escribir "5. Salir"
			Escribir "Seleccione una opción: "
			Leer opcion
			
			Segun opcion Hacer
				Caso 1:
					// Registrar producto
					Si cantidad_productos < 10 Entonces
						Escribir "Ingrese el nombre del producto: "
						Leer productos[cantidad_productos]
						Escribir "Ingrese el precio del producto: "
						Leer precios[cantidad_productos]
						cantidad_productos = cantidad_productos + 1
					SiNo
						Escribir "No se pueden registrar más productos."
					FinSi
				Caso 2:
					// Mostrar productos
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						Escribir i + 1, ". ", productos[i], " - $", precios[i]
					FinPara
				Caso 3:
					// Agregar producto al carrito
					Escribir "Seleccione el número del producto que desea agregar al carrito: "
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						Escribir i + 1, ". ", productos[i], " - $", precios[i]
					FinPara
					Leer indice
					Si indice > 0 Y indice <= cantidad_productos Entonces
						carrito[indice] = carrito[indice] + 1 // Corregir el índice
						Escribir "Producto agregado al carrito."
					SiNo
						Escribir "Número de producto no válido."
					FinSi
				Caso 4:
					// Realizar compra
					total = 0
					Escribir "Resumen de la compra:"
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						Si carrito[i] > 0 Entonces
							Escribir productos[i], " x ", carrito[i], " - $", precios[i] * carrito[i]
							total = total + precios[i] * carrito[i]
						FinSi
					FinPara
					Escribir "Total a pagar: $", total
					Escribir "Compra realizada con éxito. Gracias por su compra!"
					
					// Resetear carrito después de la compra
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						carrito[i] = 0
					FinPara
				Caso 5:
					// Salir
					Escribir "Gracias por usar el sistema."
				De Otro Modo:
					Escribir "Opción no válida."
			FinSegun
		FinMientras

FinAlgoritmo

	

