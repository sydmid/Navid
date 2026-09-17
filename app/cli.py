import typer

app = typer.Typer()

@app.command()
def watch_today(stock_name: str):
    """
    Watch the daily data for a specific stock.
    """
    print(f'here is your name: {stock_name}')

if __name__ == "__main__":
    app()
