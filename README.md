# RadiusAgent

### Objective

Parsing the required information about the property and user from webpage

### Problem Statement
Agents receive emails from the different lead sources that they have and that has the information of the buyers/sellers looking to buy or sell the property

### Installation

* Install the python3
  * `sudo apt-get install python3`
* Install the pip3
  * `sudo apt-get install python3-pip`
* Install the bs4
  * `pip install bs4`  
* Run it
  * `python3 RadiusAgentAssignment.py`
  
 ### Code Changes
 
 change the file_path to location where the html page is stored in your local system
 
![image](https://user-images.githubusercontent.com/27794146/88887488-1b972000-d25a-11ea-97f8-91b7c01e16cc.png)

### Algorithm

#### Extracting the Data 

The webpage is comprised of HTML, CSS and scripts and the requirement is to scrape the Data(required Information). This tasks was done with help of Python Library  named BeautifulSoup that retrieves the information present in webpage. Since retrieved text containes lot unwanted junks like CSS, scripts therefore those where removed to get text with required information and is subdivided into multiple lines .

#### Regular Expressions

Regular Expressions played a vital role by finding pattern in given text for required information.


### Result

Property Details in JSON Format

![image](https://user-images.githubusercontent.com/27794146/88888111-53529780-d25b-11ea-8fbd-181427de35bf.png)


  
