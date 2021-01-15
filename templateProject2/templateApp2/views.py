from django.shortcuts import render

# Create your views here.
def EmployeeView(request):
	Ename = input("Enter the name: ")
	Edesignation  = input("Enter the designation: ")
	Esal = int(input("Enter the salary: "))
	Eexp = float(input("Enter the experience: "))
	d = {'name':Ename,'desig':Edesignation,'sal':Esal,'exp':Eexp}
	return render(request,'templateApp2/1.html',d)