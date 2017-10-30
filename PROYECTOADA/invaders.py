from sys import stdin	

def solve(matrix, s, arr):
	ans = None;
	temp = arr;
	temp.sort();
	numShot = 1;

	for i in range(s):
		shot = int(stdin.readline().strip());
		col = abs(shot) - 1;							# Obtenemos la columna
		numShot += 1;

		if(arr[i] - 1 == 0):							# Si algun camino vertical esta despejado, es decir, en arr[i] = 0 (que no se encuentra ningún escudo en la columna i)

			if(shot < 0):
				ans = '-' + str(numShot);				# Tercer caso
			else:
				ans = str(numShot);						# Cuarto caso

		if(arr[col] - 1 > 0):							# -| 
			arr[col] -= 1;								#  |
														#  |- Verificamos si el disparo actual despeja un camino vertical
		elif(arr[col] - 1 == 0):						#  |
			arr[col] = 0;								# -|

	if(temp[0] == 0):
		ans = '0';										# Primer caso					

	if(ans == None):
		ans = 'X';										# Segundo caso

	return ans;

def recibirEntrada():
	temp = stdin.readline().strip().split();

	if(len(temp) == 0):									# Verifica si todavia hay un ingreso de datos
		matrix = -1;
		s = -1;
		arr = None;

	else:
		r = int(temp[0]);								# Obtenemos el número de filas, columnas y disparos
		c = int(temp[1]);
		s = int(temp[2]);

		arr = [0 for i in range(c)];					# Inicializamos un arreglo en 0, este indica cuantos escudos hay por columna

		matrix = [];

		for i in range(r):
			matrix.append(stdin.readline().strip());

			for j in range(len(matrix[i])):
				if(matrix[i][j] == '#'):				# Cada vez que hay un escudo se aumenta el contador por columna que se encuentra en el arreglo
					arr[j] += 1;

	return matrix, s, arr;

def main():
	matrix = arr = None;

	while(matrix != -1):								# La matriz = -1 si ya acabo el ingreso de datos
		matrix, s, arr = recibirEntrada();

		if(matrix != -1):
			print(solve(matrix, s, arr));

main();