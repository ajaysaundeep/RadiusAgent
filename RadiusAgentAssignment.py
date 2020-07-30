import urllib.request
from bs4 import BeautifulSoup
import re
import json

#filesystem path for HTML page
file_path = "file:///media/ajay/New%20Volume/Radius%20Agent%20Assignment/New%20Lead%20%20(3).html"
#output file name
output_file_name = "property_details.json"
property_details = {}

regex_dict = {
    #Regular Expression for Name
    'name' : re.compile(r'Name [a-z,A-z .`-]+$'),
    #Regular Expression for Email
    'email': re.compile(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'),
    #Regular Expression for Phone Number
    'phone': re.compile(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$'),
    #Regular Expression for Bed
    'beds' : re.compile(r'Beds (\d+)'),
    #Regular Expression for Address
    'address': re.compile(r'(.)*interested in [0-9a-z,A-z .`-]+(.)*$')
}

def parse_line(line):
    """
    Do a regex search against all defined regexes and
    return the key and match result of the first matching regex
    
    """
    for key, rx in regex_dict.items():
        match = rx.search(line)
        if match:
            return key, match.group(0)
    # if there are no matches
    return None, None

def extract_text_from_webpage(html_page):
    """
      It extracts the useful/required text from HTML page
    """
    # create a new bs4 object from the html data loaded
    soup = BeautifulSoup(html_page, "html.parser") 
    # remove all javascript and stylesheet code
    for script in soup(["script", "style"]): 
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines

def parse_file(filepath):
    '''
    parse text at given filepath
    
    Parameters
    -----------
    filepath : str
          filepath for file_object to be parsed

    Returns
    --------
    property_details : Dictionary
           property_details that contains key-value pair about property
    '''
    page = urllib.request.urlopen(filepath)
    extracted_text = extract_text_from_webpage(page.read())
    for line in extracted_text:
        key,value = parse_line(line)
        if key in ['name','beds']:
            property_details[key] = value.split(" ",1)[1]
        elif key == 'address':
            property_details[key] = value.split("interested in ",1)[1]    
        elif key != None:
            property_details[key] = value
    return property_details    

def store_property_details_json_format(property_details_json):
    """
      Stores the Dictionary in json format in specified path (output_file_name)
    """
    with open(output_file_name, 'w') as fp:
        json.dump(property_details_json, fp)

if __name__=='__main__':
    property_details_json = parse_file(file_path)
    store_property_details_json_format(property_details_json)
