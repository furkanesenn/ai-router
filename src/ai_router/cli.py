import typer 

from .api import core


app = typer.Typer()

@app.command()
def main():
    """Main entry point for the CLI."""
    print("Hello from ai-router!")
    
@app.command()
def request(prompt: str):
    """Handle a request with the given prompt."""
    response = core.handle_request(prompt)
    print(response)