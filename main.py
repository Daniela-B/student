from student import student


def crea_estudiantes(count_estudiantes):
	count = 0
	list_students = []
	
	while count < int(count_estudiantes):

		student_code = input("dame la matricula: ")
		student_name = input("dame el nombre: ")
		student_age = input("dame la edad: ")
		student_gender = input("dame el genero: ")
		student_carreer = input("dame la carrera: ")
		
		list_students.append(student(student_code,student_name,student_age,student_gender,student_carreer))
		
		count = count + 1
	return list_students


def ordena_edades(students):
    for stds in students:
        orden=sorted(students, key=lambda student: student.age)  
        return orden;

def separa_generos(student):
    if student[3]=="femenino":
        return 1
    else:
        return 2

def main():
	
   options = 1
   list_student = []
   list_hombres=[]
   list_mujeres=[]
   list_orden=[]

while options != "0":
		options = input("menu opciones 1. crea estudiantes - 2.ordena edades - 3.separa generos - 0. salir: ")

		if options == "1":
			print("crea estudiantes")
			count_x = input("cuantos estudiantes daremos de alta: ")
			list_student = crea_estudiantes(count_x)

		if options == "2":
		 print("ordena edades")
         list_orden=ordena_edades(list_stud)
         print(list_order)
            
            

		if options == "3":
			print("separa generos")
            for stds in list_student:
                gender=separa_generos(std)
                if gender = 1:
                    list_hombres.append(stds)
                else:
                    list_mujeres.append(stds)
            print("los hombres son: )
            print(list_hombres)
            print("las muejeres son: )
            print(list_mujeres)

if __name__ == "__main__":
	main()