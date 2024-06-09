import typer
from rich import print

app = typer.Typer()

@app.command()
def scan(directory: str):
    print("Scanning directory:", directory)

@app.command()
def convert(directory: str):
    pass

if __name__ == "__main__":
    app()
