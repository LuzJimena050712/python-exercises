import numpy as np

# Función para ingresar los vectores
def ingresar_vector():
    entrada = input("Ingrese los elementos del vector separados por comas: ")
    vector = np.array([(x) for x in entrada.split(',')])
    return vector

# Ingresar los vectores del espacio S
print("Ingrese los vectores del espacio S:")
S = np.array([ingresar_vector(), ingresar_vector()])

# Ingresar los vectores a comprobar
print("\nIngrese los vectores a comprobar:")
vectores = [ingresar_vector() for _ in range(4)]

# Comprobar si los vectores pueden expresarse como una combinación lineal de los vectores en S
for vector in vectores:
    if np.linalg.matrix_rank(np.vstack((S, vector))) == np.linalg.matrix_rank(S):
        print(f"El vector {vector} puede ser expresado como una combinación lineal de los vectores en S.")
    else:
        print(f"El vector {vector} NO puede ser expresado como una combinación lineal de los vectores en S.")