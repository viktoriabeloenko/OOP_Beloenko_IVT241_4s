class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Оплата через старую систему: {amount} руб.")


class ModernPaymentInterface:
    def pay(self, amount):
        pass


class PaymentAdapter(ModernPaymentInterface):
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        self.old_system.make_payment(amount)


# Сценарий использования
legacy_system = OldPaymentSystem()
adapter = PaymentAdapter(legacy_system)

adapter.pay(2500)
