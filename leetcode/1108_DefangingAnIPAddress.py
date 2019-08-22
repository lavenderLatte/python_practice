"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".


Example 1:

	Input: address = "1.1.1.1"
	Output: "1[.]1[.]1[.]1"

Example 2:

	Input: address = "255.100.50.0"
	Output: "255[.]100[.]50[.]0"
"""

def defangIPaddress(ip):

	# put input into a list separated by "."
	lst = ip.split(".")  

	# put items in the list together joined by "[.]" 
	res = ("[.]".join(lst))

	return (res)

print (defangIPaddress("255.100.50.0"))