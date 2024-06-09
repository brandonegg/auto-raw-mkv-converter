import typer
from rich import print
from utils.directory import is_mounted_directory

app = typer.Typer()

@app.command()
def scan(directory: str):
    """
    Scan a path for mkv files. Used to test the directory before running a conversion job.
    """
    print("Scanning directory:", directory)

    if is_mounted_directory(directory):
        print("Directory is detected as mounted. To improve file I/O performance, when performing conversions the mkv file will be copied locally during video encoding.")

@app.command()
def convert(directory: str):
    """
    Convert all mkv files in a directory to mp4 and split subtitles.
    """
    pass

if __name__ == "__main__":
    app()
