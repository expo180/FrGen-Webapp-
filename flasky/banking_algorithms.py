#Thursday before I move on Abu Dhabi 
#This part of code generates a random account  for identification purposes
import random
import math
#create an array containing all the alphabet letters from A-Z in order to increase the number of possibilities
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#generates a new alphabet array with a new configuration 
random.shuffle(alphabet)
#assign the first new array item to a variable
key_value_one = alphabet[0]
key_value_two = alphabet[1]
key_value_three = alphabet[2] + "-"
first_alphaId = (key_value_one + key_value_two + key_value_three).upper()
#initializes a random number
key_randomNumber_one = str(math.floor(random.random()*10))
key_randomNumber_two = str(math.floor(random.random()*10))
key_randomNumber_three = str(math.floor(random.random()*10))
key_randomNumber_four = str(math.floor(random.random()*10))
key_randomNumber_five = str(math.floor(random.random()*10))
key_randomNumber_six = str(math.floor(random.random()*10))
key_randomNumber_seven = str(math.floor(random.random()*10))
key_randomNumber_eight = str(math.floor(random.random()*10))
#create the second digitId
secdigId = key_randomNumber_one + key_randomNumber_two + key_randomNumber_three + "-"
#create the third digitId
thdigId = key_randomNumber_four + key_randomNumber_five + key_randomNumber_six + key_randomNumber_seven + key_randomNumber_eight 
#create the unique account Id for an alpha user
account_id = first_alphaId + secdigId + thdigId

