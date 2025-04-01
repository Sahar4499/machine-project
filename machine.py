class Machine:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def start(self):
        if not self.is_on:
            self.is_on = True
            print(f"{self.name} has been started.")
        else:
            print(f"{self.name} is already running.")

    def stop(self):
        if self.is_on:
            self.is_on = False
            print(f"{self.name} has been stopped.")
        else:
            print(f"{self.name} is already off.")

    def status(self):
        state = "running" if self.is_on else "off"
        print(f"The machine '{self.name}' is currently {state}.")
