from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass


class StandardDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return 5 + weight * 0.5


class ExpressDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return 15 + weight * 1.5


class DroneDelivery(DeliveryStrategy):
    def calculate(self, weight: float) -> float:
        return 50 + weight * 3


class DeliveryContext:
    def __init__(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy):
        self.strategy = strategy

    def calculate_price(self, weight: float):
        return self.strategy.calculate(weight)


context = DeliveryContext(StandardDelivery())
print("Обычная доставка:", context.calculate_price(10))

context.set_strategy(ExpressDelivery())
print("Экспресс доставка:", context.calculate_price(10))

context.set_strategy(DroneDelivery())
print("Доставка дроном:", context.calculate_price(10))

