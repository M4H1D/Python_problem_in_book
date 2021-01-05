bd_division_info={}
bd_division_info["Barishal"]={"district":6,"upazila":39,"union":333}
bd_division_info["Dhaka"]={"district":13,"upazila":93,"union":1833}
bd_division_info["Chittagong"]={"district":11,"upazila":97,"union":336}
bd_division_info["Khulna"]={"district":10,"upazila":59,"union":270}
bd_division_info["Mymensingh"]={"district":4,"upazila":34,"union":350}
bd_division_info["Rajshahi"]={"district":8,"upazila":70,"union":558}
bd_division_info["Rangpur"]={"district":8,"upazila":58,"union":536}
bd_division_info["Sylhet"]={"district":4,"upazila":38,"union":334}
x=0
for key in bd_division_info:
	x+=(bd_division_info[key]["district"])
print("Total district =",x)
y=0
for key in bd_division_info:
	y+=(bd_division_info[key]["upazila"])
print("Total Upazila =",y)
z=0
for key in bd_division_info:
	z+=(bd_division_info[key]["union"])
print("Total union =",z)