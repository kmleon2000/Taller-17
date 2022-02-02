# la funcion factorial(n) examina en primera instancia si el parametro el mayor a 0, esto para que cumpla con la
# primera regla de un número factorial ( el número del factorial debe ser positivo ), si es así, examina despues
# si el número es igual a 1, si es así me retorna el número, de lo contrario retorna el valor mltiplicado por la
# invocación del mismo metodo ( recursividad ) y como parametro el número decrementado en uno.

# Así, si tenemos factoral(7) se describiría como:

# factorial(7) == 7 * factorial(6)
#                     6 * factorial(5)
#                         5 * factorial(4)
#                             4 * factorial(3)
#                                 3 * factorial(2)
#                                     2 * factorial(1)
#                                         1
# Entonces tenemos: ___________________________________
#                 7 * 6 * 5 * 4 * 3 * 2 * 1 == 7!