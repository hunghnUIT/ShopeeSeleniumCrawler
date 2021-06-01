from selenium.common.exceptions import NoSuchElementException


# Settings
from settings import (
    CLASS_NAME_NAME_ITEM, CLASS_NAME_ROW_STARS, 
    CLASS_NAME_STAR, CLASS_NAME_SOLD_NUMBER, 
    CLASS_NAME_PRICE, 
)

# Functions
from helper import ( 
    process_item_url, calculate_rating, 
    convert_string_to_int, get_current_time_in_ms,
)

import timing_value

def extract_data_from_category_dom_object(dom_object:object, category_id:int) -> object:
    item = {} # FIXME change to model later.
    try:
        product_url = dom_object.find_element_by_tag_name('a').get_attribute('href')
        info_from_url = process_item_url(product_url)
        stars = dom_object.find_elements_by_css_selector(f'.{CLASS_NAME_ROW_STARS} .{CLASS_NAME_STAR}')
        sold = dom_object.find_element_by_class_name(CLASS_NAME_SOLD_NUMBER).text

        item['id'] = info_from_url['itemId']
        item['name'] = dom_object.find_element_by_class_name(CLASS_NAME_NAME_ITEM).text
        item['sellerId'] = info_from_url['sellerId']
        item['categoryId'] = category_id
        item['productUrl'] = product_url
        item['rating'] = calculate_rating(stars) if stars else 0
        item['totalReview'] = convert_string_to_int(sold.split(" ")[-1]) if sold else 0
        item['update'] = get_current_time_in_ms()
        item['expired'] = timing_value.expiredTime
        item['currentPrice'] = convert_string_to_int(dom_object.find_element_by_class_name(CLASS_NAME_PRICE).text)
        item['thumbnailUrl'] =  dom_object.find_element_by_tag_name('img').get_attribute('src')
        if not item['thumbnailUrl']:
            return {
                'success': False, 
                'data': item,
            }
        else:
            return {
                'success': True, 
                'data': item,
            }

    except NoSuchElementException:
        return {
                'success': False, 
                'data': None,
            }

# These fields below is usually failed.
def extract_field_from_category_dom_object(key:str, dom_object:object) -> any:
    switcher = {
        'thumbnailUrl': dom_object.find_element_by_tag_name('img').get_attribute('src')
    }
    return switcher.get(key, None) 