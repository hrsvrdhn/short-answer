# MADE BY HARSH
# harshavardhana.619@gmail.com
def master_greet():
	return "Welcome from master"
import urllib
def greetperson():
	return "Welcome to shortanswer"

base_url="http://api.wolframalpha.com/v1/result?"
my_api="your api here"
query=raw_input("What can I find for you ? \n")
url=base_url+urllib.urlencode({"appid":my_api,"i":query})
html=urllib.urlopen(url).read()
print html
query = raw_input("Press C to cancel or Y to continue : ")
while query == 'Y':
	query=raw_input("What can I find for you ? \n")
	try:
		url=base_url+urllib.urlencode({"appid":my_api,"i":query})
		html=urllib.urlopen(url).read()
	except:
		print "Sorry :( , cant't process your request"
	print html
	query = raw_input("Press C to cancel or Y to continue : ")
print "Thank you for trying this"