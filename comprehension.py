# nested list comprehension

nums = [1,2,3,4,5]
letters = ["a", "b", "c", "d"]
my_list = [letter + str(num) for letter in letters for num in nums]

#-----------------------------------------------------------------
# lists to dectionary using comprehension

first_name = ["ahmed", "mohamed"]
last_name = ["khaled", "hussein"]
my_dict = {key:value for key,value in zip(first_name, last_name)}

#-----------------------------------------------------------------
# list to set using comprehension

my_list2 = [1,2,2,2,2,15,2,19,19,5]
my_set = {item for item in my_list2}
