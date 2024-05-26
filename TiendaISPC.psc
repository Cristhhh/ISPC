Algoritmo TiendaISPC
	
		
		// Declaraci�n de variables en Array
		Dimension productos[10] 
		Dimension precios[10] 
		Dimension carrito[10] <- 0 // Inicializaci�n del carrito
		Definir opcion, cantidad_productos, indice Como Entero
		Definir total Como Real
		cantidad_productos = 0
		
		// Men� principal
		Mientras Verdadero Hacer
			Escribir "Men�:"
			Escribir "1. Registrar producto"
			Escribir "2. Mostrar productos"
			Escribir "3. Agregar producto al carrito"
			Escribir "4. Realizar compra"
			Escribir "5. Salir"
			Escribir "Seleccione una opci�n: "
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
						Escribir "No se pueden registrar m�s productos."
					FinSi
				Caso 2:
					// Mostrar productos
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						Escribir i + 1, ". ", productos[i], " - $", precios[i]
					FinPara
				Caso 3:
					// Agregar producto al carrito
					Escribir "Seleccione el n�mero del producto que desea agregar al carrito: "
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						Escribir i + 1, ". ", productos[i], " - $", precios[i]
					FinPara
					Leer indice
					Si indice > 0 Y indice <= cantidad_productos Entonces
						carrito[indice] = carrito[indice] + 1 // Corregir el �ndice
						Escribir "Producto agregado al carrito."
					SiNo
						Escribir "N�mero de producto no v�lido."
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
					Escribir "Compra realizada con �xito. Gracias por su compra!"
					
					// Resetear carrito despu�s de la compra
					Para i = 0 Hasta cantidad_productos - 1 Con Paso 1 Hacer
						carrito[i] = 0
					FinPara
				Caso 5:
					// Salir
					Escribir "Gracias por usar el sistema."
				De Otro Modo:
					Escribir "Opci�n no v�lida."
			FinSegun
		FinMientras

FinAlgoritmo

	

