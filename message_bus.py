class MessageBus:
    def __init__(self):
        self.handlers = {}

    def subscribe(self, event_name, handler):
        if event_name not in self.handlers:
            self.handlers[event_name] = []

        self.handlers[event_name].append(handler)

    def publish(self, event_name, data):
        if event_name in self.handlers:
            for handler in self.handlers[event_name]:
                handler(data)


# Обработчики

def send_email(data):
    print(f"Email отправлен пользователю {data['user']}")



def create_log(data):
    print(f"LOG: пользователь {data['user']} зарегистрирован")


# Сценарий использования
bus = MessageBus()

bus.subscribe("user_registered", send_email)
bus.subscribe("user_registered", create_log)

bus.publish("user_registered", {
    "user": "admin"
})
