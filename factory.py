from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotification(Notification):
    def send(self, message: str):
        print(f"Email: {message}")


class SMSNotification(Notification):
    def send(self, message: str):
        print(f"SMS: {message}")


class PushNotification(Notification):
    def send(self, message: str):
        print(f"Push: {message}")


class NotificationFactory:
    @staticmethod
    def create(notification_type: str) -> Notification:
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError("Неизвестный тип уведомления")


# Сценарий использования
factory = NotificationFactory()

email = factory.create("email")
email.send("Добро пожаловать!")

sms = factory.create("sms")
sms.send("Ваш код подтверждения")
