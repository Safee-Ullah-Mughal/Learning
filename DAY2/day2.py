import requests

#Dictionaries and Lists
people = ['Shahid','Kamran','Hamid']
person = {'Name':['Safee Ullah','Abdullah'], 'Age':28}
print(person['Name'])
print(person.keys())
print(person.values())

#List Manipulation 
#Append

a=['Apple','Banana','Cherry']
print('Before appeand',a)
a.append('Orange')
print('After Append',a)

#Remove
a.remove('Banana')
print('After removing element from List',a)
a.pop()
print(a)

#for loop in Python
list1=['Peach','Stwarberry',"Orange","Pomegranate","Cherry",'Blueberry']
item=[]
for i in range(len(list1)):
    item=list1[i]
    a.append(item)
print(a)

