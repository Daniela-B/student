from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	list_ages = []
	
	while count < int(count_estudiantes):

		student_code = input("Dame la matricula: ")
		student_name = input("Dame el nombre: ")
		student_age = input("Dame la edad: ")
		student_gender = input("Dame el genero: ")
		student_carreer = input("Dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		list_ages.append(student_age)

		count = count + 1
	return list_students


def ordena_edades(list_ages):
	for recorrer in range(1,len(list_ages)):
	 for posicion in range (len(list_ages) - recorrer):
	  if list_ages [posicion] > list_ages[posicion + 1]:
	   temp = list_ages[posicion]
	   list_ages[posicion] = list_ages[posicion + 1]
	   list_ages[posicion+1] = temp
	print list_ages[:]

def separa_generos(list_students):
	print ("metodo vacio")

def main():
	
	options = 1
	list_stud = []

	while options != "0":
		options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")

		if options == "1":
			print("crea estudiantes")
			count_x = input("cuantos estudiantes daremos de alta: ")
			list_stud = crea_estudiantes(count_x)

		if options == "2":
			ordena_edades(list_ages)

		if options == "3":
			print("separa generos")

if __name__ == "__main__":
	main()
