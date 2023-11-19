#function to extract the required data
def get_title(soup):
  try:
    #outter tag object
    title = soup.find("span", attrs = {"id":'productTitle'})

    #inner tag object
    title_value = title.text

    #removing starting and ending spaces
    title_string = title_value.strip()

  except AttributeError:
    title_string = ""

  return title_string

def get_type_of_offer(soup):
  try:
    #outter tag object
    type_of_offer = soup.find("span", attrs = {"id":'dealBadgeSupportingText'})

    #inner tag object
    type_of_offer_value = type_of_offer.text

    #removing starting and ending spaces
    type_of_offer_string = type_of_offer_value.strip()

  except AttributeError:
    type_of_offer_string = ""

  return type_of_offer_string

def get_mrp(soup):
  try:
    #outter tag object
    mrp = soup.find("span", attrs = {"class":"a-offscreen"})

    #inner tag object
    mrp_value = mrp.text

    #removing starting and ending spaces
    mrp_string = mrp_value.strip()

  except AttributeError:
    mrp_string = ""

  return mrp_string

def get_offer(soup):
  try:
    #outter tag object
    offer = soup.find("span", attrs = {"class":"a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"})

    #inner tag object
    offer_value = offer.text

    #removing starting and ending spaces
    offer_string = offer_value.strip()

  except AttributeError:
    offer_string = ""

  return offer_string

def get_brand(soup):
  try:
    #outter tag object
    brand = soup.find("tr", attrs = {"class":"a-spacing-small po-brand"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    brand_value = brand.text

    #removing starting and ending spaces
    brand_string = brand_value.strip()

  except AttributeError:
    brand_string = ""

  return brand_string

def get_model(soup):
  try:
    #outter tag object
    model = soup.find("tr", attrs = {"class":"a-spacing-small po-model_name"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    model_value = model.text

    #removing starting and ending spaces
    model_string = model_value.strip()

  except AttributeError:
    model_string = ""

  return model_string

def get_screen_size(soup):
  try:
    #outter tag object
    screen_size = soup.find("tr", attrs = {"class":"a-spacing-small po-display.size"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    screen_size_value = screen_size.text

    #removing starting and ending spaces
    screen_size_string = screen_size_value.strip()

  except AttributeError:
    screen_size_string = ""

  return screen_size_string

def get_colour(soup):
  try:
    #outter tag object
    colour = soup.find("tr", attrs = {"class":"a-spacing-small po-color"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    colour_value = colour.text

    #removing starting and ending spaces
    colour_string = colour_value.strip()

  except AttributeError:
    colour_string = ""

  return colour_string

def get_hard_disk_size(soup):
  try:
    #outter tag object
    hard_disk_size = soup.find("tr", attrs = {"class":"a-spacing-small po-hard_disk.size"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    hard_disk_size_value = hard_disk_size.text

    #removing starting and ending spaces
    hard_disk_size_string = hard_disk_size_value.strip()

  except AttributeError:
    hard_disk_size_string = ""

  return hard_disk_size_string

def get_cpu_model(soup):
  try:
    #outter tag object
    cpu_model = soup.find("tr", attrs = {"class":"a-spacing-small po-cpu_model.family"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    cpu_model_value = cpu_model.text

    #removing starting and ending spaces
    cpu_model_string = cpu_model_value.strip()

  except AttributeError:
    cpu_model_string = ""

  return cpu_model_string

def get_ram_memory_installed_size(soup):
  try:
    #outter tag object
    ram_memory_installed_size = soup.find("tr", attrs = {"class":"a-spacing-small po-ram_memory.installed_size"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    ram_memory_installed_size_value = ram_memory_installed_size.text

    #removing starting and ending spaces
    ram_memory_installed_size_string = ram_memory_installed_size_value.strip()

  except AttributeError:
    ram_memory_installed_size_string = ""

  return ram_memory_installed_size_string

def get_operating_system(soup):
  try:
    #outter tag object
    operating_system = soup.find("tr", attrs = {"class":"a-spacing-small po-operating_system"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    operating_system_value = operating_system.text

    #removing starting and ending spaces
    operating_system_string = operating_system_value.strip()

  except AttributeError:
    operating_system_string = ""

  return operating_system_string

def get_special_features(soup):
  try:
    #outter tag object
    special_features = soup.find("tr", attrs = {"class":"a-spacing-small po-special_feature"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    special_features_value = special_features.text

    #removing starting and ending spaces
    special_features_string = special_features_value.strip()

  except AttributeError:
    special_features_string = ""

  return special_features_string

def get_purchases_in_last_month(soup):
  try:
    #outter tag object
    purchases_in_last_month = soup.find("span", attrs = {"id":"social-proofing-faceout-title-tk_bought"})

    #inner tag object
    purchases_in_last_month_value = purchases_in_last_month.text

    #removing starting and ending spaces
    purchases_in_last_month_string = purchases_in_last_month_value.strip()

  except AttributeError:
    purchases_in_last_month_string = ""

  return purchases_in_last_month_string

def get_rating(soup):
  try:
    #outter tag object
    rating = soup.find("span", attrs = {"id":"acrPopover"}).find("span", attrs = {"class":'a-size-base a-color-base'})

    #inner tag object
    rating_value = rating.text

    #removing starting and ending spaces
    rating_string = rating_value.strip()

  except AttributeError:
    rating_string = ""

  return rating_string

def get_number_of_ratings(soup):
  try:
    #outter tag object
    number_of_ratings = soup.find("span", attrs = {"id":"acrCustomerReviewText"})

    #inner tag object
    number_of_ratings_value = number_of_ratings.text

    #removing starting and ending spaces
    number_of_ratings_string = number_of_ratings_value.strip()

  except AttributeError:
    number_of_ratings_string = ""

  return number_of_ratings_string

def get_reviews(soup):
  rev_list = []
  try:
    for item in soup.find("div", attrs = {"id":"cm-cr-dp-review-list"}).find_all("div", attrs = {"class":"a-expander-content reviewText review-text-content a-expander-partial-collapse-content"}):

      #inner tag object
      rev_list.append(item.text)

  except AttributeError:
    rev_list.append(None)

  return rev_list


def get_memory_storage_capacity(soup):
  try:
    #outter tag object
    memory_storage_capacity = soup.find("tr", attrs = {"class":"a-spacing-small po-memory_storage_capacity"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    memory_storage_capacity_value = memory_storage_capacity.text

    #removing starting and ending spaces
    memory_storage_capacity_string = memory_storage_capacity_value.strip()

  except AttributeError:
    memory_storage_capacity_string = ""

  return memory_storage_capacity_string

def get_max_display_resolution(soup):
  try:
    #outter tag object
    max_display_resolution = soup.find("tr", attrs = {"class":"a-spacing-small po-display.resolution_maximum"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    max_display_resolution_value = max_display_resolution.text

    #removing starting and ending spaces
    max_display_resolution_string = max_display_resolution_value.strip()

  except AttributeError:
    max_display_resolution_string = ""

  return max_display_resolution_string

def get_network_service_provider(soup):
  try:
    #outter tag object
    network_service_provider = soup.find("tr", attrs = {"class":"a-spacing-small po-wireless_provider"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    network_service_provider_value = network_service_provider.text

    #removing starting and ending spaces
    network_service_provider_string = network_service_provider_value.strip()

  except AttributeError:
    network_service_provider_string = ""

  return network_service_provider_string

def get_cellular_technology(soup):
  try:
    #outter tag object
    cellular_technology = soup.find("tr", attrs = {"class":"a-spacing-small po-cellular_technology"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    cellular_technology_value = cellular_technology.text

    #removing starting and ending spaces
    cellular_technology_string = cellular_technology_value.strip()

  except AttributeError:
    cellular_technology_string = ""

  return cellular_technology_string

def get_form_factor(soup):
  try:
    #outter tag object
    form_factor = soup.find("tr", attrs = {"class":"a-spacing-small po-headphones_form_factor"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    form_factor_value = form_factor.text

    #removing starting and ending spaces
    form_factor_string = form_factor_value.strip()

  except AttributeError:
    form_factor_string = ""

  return form_factor_string

def get_connectivity_technology(soup):
  try:
    #outter tag object
    connectivity_technology = soup.find("tr", attrs = {"class":"a-spacing-small po-connectivity_technology"}).find("span", attrs = {"class":"a-size-base po-break-word"})

    #inner tag object
    connectivity_technology_value = connectivity_technology.text

    #removing starting and ending spaces
    connectivity_technology_string = connectivity_technology_value.strip()

  except AttributeError:
    connectivity_technology_string = ""

  return connectivity_technology_string
