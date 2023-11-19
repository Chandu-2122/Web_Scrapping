# Web_Scrapping
Web scrapped 'amazon.in' using BeautifulSoup library

# Objective
Collecting electronic gadgets data from amazon which are usually used by a software employee or a student like: 
laptop, tablets, smartphone, smartwatch, headphones, earphones, earbuds considering the offer deals during this diwali season.

# Dataset Description
collecting our required data from the webpage:

**name**: Title of the product

**brand**: Brand of the product

**model name**: Model name of the product

**screen size**: Display size of the screen

**colour**: Colour of the product

**cpu model**: CPU model of the product

**ram memory installed size**: Installed size of ram memory in the product

**operating system**: Operating System of the product

**mrp**: Actual price of the product

**offer**: Offer on the product

**number of purchase in last month**: Number of purchases of the product in last month

**number of ratings**: Number of ratings received for the product

**rating**: Overall rating of the product

# Project Structure
1. **fuctions.py**:
   
   This file has all the functions required to extract the necessary data from the amazon.in website

2. **main.py**:
   
   This file has the main part:

   Web scrapping the required data from 20 pages in the URLs of required products(laptop, tab, smartphone, smartwatch, earphones, earbuds, headphones) and saving it as csv files.

# Data Preparation

With the functions, required data was extracted from the webpage by finding the mentioned tags and if no such tag was found that value is replaced with an empty string.

And then, products having no title value were removed from the dataset and then saved as a csv file.

# Libraries Used

1. **requests** : Used for sending HTTP requests to websites to fetch the HTML content of web pages

2. **BeautifulSoup (from bs4)** : Used for parsing the HTML content obtained using the 'requests' library

3. **pandas** : Used to create the DataFrame to organize and structure the scraped data

4. **numpy** : Used to replace null values

# Results
Was successfully able to web scrape the amazon.in data once before the header i used got blocked or restricted.

# Data Snippet 

![image](https://github.com/Chandu-2122/Web_Scrapping/assets/107211229/21a492cf-4536-4739-8066-b0d7e1ae60a2)


# Conclusion
The success of web scrapping depends on various factors:

   **Headers**: Many websites require a valid user-agent string which allows/blocks/restricts the reuests.

   **Website Policies**: Some websites like amazon are having strict anti-scraping policies that are preventing or limiting scraping attempts.

   **Website Changes**: As we are relying on specific HTML tags to web scrape the data, sometimes our code might not be able to find the required HTML elements if the website changes its structure.





   
       
