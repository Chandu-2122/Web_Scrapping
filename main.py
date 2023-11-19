#importing necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

#importing functions to extract the data
from functions import *


#main function
if __name__ == '__main__':
  #urls of the webpages
  URLs = ['https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2',
          'https://www.amazon.in/s?k=tab&ref=nb_sb_noss_2',
          'https://www.amazon.in/s?k=smartphone&ref=nb_sb_noss',
          'https://www.amazon.in/s?k=smartwatch&ref=nb_sb_noss_1',
          'https://www.amazon.in/s?k=earphones&ref=nb_sb_noss_2',
          'https://www.amazon.in/s?k=earbuds&ref=nb_sb_noss_2',
          'https://www.amazon.in/s?k=headphones&ref=nb_sb_ss_ts-doa-p_1_4']

  #header for request
  HEADER = ({"User-Agent":""})

  for URL in URLs:
    #HTTP request
    webpage = requests.get(URL, headers=HEADER)

    #check
    urlcount = 1
    print(f"status of URL{urlcount}:", webpage.status_code)
    urlcount +=1
    #soup object containing the data
    soup = BeautifulSoup(webpage.content, "html.parser")

    #last page number
    #assume
    last_page = 20

    #pages list
    pages_list = []

    #extracting each page link
    for page in range(1, last_page+1):
      pages_list.append(URL+f"&page={str(page)}")

    #collecting products' links from each page
    count = 0

    #links list
    links_list = []

    #products in each page
    for page_link in pages_list:
      newpage_webpage = requests.get(page_link, headers = HEADER)
      count+=1
      #check
      print(f"status of page{count}:", newpage_webpage)

      #soup object containing the data of product
      newpage_soup = BeautifulSoup(newpage_webpage.content, "html.parser")

      #<a> tag of each product
      links = newpage_soup.find_all("a", attrs = {'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

      #extracting links from tag
      for link in links:
        links_list.append(link.get('href'))


    #features of each device
    if URL == 'https://www.amazon.in/s?k=laptop&ref=nb_sb_noss_2':
      device = 'laptop'
      d = {"title":[], "type_of_offer":[], "mrp":[], "offer":[], "brand":[], "model":[], "screen_size":[], "colour":[], "hard_disk_size":[], "cpu_model":[], "ram_memory_installed_size":[], "operating_system":[],"special_features":[], "purchases_in_last_month":[], "ratings":[], "number_of_ratings":[], "reviews":[]}

    if URL == 'https://www.amazon.in/s?k=tab&ref=nb_sb_noss_2':
      device = 'tab'
      d = {"title":[], "type_of_offer":[], "mrp":[], "offer":[], "brand":[], "model":[], "memory_storage_capacity":[], "screen_size":[], "max_display_resolution":[], "purchases_in_last_month":[], "ratings":[], "number_of_ratings":[], "reviews":[]}

    if URL == 'https://www.amazon.in/s?k=smartphone&ref=nb_sb_noss':
      device = 'smartphone'
      d = {"title":[], "type_of_offer":[], "mrp":[], "offer":[], "brand":[], "model":[], "network_service_provider":[], "operating_system":[], "cellular_technology":[], "purchases_in_last_month":[], "ratings":[], "number_of_ratings":[], "reviews":[]}

    if URL == 'https://www.amazon.in/s?k=smartwatch&ref=nb_sb_noss_1':
      device = 'smartwatch'
      d = {"title":[], "type_of_offer":[], "mrp":[], "offer":[], "colour":[], "brand":[], "model":[], "network_service_provider":[], "operating_system":[], "cellular_technology":[], "purchases_in_last_month":[], "ratings":[], "number_of_ratings":[], "reviews":[]}

    if URL == 'https://www.amazon.in/s?k=earphones&ref=nb_sb_noss_2' or URL == 'https://www.amazon.in/s?k=headphones&ref=nb_sb_ss_ts-doa-p_1_4' or URL == 'https://www.amazon.in/s?k=earbuds&ref=nb_sb_noss_2':
      device = 'earphones'
      d = {"title":[], "type_of_offer":[], "mrp":[], "offer":[], "brand":[], "model":[], "colour":[], "form_factor":[], "connectivity_technology":[], "purchases_in_last_month":[], "ratings":[], "number_of_ratings":[], "reviews":[]}

    product = 0
    #product webpage
    for link in links_list:
      new_webpage = requests.get("https://www.amazon.in" + link, headers = HEADER)

      #check
      product+=1

      print(f"status of product:{product}", new_webpage)

      #soup object containing the data of product
      new_soup = BeautifulSoup(new_webpage.content, "html.parser")

      #if its laptop extract these features
      if device == 'laptop':
        d['title'].append(get_title(new_soup))
        d['type_of_offer'].append(get_type_of_offer(new_soup))
        d['mrp'].append(get_mrp(new_soup))
        d['offer'].append(get_offer(new_soup))
        d['brand'].append(get_brand(new_soup))
        d['model'].append(get_model(new_soup))
        d['screen_size'].append(get_screen_size(new_soup))
        d['colour'].append(get_colour(new_soup))
        d['hard_disk_size'].append(get_hard_disk_size(new_soup))
        d['cpu_model'].append(get_cpu_model(new_soup))
        d['ram_memory_installed_size'].append(get_ram_memory_installed_size(new_soup))
        d['operating_system'].append(get_operating_system(new_soup))
        d['special_features'].append(get_special_features(new_soup))
        d['purchases_in_last_month'].append(get_purchases_in_last_month(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['number_of_ratings'].append(get_number_of_ratings(new_soup))
        d['reviews'].append(get_reviews(new_soup))

      if device == 'tab':
        d['title'].append(get_title(new_soup))
        d['type_of_offer'].append(get_type_of_offer(new_soup))
        d['mrp'].append(get_mrp(new_soup))
        d['offer'].append(get_offer(new_soup))
        d['brand'].append(get_brand(new_soup))
        d['model'].append(get_model(new_soup))
        d['memory_storage_capacity'].append(get_memory_storage_capacity(new_soup))
        d['screen_size'].append(get_screen_size(new_soup))
        d['max_display_resolution'].append(get_max_display_resolution(new_soup))
        d['purchases_in_last_month'].append(get_purchases_in_last_month(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['number_of_ratings'].append(get_number_of_ratings(new_soup))
        d['reviews'].append(get_reviews(new_soup))

      if device == 'smartphone':
        d['title'].append(get_title(new_soup))
        d['type_of_offer'].append(get_type_of_offer(new_soup))
        d['mrp'].append(get_mrp(new_soup))
        d['offer'].append(get_offer(new_soup))
        d['brand'].append(get_brand(new_soup))
        d['model'].append(get_model(new_soup))
        d['network_service_provider'].append(get_network_service_provider(new_soup))
        d['operating_system'].append(get_operating_system(new_soup))
        d['cellular_technology'].append(get_cellular_technology(new_soup))
        d['purchases_in_last_month'].append(get_purchases_in_last_month(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['number_of_ratings'].append(get_number_of_ratings(new_soup))
        d['reviews'].append(get_reviews(new_soup))

      if device == 'smartwatch':
        d['title'].append(get_title(new_soup))
        d['type_of_offer'].append(get_type_of_offer(new_soup))
        d['mrp'].append(get_mrp(new_soup))
        d['offer'].append(get_offer(new_soup))
        d['colour'].append(get_colour(new_soup))
        d['brand'].append(get_brand(new_soup))
        d['model'].append(get_model(new_soup))
        d['network_service_provider'].append(get_network_service_provider(new_soup))
        d['operating_system'].append(get_operating_system(new_soup))
        d['cellular_technology'].append(get_cellular_technology(new_soup))
        d['purchases_in_last_month'].append(get_purchases_in_last_month(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['number_of_ratings'].append(get_number_of_ratings(new_soup))
        d['reviews'].append(get_reviews(new_soup))

      if device == 'earphones':
        d['title'].append(get_title(new_soup))
        d['type_of_offer'].append(get_type_of_offer(new_soup))
        d['mrp'].append(get_mrp(new_soup))
        d['offer'].append(get_offer(new_soup))
        d['brand'].append(get_brand(new_soup))
        d['model'].append(get_model(new_soup))
        d['colour'].append(get_colour(new_soup))
        d['form_factor'].append(get_form_factor(new_soup))
        d['connectivity_technology'].append(get_connectivity_technology(new_soup))
        d['purchases_in_last_month'].append(get_purchases_in_last_month(new_soup))
        d['ratings'].append(get_rating(new_soup))
        d['number_of_ratings'].append(get_number_of_ratings(new_soup))
        d['reviews'].append(get_reviews(new_soup))

      amazon_df = pd.DataFrame.from_dict(d)
      #removing the products with no title
      amazon_df['title'].replace('', np.nan, inplace = True)
      amazon_df = amazon_df.dropna(subset = ['title'])
      amazon_df.to_csv(f"amazon_{device}_data.csv", header = True)


