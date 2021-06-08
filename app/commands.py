import click
from flask import Blueprint

bp_commands = Blueprint('commands', __name__, cli_group=None)


@bp_commands.cli.command("watch-today")
@click.argument("stock_name")
def watch_today(stock_name):
    print(f'here is your name: {stock_name}')