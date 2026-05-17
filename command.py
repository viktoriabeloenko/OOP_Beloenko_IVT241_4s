from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Свет включен")

    def off(self):
        print("Свет выключен")


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    def submit(self, command: Command):
        command.execute()


# Сценарий использования
light = Light()
remote = RemoteControl()

on_command = LightOnCommand(light)
off_command = LightOffCommand(light)

remote.submit(on_command)
remote.submit(off_command)
