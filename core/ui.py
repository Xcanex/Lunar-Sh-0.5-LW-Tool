from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import box
from rich.align import Align
from rich.prompt import Prompt

console = Console()

LOGOS = [
    """
[cyan]
 __       __    __  .__   __.      ___      .______      
|  |     |  |  |  | |  \ |  |     /   \     |   _  \     
|  |     |  |  |  | |   \|  |    /  ^  \    |  |_)  |    
|  |     |  |  |  | |  . `  |   /  /_\  \   |      /     
|  `----.|  `--'  | |  |\   |  /  _____  \  |  |\  \----.
|_______| \______/  |__| \__| /__/     \__\ | _| `._____|
                                                       
[/cyan]
""",
]

def print_banner(os_name):
    """Prints the gorgeous Lunar banner"""
    console.print(LOGOS[0])
    
    desc_text = Text()
    desc_text.append(" Lunar Toolkit ", style="bold white on blue")
    desc_text.append(f" | System: {os_name} ", style="bold black on white")
    desc_text.append(f" | Dev: LunarTool ", style="bold black on cyan")
    
    console.print(Align.center(desc_text))
    console.print()

def print_menu(categories):
    """Prints the main menu of categories"""
    table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan", expand=True)
    table.add_column("ID", justify="center", style="bold green", width=5)
    table.add_column("Category Name", style="bold white")
    table.add_column("Description", style="italic dim")

    for cat_id, cat_info in categories.items():
        table.add_row(cat_id, cat_info["name"], cat_info["description"])

    table.add_row("u", "[bold yellow]Update Lunar", "Pull the latest changes from git")
    table.add_row("a", "[bold magenta]About", "Information about Lunar Toolkit")
    table.add_row("x", "[bold red]Exit", "Close the toolkit")

    console.print(table)

def print_tools(category_info, cat_id):
    """Prints the tools in a specific category"""
    console.print(f"\n[bold green]-- {category_info['name']} --[/bold green]")
    
    table = Table(box=box.SIMPLE, show_header=True, header_style="bold magenta")
    table.add_column("ID", justify="center", style="bold yellow")
    table.add_column("Tool Name", style="bold white")
    table.add_column("Description", style="dim")

    for idx, tool in enumerate(category_info['tools']):
        table.add_row(str(idx + 1), tool['name'], tool['desc'])
    
    table.add_row("b", "Back", "Go back to main menu")

    console.print(table)

def get_input(prompt_text="Lunar"):
    """Gets input with a nice styled prompt"""
    return Prompt.ask(f"[bold cyan]┌──([bold green]lunar[bold cyan])-[[bold white]~[bold cyan]]\n[bold cyan]└─$[/bold cyan]")

def print_success(msg):
    console.print(f"[bold green][+][/bold green] {msg}")

def print_error(msg):
    console.print(f"[bold red][-][/bold red] {msg}")

def print_info(msg):
    console.print(f"[bold blue][*][/bold blue] {msg}")

def print_warning(msg):
    console.print(f"[bold yellow][!][/bold yellow] {msg}")
