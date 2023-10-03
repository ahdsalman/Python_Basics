                    # <---Python Basics--->

a=10
b=20

if a<b:
    print(True)
else:
    print(False)

                    # <---Python List--->

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y=my_list[::-1]
print(y)
x=my_list[2:5]
print(x)
 
                    # <---List itration--->

list1=[1,2,3,4,5,6,7]

for x in list1:
    print(x,end='')


                    #<--- Slicing with start, stop, and step--->

sliced_list = my_list[2:7:2]

print(sliced_list)  # Output: [2, 4, 6]

                    # <---Python Tuple--->

tuple1=('Apple','Orange','Mango')
print(tuple1)

c=tuple1.count('Orange')
print(c)

print(tuple1[0]) #<---Possession Accessing--->

del tuple1       #<---Deletion--->
print(tuple1)


tu=(1,2,3,4,5,6,7) #<---Count of element--->
x=tu.count(2)
print('Count',x)

T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)  
res = T1.count(2)   #<---Element of counting possession--->
print('Count of 2 in T1 is:', res)  

                            # <---Python set--->

set0={"Salman","Shammas","Shahal","Yaseen","Anshad"}
print(set0)

set0.add("Shazin") #( ___Add a new Element___)

print("After Add:",set0)


# (___Python set updation___)


set1={"Salman","Shammas","Shahal","Yaseen","Anshad","salman"}
print(set1)

set1.update(["Safvan","Shamil","Ameer"])

print("After Update:",set1)

# (___Python set remove() and discard()___ )


set1.discard("Mufees")   #( Mentioned element not from the set() objects. 
                        # But it is not rise an error, It will give the output of set() objects. )
print("Discard:",set1)
print(type(set1))

# ( ___remove()___ )
# ___________________

# set1.remove("Mufees") ( It is rise an error.Becouse Mentioned element not from set objects. 
#                        remove() method allowed for removing the elements from set objects )
# print("Remove:",set1)


                        # <---Python Dict--->

Employee = {"Name": "Salman", "Age": 23, "salary":30000,"Company":"WIPRO",(201):"Department ID"}        
for x,y in Employee.items():        
    print(x,y)  




                        # <---Python Copies--->

import copy

                        #(___shallow copy___) 

og_list = [1,2,[3,4,5]]

shallow = copy.copy(og_list)

shallow[2][0]=7

print(og_list)
print(shallow)

                        # (___Deep copy___)

n_list = [1,2,[3,4,5]]

deep = copy.deepcopy(n_list)

deep[2][0]=7

print(n_list)
print(deep)

                        # <---Use of dir()--->
                        # (___in list[]___)

liste=[1,2,3,4,5]

x=dir(list)

print(x)

                        # (___in tuple()___)

tuple=("salman","shazin","safvan")

y=dir(tuple)

print(y)

                    # <---list comprehension--->

liste1 = [2,3,4,5,6,7,8]
evn = [x for x in liste1 if x % 2 == 0]
print(evn)

                    # <---lambda dunction--->

num = [2,3,4,5]
mlt = map(lambda x: x*2 , num)
print(list(mlt))

                        # <---Generator---?

def mystd():
    lis=["Salman"]

    for x in lis:
        yield x
k=mystd()
print(next(k))


def gen():
    x="I am hero"
    yield x

print(next(gen()))

                        # <---Decerator--->

def myapp(game):
    def mine(k):
        res=game(k)
        return res.upper()
        
    return mine

@myapp
def me(j):
    return j
print(me("football"))
    

li=[2,4,6,8,10]
def cal(loop):
    def wrapp(k):
        ml=1
        for x in li:
            ml=ml*x
        return ml
    print(loop(sum))
    return wrapp

@cal
def mult(k):
    su=0
    for x in li:
        su=su+x
    return su
print(mult(sum))


li=[1,2,3,4,5]
def ku(func):
    def wrapp(k):
        ml=1
        for x in li:
            ml=ml*x
        
        return ml
    print(func(sum))
        
    return wrapp

@ku
def mt(j):
    s=0
    for x in li:
        s=s+x
    return s
print(mt(sum))

            