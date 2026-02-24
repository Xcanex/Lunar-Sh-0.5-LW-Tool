import sys
import time
from rich.console import Console

from core import system
from core import ui
from core.tools_db import CATEGORIES

console = Console()

def handle_tool_selection(cat_id):
    category = CATEGORIES[cat_id]
    os_name = system.get_os()

    while True:
        system.clear_screen()
        ui.print_banner(os_name)
        ui.print_tools(category, cat_id)

        choice = ui.get_input()

        if choice.lower() == 'b':
            break

        try:
            tool_idx = int(choice) - 1
            if 0 <= tool_idx < len(category["tools"]):
                tool = category["tools"][tool_idx]
                
                ui.print_info(f"Selected: {tool['name']}")
                console.print(f"1. Run {tool['name']}")
                console.print(f"2. Install {tool['name']}")
                console.print(f"3. Go Back")
                
                action = ui.get_input()

                if action == '1':
                    ui.print_info(f"Starting {tool['name']}...")
                    time.sleep(1)
                    system.run_command(tool['run'])
                    ui.get_input("Press Enter to continue...")

                elif action == '2':
                    ui.print_info(f"Installing {tool['name']} for {os_name}...")
                    install_cmd = tool['install'].get(os_name)
                    
                    if not install_cmd:
                        ui.print_error(f"No installation instructions for {os_name}.")
                    else:
                        time.sleep(1)
                        if system.run_command(install_cmd):
                            ui.print_success("Installation command executed successfully!")
                        else:
                            ui.print_error("Installation failed. Check errors above.")
                    ui.get_input("Press Enter to continue...")
                
                elif action == '3':
                    continue
                else:
                    ui.print_warning("Invalid option. Try again.")
                    time.sleep(1)
            else:
                ui.print_warning("Invalid tool ID.")
                time.sleep(1)
        except ValueError:
            ui.print_warning("Please enter a valid number.")
            time.sleep(1)


def main():
    os_name = system.get_os()

    while True:
        system.clear_screen()
        ui.print_banner(os_name)
        ui.print_menu(CATEGORIES)
        
        choice = ui.get_input()

        if choice.lower() == 'x':
            ui.print_info("Exiting Lunar Toolkit. Goodbye!")
            sys.exit(0)
        
        elif choice.lower() == 'a':
            system.clear_screen()
            ui.print_banner(os_name)
            console.print("[bold cyan]Lunar Toolkit[/bold cyan] is an advanced, beautiful, and cross-platform")
            console.print("penetration testing utility designed as a modern alternative to AllHackingTools.")
            console.print("\nDeveloped with [red]heart[/red] by LunarTool.")
            ui.get_input("Press Enter to go back...")
            
        elif choice.lower() == 'u':
            ui.print_info("Update feature is not implemented in this version yet.")
            time.sleep(1)

        elif choice in CATEGORIES:
            handle_tool_selection(choice)
        
        else:
            ui.print_warning("Invalid selection. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        ui.print_info("Keyboard interrupt detected. Exiting...")
        sys.exit(0)
