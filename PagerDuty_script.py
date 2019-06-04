import sys

def customers_pages(file_name, target_customer):
	customer_log = {}
	# empty dict to contain customer IDs and the page IDs they have visisted

	for line in file_name:
		log = line.rstrip().replace(" ", "").split(",")
		# strip white space to the right
		# take away (replace) extra spaces
		# seperate information by the commas creating a list of the items for that log

		time, customer_ID, page_ID = log
		# unpacking list of the three items into variables

		if customer_ID not in customer_log:
			customer_log[customer_ID] = []
			# creating key-value pairs with empty list as value
			# if customer ID key does not exist
		customer_log[customer_ID].append(page_ID)
		# filling dict using customer ID keys and appending to their value
		# which is a list

	if target_customer in customer_log:
		print ", ".join(customer_log[target_customer])
		# presents the list value on a single line as a string

	else:
		print "Sorry, that customer does not exist."
		# in case the target customer ID does not exist in the file


with open(sys.argv[1]) as file_name:
# read in file from terminal line
# using 'with' will open and close the file after use
# so as to not create errors if the file is continuously used for something else
	target_customer = sys.argv[2]
	# also from the terminal line, take in customer ID to look up 
	customers_pages(file_name, target_customer)
	# calling the function