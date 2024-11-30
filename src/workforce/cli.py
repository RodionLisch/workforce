"""Console script for workforce."""
import workforce

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for workforce."""
    console.print("Replace this message by putting your code into "
               "workforce.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    


if __name__ == "__main__":
    app()
