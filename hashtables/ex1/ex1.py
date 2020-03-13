#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
	HashTable,
	hash_table_insert,
	hash_table_remove,
	hash_table_retrieve,
	hash_table_resize
	)


def get_indices_of_item_weights(weights, length, limit):
	ht = HashTable(16)

	# Add weights and their indeces to the hashtable
	for item in range(0, length):
		hash_table_insert(ht, weights[item], item)
	
	# Check the hashtable for the value that equals the limit minus the weight in the weights list
	for index in range(0, length):
		difference = limit - weights[index]

		# Check for difference in hashtable
		check_hashtable = hash_table_retrieve(ht, difference)

		if check_hashtable is not None:
			if check_hashtable > index:
				return (check_hashtable, index)
			else:
				return (index, check_hashtable)

	return None


def print_answer(answer):
	if answer is not None:
		print(str(answer[0] + " " + answer[1]))
	else:
		print("None")
