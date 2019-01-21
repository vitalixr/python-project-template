import sys

import click


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', help='The name.')
def hello(name):
    click.echo('Hello %s!' % name)


def entry_point():
    cli()


if __name__ == '__main__':
    entry_point()
