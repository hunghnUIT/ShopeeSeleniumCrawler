import requests
from settings import RECEIVE_NOTIFICATION_SERVICE_ADDRESS


def notify_web_service_about_decreased_price(item_id: int, new_price: int, is_trying_again: bool = False):
    url = f'{RECEIVE_NOTIFICATION_SERVICE_ADDRESS}?itemId=${item_id}&newPrice=${new_price}&platform=shopee'
    try:
        response = requests.get(url)

        if response and response.status_code == requests.codes.ok:
            print('Notified web service about decreased price')
        elif (not response and not is_trying_again) or (response['status'] != 200 and not is_trying_again):
            notify_web_service_about_decreased_price(item_id, True)
        elif (not response and is_trying_again) or (response['status'] != 200 and is_trying_again):
            print('Notify to web service failed')
    except requests.exceptions.HTTPError as errHttp:
        print ("Http Error:",errHttp)
    except requests.exceptions.ConnectionError as errConnect:
        print ("Error Connecting:",errConnect)
    except requests.exceptions.Timeout as errTimeout:
        print ("Timeout Error:",errTimeout)
    except requests.exceptions.RequestException as err:
        print ("OOps: Something Else",err)

