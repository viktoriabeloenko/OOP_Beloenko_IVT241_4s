from abc import ABC, abstractmethod


class DataService(ABC):
    @abstractmethod
    def get_data(self):
        pass


class ApiService(DataService):
    def get_data(self):
        return "Данные из API"


class ServiceDecorator(DataService):
    def __init__(self, service: DataService):
        self.service = service


class LoggingDecorator(ServiceDecorator):
    def get_data(self):
        print("[LOG] Запрос данных")
        result = self.service.get_data()
        print("[LOG] Данные получены")
        return result


service = ApiService()
logged_service = LoggingDecorator(service)

print(logged_service.get_data())
