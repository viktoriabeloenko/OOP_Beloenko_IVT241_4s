from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def next_state(self, order):
        pass

    @abstractmethod
    def status(self):
        pass


class CreatedState(OrderState):
    def next_state(self, order):
        order.state = PaidState()

    def status(self):
        return "Заказ создан"


class PaidState(OrderState):
    def next_state(self, order):
        order.state = ShippedState()

    def status(self):
        return "Заказ оплачен"


class ShippedState(OrderState):
    def next_state(self, order):
        order.state = DeliveredState()

    def status(self):
        return "Заказ отправлен"


class DeliveredState(OrderState):
    def next_state(self, order):
        print("Заказ уже доставлен")

    def status(self):
        return "Заказ доставлен"


class Order:
    def __init__(self):
        self.state = CreatedState()

    def next(self):
        self.state.next_state(self)

    def current_status(self):
        print(self.state.status())


# Сценарий использования
order = Order()

order.current_status()
order.next()

order.current_status()
order.next()

order.current_status()
order.next()

order.current_status()
