import sender_stand_request
import data


#  успешный ответ на запрос на получение заказа по треку заказа
def test_get_order_success():
    track = sender_stand_request.post_new_order(data.order_body)
    order_response = sender_stand_request.get_order_info(track)
    # Проверяется, что код ответа равен 200
    assert order_response.status_code == 200
