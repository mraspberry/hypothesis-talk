import click

from hypothesis_talk import adder


@click.command
@click.argument("nums", type=int, nargs=-1)
def main(nums):
    """Add NUMS together"""
    click.echo(adder.add_nums(*nums))


if __name__ == "__main__":
    main()
