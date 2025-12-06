
# Write a program that will take as input a string of cities along with their city identification numbers. The city ID, City name pair will be comma separated.

# Your program should process these cities into a hash table (with 10 slots) using the simple hash function with chaining for handling collision.

# Note that there should be a single white space at the end of each line, whether it ends with a number or a city name.

# For example, if input is:

# 10 Cincinnati,11 Chicago,12 Boston,20 SouthBend,45 Florence
# The output would be:

# 0 Cincinnati SouthBend 

# 1 Chicago 

# 2 Boston 

# 3 

# 4 

# 5 Florence 

# 6 

# 7 

# 8 

# 9  


#This is definitely convoluted but at least I'm getting somewhere
#My solution is to take the input of comma separated strings and place them in the below variables
cities_raw = input()
cities_filtered = cities_raw.split(',')
cities_array = []
city_ids = []
city_names = []
#this is the hash table
hash_list = [ [], [], [], [], [], [], [], [], [], []]


#this first for loop is to split up strings based on commas. the end result will have something like [10 City]
for city in cities_filtered:
    cities_array.append(city.split())

#this for loop will then split the ids into one array and cities into the other. 
for city in cities_array:
    city_id = int(city[0])
    city_name = city[1]
    #sprinkle a little simple hash
    index = city_id % 10
    hash_list[index].append(city_name)
