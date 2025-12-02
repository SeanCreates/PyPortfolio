class UndoStack:
    """
    Simulates a stack-based history for an undo feature.
    Uses LIFO (Last-In, First-Out) principle, implemented with a Python List.
    """

    def __init__(self):
        # The list 'history' acts as the stack.
        self.history = []
        print("Stack initialized. History is empty.")

    def execute_command(self, command: str):
        """
        Pushes a new command onto the stack (LIFO: Last-In, First-Out).
        Equivalent to a 'push' operation.
        """
        # List.append() adds the item to the end (the 'top' of the stack)
        self.history.append(command)
        print(f"✅ Executed command: '{command}'.")
        self.display_status()

    def undo(self):
        """
        Pops the last command from the stack.
        Equivalent to a 'pop' operation.
        """
        if self.history:
            # List.pop() removes and returns the item at the end (the 'top' of the stack)
            last_command = self.history.pop()
            print(f"↩️ UNDO: Reversed command: '{last_command}'.")
        else:
            print("🛑 Cannot undo: History stack is empty.")
        self.display_status()

    def display_status(self):
        """Prints the current contents of the stack."""
        if self.history:
            # We display the stack from top to bottom (last element added is first)
            print(f"   [Stack Status: Top -> {self.history[-1]}, Total: {len(self.history)}]")
        else:
            print("   [Stack Status: EMPTY]")


# --- Main Program Execution ---
def main():
    manager = UndoStack()

    print("\n--- Command Execution Sequence ---")
    manager.execute_command("Change background color to blue")
    manager.execute_command("Insert image 'logo.png'")
    manager.execute_command("Resize selected object")

    print("\n--- Undo Actions ---")
    # Undo the last command (Resize selected object)
    manager.undo()

    # Undo the next command (Insert image 'logo.png')
    manager.undo()

    # Try to undo when the stack is empty or almost empty
    manager.execute_command("Add text box 'Header'")
    manager.undo()
    manager.undo()  # Should fail here


if __name__ == "__main__":
    main()