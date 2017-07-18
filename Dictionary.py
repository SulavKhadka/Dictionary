"""
Get a definition of a word from Merriam Webster based on user input.
This script uses Dictionary API by Merriam Webster to access the information about a given word
"""


# Native libraries
import urllib2
import xml.etree.cElementTree as Et


# Gets the raw XML data from the api, sends it to xml_parse and returns the clean results as a dict.
def dictionary_info(query, api_key):
	try:
		data = urllib2.urlopen('http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{}?key={}'.format(query, api_key))
	except urllib2.URLError:
		print "Please check to your internet connection"
		exit()

	xml_string = data.read()
	data.close()
	parsed_result = xml_parse(query, xml_string)
	return parsed_result


# Extracts specific entities from the raw XML data and returns results as a dict depending on the type of page returned.
def xml_parse(query, xml_string):

	root = Et.fromstring(xml_string)
	try:
		page_tag = root[0].tag
	except IndexError:
		return dict(type='error', text='I cant seem to find the word you are looking for')

	if page_tag == 'entry':
		label = root.find('./entry/fl')
		if label is not None:
			if label.text != "geographical name" and label.text != "biographical name":
				pass
			else:
				print "This word is a {}, we deal with that off-site!!".format(label.text)
				exit()
		word = root.find('./entry/ew')
		if word is None:
			word = "* Can't Find Word *"
		origin = root.find('./entry/et')
		if origin is None:
			origin = ""
		origin_date = root.find('./entry/def/date')
		if origin_date is None:
			origin_date = ""
		definition = ""
		for i in root.find('.entry/def/dt').itertext():
			definition = definition + i.strip()
		def_dict = dict(type='entry', word=word, origin=origin, origin_date=origin_date, definition=definition)
		return def_dict

	elif page_tag == 'suggestion':
		suggestions = root.findall('./suggestion')
		suggest_dict = dict(type='suggestion', query=query)
		counter = 0
		for i in suggestions:
			if counter != 3:
				suggest_dict[str(counter)] = i.text
				counter += 1
			else:
				pass
		return suggest_dict


# Prints the final results to the terminal screen.
def display_output(page_result):

	if page_result['type'] == "entry":
		print '{} ({}->{}):\n {}'.format(page_result['word'].text.upper(),
										 page_result['origin'].text,
										 page_result['origin_date'].text,
										 page_result['definition'])
	elif page_result['type'] == "suggestion":
		query = page_result['query']
		print "I was unable to find {}, did you mean:".format(query)
		for i in page_result:
			if i != 'type' and i != 'query':
				print page_result[i]
		get_input()
	else:
		print page_result['text']


def get_input():
	API_KEY = raw_input("Please enter your Merriam Webster dictionary API key:")
	query = raw_input("Enter Query:")
	output_dict = dictionary_info(query, API_KEY)
	display_output(output_dict)

if __name__ == '__main__':
	get_input()