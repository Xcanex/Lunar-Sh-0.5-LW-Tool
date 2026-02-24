import os
import platform
import subprocess
import shutil

def get_os():
    """Returns the current operating system (Windows, Linux, Termux)"""
    if "com.termux" in os.environ.get("PREFIX", ""):
        return "Termux"
    return platform.system()

def clear_screen():
    """Clears the terminal screen cross-platform"""
    os_name = get_os()
    if os_name == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def is_tool_installed(tool_name):
    """Check if a command-line tool is installed"""
    return shutil.which(tool_name) is not None

def run_command(command, wait=True):
    """Run a shell command cross-platform"""
    try:
        if wait:
            subprocess.run(command, shell=True, check=True)
        else:
            subprocess.Popen(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
