# create a mapping of state to abbreviathion
states = {
 'Oregon': 'OR',
 'Floride': 'EL',
 'California': 'CA'
 'New york': 'NY'
 'Michigen': 'MI'
 }
 
 # create a basic set of states and some cities in them 
cities = {
 'CA': 'san Francisco',
 'MI': 'Detroit',
 'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities 
print '_' * 10
print "NY State has: ", cities['NY']
print "OR state has: ", cities['OR']

# print some states
print '_' * 10