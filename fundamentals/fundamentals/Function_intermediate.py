

x = [ [5,2,3], [10,8,9] ]
print(x)
x[1][0] = 15
print(x)



students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]    

students[0]['last_name'] = 'Bryant'
print(students)

# ---------------------------------------third part--------------------------------------------------------
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}


sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

#--------------------------------------------fourth part---------------------

z = [ {'x': 10, 'y': 20} ] 
# # Change the value 20 in z to 30
z[0]['y'] = 30
print(z)


def iterateDictionary(students):
    for i in range(len(students)):
        print(f"first_name-{students[i]['first_name']}, last_name-{students[i]['last_name']}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)



def iterateDictionary2(key_name, some_list):
    for i in range(len(students)):
        print(f"{students[i]['first_name']}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2(['first_name'], students)

def iterateDictionary2(key_name, some_list):
    for i in range(len(students)):
        print(f"{students[i]['last_name']}")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2(['last_name'], students)



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for i in (dojo):
        print(i)
        for j in (dojo[i]):
            print(j)

printInfo(dojo)


