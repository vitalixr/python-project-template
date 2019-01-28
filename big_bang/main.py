import sys
import logging
from pprint import pprint

import click


logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


@click.group()
@click.option('--debug', '-d', is_flag=True, default=False)
@click.pass_context
def cli(ctx, debug):
    if debug:
        logger.setLevel(logging.DEBUG)


@cli.command()
@click.option('--name', help='The name.')
@click.pass_context
def hello(ctx, name):
    click.echo('Hello %s!' % name)


def entry_point():
    cli()


if __name__ == '__main__':
    entry_point()
