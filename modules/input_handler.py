from modules.command import Command


class InputHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command: Command, command_name) -> None:
        if command_name not in self.commands:
            self.commands[command_name] = []
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name not in self.commands:
            print("Comando não encontrado")
            return
        self.commands[command_name].execute()