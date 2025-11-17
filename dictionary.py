my_dict={
    "name":"Shweta",
    "age":23,
    "City":"Pune",
    "occupation":"MCA",
    "Status":"Active"
}
print("Original Dictionary :",my_dict)
print("\n Keys of my dictionary :")
for key in my_dict.keys():
    print(key)

my_dict["email"]="shweta222@gmail.com"
print("\n Dictionary after adding new key-value pair ('email'):",my_dict)

del my_dict["Status"]
print("\n Dictionary after deleting the element with the key'status':",my_dict)

my_dict["age"]=22
print("\n Dictionary after the modifying :",my_dict)