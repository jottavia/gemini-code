"""
System operation tools.
"""

import os
import subprocess
import tempfile
from .base import BaseTool

class BashTool(BaseTool):
    """Tool to execute bash commands."""
    
    name = "bash"
    description = "Execute a bash command, optionally with sudo. For sudo, ensure non-interactive sudo is configured for the user."
    
    # List of banned commands for security
    BANNED_COMMANDS = [
        'curl', 'wget', 'nc', 'netcat', 'telnet',
        'lynx', 'w3m', 'links', 'ssh',
    ]
    
    def execute(self, command: str, use_sudo: bool = False, timeout: int = 30000):
        """
        Execute a bash command.

        Args:
            command: The command to execute
            use_sudo: If True, prepend 'sudo -n ' to the command.
            timeout: Timeout in milliseconds (optional)
        """
        original_command = command
        executable_command = command

        try:
            # Check for banned commands in the original command
            command_parts = original_command.split()
            for banned_word in self.BANNED_COMMANDS:
                if banned_word in command_parts:
                    return f"Error: The command '{banned_word}' (part of '{original_command}') is not allowed for security reasons."

            if use_sudo:
                executable_command = f"sudo -n {original_command}"

            # Convert timeout to seconds (with better error handling)
            try:
                timeout_sec = int(timeout) / 1000
                if timeout_sec <= 0: # Ensure positive timeout
                    timeout_sec = 30
            except ValueError:
                # If timeout can't be converted to int, use default
                timeout_sec = 30
            
            process = subprocess.Popen(
                executable_command, # Use the potentially modified command
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            
            try:
                stdout, stderr = process.communicate(timeout=timeout_sec)
                
                if use_sudo and process.returncode == 1 and "a password is required" in stderr.lower():
                    return "Error: sudo -n requires a password, or passwordless sudo is not configured for this user. Command not executed."

                if process.returncode != 0:
                    return f"Command exited with status {process.returncode} (executed: '{executable_command}')\n\nSTDOUT:\n{stdout}\n\nSTDERR:\n{stderr}"
                
                return stdout
            
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate() # Get any output
                return f"Error: Command '{executable_command}' timed out after {timeout_sec} seconds.\n\nSTDOUT:\n{stdout}\n\nSTDERR:\n{stderr}"
        
        except Exception as e:
            return f"Error executing command '{executable_command}': {str(e)}"