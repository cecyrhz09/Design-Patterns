'''
Created on 23 nov. 2019

@author: Cecy Rodríguez
'''

''' our iterator implementation'''
def count_to(count):
    #List
    antibiotics = ['Penicillin', 'Dichloxacillin', 'Chloramphenicol','Ciprofloxacin',
                    'Streptomycin', 'Amoxicillin']
    #Our built-in iterator
    #Creates a tuple such as (1, Penicillin)
    iterator = zip(range(count), antibiotics)
    
    #Iterate  throuh our iterable list 
    #Extract the Antibiotics
    #Put them in a generator called number 
    
    for position, number in iterator:
        #Returns a generator containing antibiotics
        yield number
        
#Let's  test the generator  returned by our iterator 
for num in count_to(3):
    print("{}".format(num))
    
for num in count_to(5):
    print("{}".format(num))
   
    
     
     