#strings
#exercise 1
#raw string includes slashes
raw = r'this\t\n and that'

# this\t\n and that
print(raw)

multi = """It was the best of times.
It was the worst of times."""

#print the quote on two lines
# It was the best of times.
#   It was the worst of times.
print(multi)


#exercise 2
#fomatted string literals
value = 2.791514
print(f'approximate value = {value:.2f}')  # approximate value = 2.79

car = {'tires':4, 'doors':2}
print(f'car = {car}') # car = {'tires': 4, 'doors': 2}


#exercise 3
#if statement
#define time_hour
time_hour = 9
#check if time_hour is less than 10
if time_hour < 10: print('coffee')
else: print('water')


#lists
#exercise 1
#define list
colors = ['red', 'blue', 'green']
#access coordinating colors
print(colors[0])    ## red
print(colors[2])    ## green
#print length of list
print(len(colors))  ## 3

#exercise 2
#for in
squares = [1, 4, 9, 16]
#define sum
sum = 0
for num in squares:
    #add sum to num (0 + list sum)
    sum += num
print(sum)  ## 30


#excersise 3
#list slice
list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']