#Prints data from python: adds a u before each isotope (u'ir191': 0.0,)
import json
from pprint import pprint

data = json.load(open('data.JSON'))
particle = data[99]
print particle ['c12']
#pprint(data)

#Found above example at https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file. Tried to parse out values using Justin Peel's example, but couldn't determine what values in the example file corruspond with the values in the actual, data.JSON  file. 
