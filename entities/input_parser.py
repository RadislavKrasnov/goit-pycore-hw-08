"""User input parser"""

class InputParser:
    def parse_input(self, user_input: str) -> tuple:
        """Parse user input and return command and its arguments.

        Args:
            user_input: 
                String that is user input command and its arguments.
        
        Returns:
            Tuple with command name and its arguments.
        """
        if user_input:
            cmd, *args = user_input.split()
            cmd = cmd.strip().lower()
            return cmd, *args
        else:
            return ('', [])
