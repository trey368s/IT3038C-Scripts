import numpy as np
phone_number = input("Enter a phone number: ")
phone_num_list = [int(x) for x in str(phone_number)]
reversed_num = np.flipud(phone_num_list)
sorted_num = np.sort(phone_num_list)
shuffled_num = np.array(phone_num_list)
np.random.shuffle(shuffled_num)
print("Reversed Phone Number: " + "".join(map(str, reversed_num)))
print("Sorted Phone Number: " + "".join(map(str, sorted_num)))
print("Shuffled Phone Number: " + "".join(map(str, shuffled_num)))