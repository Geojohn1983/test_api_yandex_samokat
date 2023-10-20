import requests
import configuration



# создаем новый заказ
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body).json()["track"]

# получаем заказ по треку
def get_order_info(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(track))
