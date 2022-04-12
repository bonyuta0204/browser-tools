import typer
from .dakoku import FreeeDakoku

app = typer.Typer()


@app.command()
def shukkin(email: str, password: str):
    dakoku = FreeeDakoku(email, password)
    dakoku.login()
    dakoku.shukkin()


@app.command()
def taikin(email: str, password: str):
    dakoku = FreeeDakoku(email, password)
    dakoku.login()
    dakoku.taikin()


if __name__ == "__main__":
    app()
