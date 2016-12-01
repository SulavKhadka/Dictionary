import urllib2
import xml.etree.cElementTree as ET


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


def xml_parse(query, xml_string):

    root = ET.fromstring(xml_string)
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
    else:
        print page_result['text']


def main():
    word = raw_input('Enter a word to lookup: ')
    api_key = "94125589-6e52-4cbe-a6f8-b8ae5b3bed42"
    output_dict = dictionary_info(word, api_key)
    display_output(output_dict)

main()



