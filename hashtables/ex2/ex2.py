#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
	HashTable,
	hash_table_insert,
	hash_table_retrieve,
	)


class Ticket:
	def __init__(self, source, destination):
		self.source = source
		self.destination = destination


def reconstruct_trip(tickets, length):
	hashtable = HashTable(length)
	route = [None] * length

	"""
	YOUR CODE HERE
	"""
	# Add tickets to hash table
	for ticket in tickets:
		hash_table_insert(hashtable, ticket.source, ticket.destination)

	# Start the route with the ticket that has source None
	route[0] = hash_table_retrieve(hashtable, "NONE")

	# Keep looping through the
	for i in range(1, length):
		route[i] = hash_table_retrieve(hashtable, route[i-1])

	return route
