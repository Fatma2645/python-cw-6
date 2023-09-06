# write your code here
person={
"name":"fatma",
"age":15,
"hobbies":["horse rider","painter"]
}



print(person.get ("name"))


print(person.get('age'))


person["age"]=18
person["country"]="Spain" 
print(person)
print("length of dictionary:",len(person))




person["hobbies"].append("wriring")




def check_hobbies(person):
    if len (person['hobbies'])>3:
        print("wow you are amazing")
check_hobbies(person)     