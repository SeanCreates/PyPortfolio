#Call Stack memory in managing functions
class UndoStack:
    """
    Simulates a stack-based history for an undo feature.
    Uses LIFO (Last In - First Out)
    """
    def __init__(self):
        #The list 'history' acts as the stack.
        self.history = []
        print("Stack Initialized. History is empty.")
    def execute_command(self, command: str):
        """
        Pushes a new command onto the stack (LIFO: last in, first out)
        Equivalent to a 'push' operation.
        """
        self.history.append(command)
        print(f"Executed Command: {command}.")
        self.display_status()

    def undo(self):
        if self.history:
            last_command = self.history.pop()
            print(f"UNDO Command: {last_command}.")
        else:
            print("Cannot Undo. Stack is empty.")
        self.display_status()

    def display_status(self):
        if self.history:
            print(f"[Stack Status: Top -> {self.history[-1]}, Total: {len(self.history)}]")
        else:
            print("[Stack Status: Empty]")


def main():
    manager = UndoStack()

    print("command execution sequence:")
    manager.execute_command("Change background color to blue")
    manager.execute_command("Insert Image 'img.png'")
    manager.execute_command("Resize the image")

    print("Undo Last Command:")
    manager.undo()
    manager.undo()

    manager.execute_command("Add textbox to 'Header'")
    manager.undo()
    manager.undo()

if __name__ == "__main__":
    main()









