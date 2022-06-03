ImmoEliza

## The ussage of the machine

Scrap the webpages link that contains information about houses and apartaments for sale.
Saves the links in a text file
Intiterate the text file containing the links to perform scrapping of the data.
Creates a DataFrame with all the information contained on the website.

## Install & Run it

Is based Python3 , so we need to be sure that we have it on the pc, or install it if not

Steps:

1. Clone the repo to your computer.
2. Install Requests  
   `$ pip3 install requests`
3. Install Pandas  
   `$ pip3 install pandas`
4. Install Selenium  
   `$ pip3 install selenium`  
ATENTION: Make Sure do have `geckodriver` ussed for webdrive scrapping as all the testing and running was made on FIREFOX

## Usage

Get the links to the pages of real state objects by running `Links_Grab.py`. The results will be saved into `url_links.txt` file.

There is a probabily to have dubplicates on the links, i reccomand clean it manualy , the software does not includes a cleaning.

Run `main.py` to extract the data directly in `data.csv` file 

The example can be seen in the repository

Enjoy your new collected information.
