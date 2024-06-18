#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=10


# In[2]:


a+a


# In[3]:


a+2*a


# In[4]:


'hello i am ankit'


# In[5]:


"I'm ankit dubey"


# In[12]:


print('hello world')


# In[13]:


print("hello this is /n ankit")


# In[14]:


mystring='hello world'


# In[15]:


mystring[-2]


# In[16]:


mystring= "hello world"


# In[17]:


mystring


# In[18]:


mystring[-2]


# In[19]:


mystring[2:]


# In[20]:


mystring[2:5]


# In[23]:


mystring[2:9]


# In[1]:


x='hello world'


# In[2]:


#.DOT FORMAT METHOD !!!




# 17th  january 2024


# In[4]:


print("I'm {} {} " .format('Ankit','Dubey'))



# In[21]:


print('The {p} {h}'.format(p='Great',h='Khali'))



# In[13]:


#float formatting method with dot format method.
result=100/666


# In[14]:


result


# In[20]:


print("this result was {r}".format(r=result)
)


# In[22]:


print("The result was {r:1.2f}" .format(r=result))


# In[23]:


#actual float format method (new method).


# In[24]:


name='jose'


# In[29]:


print(f'hello,his name is {name}')


# In[27]:


name='Jose'
age='18'


# In[30]:


print(f'{name} is {age} years old')


# In[31]:


#LIST IN PYTHON!!!





# In[34]:


mylist =['one','two','three']


# In[35]:


mylist[0]


# In[36]:


anotherlist=['four','five']


# In[56]:


newlist = mylist + anotherlist


# In[52]:


mylist[2:]


# In[54]:


mylist[1:3]


# In[57]:


newlist


# In[60]:


newlist[0] = 'ONE ALL CAPS'


# In[ ]:





# In[62]:


newlist


# In[63]:


newlist.append('six')


# In[64]:


new_list


# In[15]:


new_list=['one','two','three']


# In[16]:


new_list


# In[17]:


new_list.append('four')


# In[18]:


new_list


# In[19]:


new_list.pop()


# In[20]:


new_list


# In[22]:


popped_item=new_list.pop()


# In[23]:


new_list


# In[1]:


#24 jan /2024
#DICTIONARIES IN PYTHON !!!!





# In[4]:


d={'k1': 123,'k2': 345,'k3':{'isomerism': 100}}


# In[7]:


d['k2']


# In[8]:


d['k3']['isomerism']


# In[9]:


d={'k1':['1','2','3']} 


# In[12]:


d


# In[15]:


d['k1'].pop()


# In[16]:


d


# In[17]:


#Tuples in python !!!


# In[1]:


#sets in python !!


# In[2]:


myset=set()


# In[3]:


myset


# In[4]:


myset.add(1)


# In[5]:


myset


# In[6]:


myset.add(2)


# In[7]:


myset


# In[8]:


myset.add(2)


# In[9]:


myset # it takes unique values/ new values 
#note this !!


# In[10]:


#booleans in python
# true or false 


# In[11]:


1>2


# In[12]:


1==1


# In[13]:


#I/O WITH BASIC FILES IN PYTHON!!!





# In[14]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'Hello this is text file\nthis is the  second line\nthis is the third line\n')


# In[16]:


myfile= open('myfile.txt')


# In[ ]:





# In[19]:


pwd


# In[20]:


myfile=open('myfile.txt')


# In[21]:


myfile.read()


# In[25]:


myfile.read() # cursor ends so in order to read again we need to do .seek(0)


# In[26]:


myfile.seek(0)


# In[28]:


myfile.read()


# In[30]:


myfile.seek(0)


# In[31]:


myfile.readlines()


# In[32]:


#files location 


# In[33]:


pwd


# In[35]:


myfile.close() # agr close nhi krenge tho incase muje kyi aur woh file ko kholna tho woh bolenge this file is still running in python 
# in order to not face this we use .close()
# instead better way is niche joh likha hai cuz ye .close se pura band hojata hai so if nxt time u want this file thn u hv to
#create it.


# In[37]:


with open('myfile.txt') as my_new_list:
    contents= my_new_list.read()  
    # after doing this step u no longer need to close the files .....


# In[38]:


contents


# In[41]:


with open('myfile.txt', mode='r') as f:
         contents= f.read()


# In[42]:


contents


# In[43]:


get_ipython().run_cell_magic('writefile', 'myfile.txt', 'ONE is two\ntwo is one \nthree is four\n')


# In[44]:


with open('myfile.txt', mode='r') as f:
    print(f.read())


# In[48]:


with open('jsbdjbdjsbd.txt', mode='w') as f:
    f.write('four is three')


# In[50]:


with open('jsbdjbdjsbd.txt', mode='r') as f:
    print(f.read())


# In[1]:


#PYTHON COMPARISON OPERATORS!!!





# In[2]:


2==2


# In[3]:


2!=3 #( where != defines inequality sign)


# In[5]:


#strings works in booleans for example
'hello'=='bye'


# In[6]:


'hey'!= 'bye'


# In[9]:


#CHAINING COMPARISON OPERATOR WITH LOGICAL OPERATORS!!
# 9TH FEB 2024!!




#example below
200 != 2 and 'h'=='h'


# In[10]:


200>3


# In[11]:


not 200>3


# In[12]:


200==200 or 100<2 #


# In[1]:


# IF ELIF ELSE STATEMENT IN PYTHON!!!





# In[2]:


if True:
    print('this is true!')


# In[4]:


hungry= True
if hungry:
    print('Feed me!')
# if i write false instead of True then no output will generate !!


# In[9]:


#nice example
name= 'Sammy'

if name== 'Frankie':
    print('Hello Frankie')
elif name== 'Sammy':
    print('Hello Sammy')
else:
    print("What's your name??")


# In[1]:


# FOR LOOPS IN PYTHON!!
# four examples!!
#10thfeb/24




# In[2]:


mylist= [1,2,3,4,5,6]


# In[26]:


for num in mylist :
    print(num)


# In[6]:


mylist=[1,2,3,4]

for num in mylist:
    #check for even
    if num % 2 == 0:
        print(num)
    else: 
        print("result not found") #float format method!!


# In[9]:


mystring= 'Hello world!'

for letter in mystring:
    print(letter)


# In[10]:


len(mystring)#len counts spacebar a counting!


# In[23]:


d= {'k1':1,'k2':2,'k3':3}

for values in d.values():
    print(values)


# In[13]:


mylist=[(1,2),(3,4),(5,6)]

for a,b in mylist:
    print(b)


# In[24]:


# WHILE LOOPS IN PYTHON!!!





# In[1]:


x=0

while x<5:
    print(f'The current value of x is {x}')
    x+=1


# In[2]:


x=40

while x<5:
    print(f'The current value of x is {x}')
    x+=1
else:
    print('X IS NOT LESS THAN 5')


# In[3]:


#pass keyword 
x=[1,2,3]

for item in x:
    #do something 
    pass
print("ankit is badass")


# In[6]:


#continue keyword
mystring='sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)


# In[7]:


#break keyword
mystring='sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)


# In[2]:


#USEFUL OPERATORS IN PYTHONN!!!!






# In[7]:


for num in range(0,10,3):
    print(num)


# In[6]:


list(range(0,10,3))


# In[11]:


index_count=0

for letter in 'abcde':
    print('At indea {} the letter is {}'.format(index_count,letter))
    index_count+=1


# In[2]:


#ENUMERATE!!


word='abcde'
for letter in enumerate(word):
    print(letter)


# In[16]:


#ZIP FUNCTIONS!!

#for unven: it selects the shortest list & ignores rest!
mylist1=[1,2,3]
mylist2=['a','b','c']
mylist3=[100,200]


for item in zip(mylist1,mylist2,mylist3):
     print (item)


# In[2]:


# built-in random libraries!!


from random import shuffle


# In[3]:


mylist=[1,2,3,4,5]
shuffle(mylist)


# In[4]:


mylist


# In[5]:


from random import randint     #randint= random integer in the particular range !!


# In[6]:


randint(0,10)


# In[19]:


#input function!!
input('whats your name ?')


# In[9]:


#LIST COMPREHENSION IN PYTHON!!!!
#general :- variable 1
#variable 2 = [ element for element in variable 1 ]






# In[7]:


celcius =[25,26]

fahrenheit= [((9/5)*temp +32) for temp in celcius]


# In[8]:


fahrenheit


# In[10]:


mylist=[x**2 for x in range(0,10)]


# In[11]:


mylist


# In[12]:


results=[x if x%2==0 else 'ODD' for x in range(0,11)]


# In[13]:


results


# In[22]:


#nested loop
mylist= []
for x in [2,5,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
        


# In[23]:


mylist


# In[1]:


#1st April 2024
#Methods & Functions !!!







# In[14]:


def print_result(num1,num2):
    print(num1+num2)


# In[15]:


def return_result(num1,num2):
    return num1+num2


# In[16]:


print_result(10,20)


# In[18]:


result=return_result(10,20)


# In[19]:


#basically In return u can use the output as variable whereas in print u cant 
result


# In[20]:


#functions with logic






# In[30]:


#return all even numbers in list
def check_even_list(num_list):
    #placeholder variables
    even_numbers = []
    
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        
        else:
            pass
        
    return even_numbers    
    
        


# In[31]:


check_even_list([1,2,3,4])


# In[32]:


check_even_list([1,3,5])


# In[33]:


#TUPLES UNPACKING WITH PYTHON!!





# In[40]:


#check employee work hours in a month
work_hours=[('ankit',100),('danish',200),('aaryan',4000)]
def employee_check(work_hours):
    
    # two placeholder variables as we are  doing tuples 
    current_max = 0
    employee_of_month = ''
    
    for employee,hours in work_hours:
        if hours>current_max:
            current_max = hours
            employee_of_month = employee
        
        else:
            pass
        
    return (employee_of_month,current_max)


# In[41]:


result=employee_check(work_hours)                             


# In[42]:


result


# In[43]:


#INTERACTIONS BTW PYTHON FUCNTIONS




#SIMPLE GAME OF GUESSING


# In[48]:


mylist=['','0','']  


# In[49]:


from random import shuffle

def shuffle_check(mylist):
    shuffle(mylist)
    return mylist
    


# In[50]:


shuffle_check(mylist)


# In[25]:


def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess= input("Pick a number 0,1 or 2:-")
    
    return int(guess)


# In[26]:


player_guess()


# In[60]:


def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
        
    else:
            print("Wrong Guess!")
            print(mylist)


# In[65]:


#intial list
mylist = ['','0','']
#shuffle list
result = shuffle_check(mylist)
#player guess
guess = player_guess()
#guess  is right or wrong 
check_guess(mylist,guess)


# In[1]:


#*args & *kwargs in python !!!






# In[27]:


def myfunc(a,b,c=0,d=0,e=0):
    # return 5% of sum of arguments!!
    return sum((a,b,c,d,e))*0.05


# In[28]:


myfunc(40,60,100,2,3,4)


# In[29]:


# to avoid positonal arg above we use *args 
def myfunc(*args):# using *args gives us unlimited argument to use!!
    return sum(args)*0.05


#IMPORTANT


# In[30]:


myfunc(40,100.200)


# In[28]:


#keyword arguments **


def myfunc(**kwargs):
    print(kwargs)
    if 'fruit'in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
            print(' I did not get any fruit here!')


# In[30]:


myfunc(fruit='apple',veggie='tomato')


# In[44]:


def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like to have {} {}'.format(args[0],kwargs['food']))
    
    
    #IMPORTANT!!!


# In[45]:


myfunc(10,food='apple')


# In[1]:


#lambda expressions,Map and Filter functions







# In[36]:


#map functions 


mynums= [1,2,3,4,5]
def square(num):
    return num**2
    


# In[37]:


list(map(square,mynums))


# In[8]:


def splicer(mystring):
    if len(mystring)%2==0:
        return 'Even'
    else:
        return mystring[0]


# In[9]:


mystring=['Addy','Eve','Ankit']


# In[10]:


list(map(splicer,mystring))


# In[11]:


#filter functions

def check_even(num):
    return num%2==0


# In[12]:


my_nums=[1,2,3,4,5,6]


# In[13]:


list(filter(check_even,my_nums))


# In[14]:


#Lambda Expressions
#using map functions
#syntax= lambda argument:condition,list


list(map(lambda num:num**2,mynums))


# In[17]:


list(filter(lambda num:num%2==0,my_nums))


# In[18]:


#NESTED STATEMENTS & SCOPE!!!!






# In[31]:


#GLOBAL
name='This is a Global Local'

def greet():
    #Enclosing function local
    name='Sammy'
    
    def hello():
        #LOCAL
        print('Hello '+name)
        
    hello() 


# In[32]:


greet()


# In[1]:


#MILESTONE PROJECT!!!!!!!







# In[3]:


def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    


# In[4]:


row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']


# In[5]:


display(row1,row2,row3)


# In[6]:


row2[2]='O'


# In[8]:


display(row1,row2,row3)


# In[9]:


result= int(input("Enter a position number:"))


# In[10]:


row2[result]


# In[17]:


#Validating USER INPUT!!!!!!!











def user_choice():
    #two major problem with user choice is input datatype & certain range e.g: 0 to 10.
    #1. For datatype, we have to make a default varibale by while loop .
    choice= 'WRONG'
    while choice.isdigit()==False:
        
        choice= input("Please enter a number (0-10):")
        if choice.isdigit()==False:
            print('Sorry! That is not digit.')
            
    return int(choice)            


# In[18]:


user_choice()


# In[20]:


def user_choice():
    #VARIABLE
    
    #Initial
    choice= 'WRONG'
    acceptable_range= range(0,10)
    within_range=False
    
    #TWO CONDITONS TO CHECK
    #DIGIT OR WITHIN_RANGE CHECK==FALSE
    while choice.isdigit()==False:
        
        choice= input("Please enter a number (0-10):")
        
        #DIGIT CHECK
        if choice.isdigit()==False:
            print('Sorry! That is not digit.')
            
        #RANGE CHECK
        if choice.isdigit()== True:
            if int(choice) in acceptable_range:
                within_range=True

            else:
                    print("You are  out of acceptable range 0-10")
                    within_range=False
                    
    return int(choice)    


# In[21]:


user_choice()


# In[22]:


user_choice()


# In[1]:


game_list=[0,1,2]
def display_game(game_list):
    print("Here is the current list:")
    print(game_list)


# In[2]:


display_game(game_list)


# In[3]:


def position_choice():
    
    choice='WRONG'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position number from (0,1,2):")
        
        if choice not in ['0','1','2']:
            print("Sorry! It is not valid!")
     
    return int(choice)                    
                          


# In[4]:


position_choice()


# In[5]:


def replacement_choice(game_list,positon_choice):
    
    user_replacement = input("Add a string:")
    
    game_list[positon_choice] = user_replacement
    
    return game_list


# In[6]:


replacement_choice(game_list,2)


# In[7]:


def gameon_choice():
    
    choice='WRONG'
    
    while choice not in ['Y','N']:
        
        choice= input("keep playing? (Y,N):")
        
        if choice not in ['Y','N']:
            print("Sorry this is invalid!")
            
    if choice== 'Y':
        return True
    else:
        return False
    


# In[8]:


gameon_choice()


# In[ ]:


game_on= True
game_list=[0,1,2]4

while game_on:
    
    display_game(game_list)
    
    position= position_choice()
    
    game_list = replacement_choice(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()


# In[ ]:


#TIC                   TAE                   TAO                 GAME!!!!

#MILESTONE PROJECT 1 





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:





# In[13]:





# In[ ]:





# #### 

# In[ ]:





# 

# In[38]:


from IPython.display import clear_output
def display_board(board):
    clear_output()  # Remember, this only works in jupyter!
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# In[10]:


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# In[11]:


def place_marker(board, marker, position):
    board[position] = marker


# In[12]:


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[13]:


import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[14]:


def space_check(board, position):
    
    return board[position] == ' '


# In[15]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


# In[16]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[17]:


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# In[18]:


#While loop to keep running the game!
print('Welcome to Tic Tac Toe!')

while True:
    #Play the game
    
    #SET EVERYTHING UP(BOARD, WHOS FIRST , CHOOSE MARKERS X,O)
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    ## GAME PLAY
    while game_on:
        if turn == 'Player 1':
            #show the board
            display_board(theBoard)
            #choose a position
            position = player_choice(theBoard)
            #Place the marker on the position
            place_marker(theBoard, player1_marker, position)
            #Check if they won

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[39]:


#OOP







#OBJECT ORIENTED PROGRAMMING!!!!


# In[18]:


#Class Keyword!!!


#CLASS = a kind of template that defines the properties (attributes) and behaviors (methods) that objects of that class will have. 
#It allows you to logically group data and functions in a way that makes them easy to manage and reuse.



class Dog():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF CLASS
    species = 'mammal'
    def __init__(self,breed,name):
        
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name 
    
    def bark(self,number):
        print("Woof! My name is {} and the number is {}".format(self.name,number))


# In[19]:


my_dog = Dog('Huskie','Sammy')


# In[21]:


my_dog.bark(1)


# In[23]:


#Inheritance and Polymorphism class





class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an Animal")
    def eat(self):
        print("I am eating!")


# In[24]:


myanimal= Animal()


# In[26]:


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED!")


# In[28]:


mydog= Dog()


# In[31]:


#POLYMORPHISM!!


# In[35]:


class Dog():
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print("{} says Woof!".format(self.name))


# In[36]:


class Cat():
    def __init__(self,name):
        self.name = name 
    def speak(self):
        return self.name + " says meow!"


# In[37]:


niko = Dog("niko")
felix = Cat("felix")


# In[39]:


for pet in [niko,felix]:
        
        print(type(pet))
        print(pet.speak())


# In[41]:


#OR we can create a function to use same methods for diff class!!

def pet_speak(pet):
    print(pet.speak())


# In[42]:


pet_speak(niko)


# In[47]:


# SPECIAL (MAGIC/DUNDER) METHODS!!!



class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self):
        return self.pages
    


# In[48]:


b = Book("Python rocks","Jose",200)


# In[49]:


#to print a class u need to hv a string representation in your class
print(b)


# In[50]:


#to know the length So use def __len__(self):
len(b)


# In[57]:


#to delete a class or varible :
del b


# In[2]:


####OOP CHALLENGE
##Methods affect attributes!!!




class Account:
    
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self,withdraw):   
        return self.balance - withdraw


# In[3]:


acct1 = Account('Jose',100)


# In[4]:


print(acct1)


# In[5]:


acct1.owner


# In[6]:


acct1.balance


# In[7]:


acct1.deposit(50)


# In[8]:


acct1.withdraw(75)


# In[1]:


#ERRORS AND EXCEPTIONS HANDLING!!!!!!!






# In[3]:


try:
    f = open('testfile','r')
    f.write("Write a test line")
except TypeError:        #writing error str and int
    print("There was a type error!")
except OSError:          # bola h read krne & hum krre write .soo fir ye OSError khelata h !!
    print("Hey you have an OS error!")
finally:                 #no matter error and exception, this block of code will run always !!
    print("I always runs")


# In[4]:


# as we can't remember all the errors name & all !!! therefore we simply do type ,except,else!!
try:
    f = open('testfile','r')
    f.write("Write a test line")
except:
    print("All other exceptions")
finally:                
    print("I always runs")


# In[1]:


def ask_for_int():
    
    while True:
        try:
            result = int(input("Please provide number:"))
        except:
            print("Whoops!That is not a number!")
            continue
        else:
            print("Yes! Thank you.")
            break 
        finally:
            print("End of try\except\finally")
            print("I will always run at the end!")


# In[2]:


ask_for_int()


# In[71]:


#MILESTONE PROJECT 2







# In[107]:


#WARMUP PROJECT!!!
# - Card Class
# -Deck Class
# -Player Class
# -Game Logic 


# In[108]:


#CARD
#SUIT,RANK,VALUES GIVEN TO CARD 


# In[1]:


#Dictionary
#we are using this global variables for deck class!!

import random
suits = {'Hearts','Diamonds','Spades','Clubs'}
ranks = {'Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
         'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[2]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank+ " of " +self.suit


# In[3]:


three_of_clubs = Card("Clubs",'Three')


# In[4]:


three_of_clubs


# In[5]:


print(three_of_clubs)


# In[6]:


three_of_clubs.suit


# In[7]:


three_of_clubs.rank


# In[8]:


three_of_clubs.value


# In[9]:


#Deck Class
#there is no use of inheritance & polymorphism in this class
#Therefore class name ke idhr parenthesis nhi lga h !!
class Deck:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                #adding all card to all_cards as it initally contains nothing in it!!
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        
        return self.all_cards.pop()


# In[10]:


new_deck = Deck()


# In[11]:


len(new_deck.all_cards)


# In[ ]:





# In[12]:


new_deck.shuffle()


# In[13]:


bottom_card = new_deck.all_cards[-1]


# In[14]:


print(bottom_card)


# In[15]:


pick_one =new_deck.deal_one()


# In[16]:


print(pick_one)


# In[17]:


len(new_deck.all_cards)


# In[18]:


#Player Class

class Player:

    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_cards(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
             #list of multiple card object
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)


    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards !'


# In[19]:


new_player = Player("Jose")


# In[20]:


print(new_player)


# In[21]:


#for single card since append is using in this case!!
new_player.add_cards(pick_one)


# In[22]:


print(new_player)


# In[23]:


#for multiple cards or to add a list we use .extend() built-in function!
new_player.add_cards([pick_one,pick_one,pick_one])


# In[24]:


print(new_player)


# In[25]:


#to check for removing the card


# In[26]:


new_player.remove_cards()


# In[27]:


print(new_player)


# In[28]:


#Game logic !!


# In[29]:


#Game Setup
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
        player_one.add_cards(new_deck.deal_one)
        player_two.add_cards(new_deck.deal_one)


# In[30]:


print(player_one)


# In[31]:


game_on = True


# In[32]:


round_num = 0
while game_on:
    round_num +=1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print("Player One has lost the game! Player Two Wins!!!")
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print("Player Two has lost the game! Player One Wins!!!")
        game_on = False
        break
        
    #Start a New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_cards())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_cards())
        
    #While at war!
    at_war = True
    while at_war:
        
        if player_one_cards[-1].value > player_two_cards[-1].value :
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False 
            
        else:
            print("WAR!")
            
            if len(player_one.add_cards) < 5: 
                print("Player ONE is unable to PLay")
                print("Player TWO WINS !!")
                
                game_on = False
                break
                
            elif len(player_two.add_cards) < 5: 
                print("Player TWO is unable to PLay")
                print("Player ONE WINS !!")
                
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_cards())
                    player_two_cards.append(player_two.remove_cards())
                    


# In[1]:


#BLACK JACK GAME !!!!


# In[20]:


import random
suits = {'Hearts','Diamonds','Spades','Clubs'}
ranks = {'Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','King','Queen','Jack'}
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
         'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[48]:


class Deck:
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_cards =  Card(suit,rank)
                self.all_cards.append(created_cards)
    
    def __str__(self):
        deck_comp = ''
        for card in self.all_cards:
            deck_comp += "\n"+ card.__str__()
        return "The Deck has: " +deck_comp
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal(self):
        single_card = self.all_cards.pop()
        return single_card


# In[ ]:


class Hand():
    def __init__(self):
        self.cards = []    #start with an empty list as we did in the Deck class
        self.value = 0    #start with zero value
        self.aces = 0    #add an attribute to keep track of aces
        
    def add_card(self,card):
        #card passed in 
        #from Deck.deal() --> single_card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        
        #IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        #THAN CHANGE MY ACE TO BE A 1 INSTEAD OF 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.values -= 1


# In[ ]:


class Chips:
    
    def __init__(self,total=100):
        self.total = total #This can be set to a default value or supplied by user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




