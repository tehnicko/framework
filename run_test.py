#!/usr/bin/env python
import click
import os
import time
from subprocess import call
from six.moves.configparser import RawConfigParser

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = ROOT_DIR + "/report"
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.ini')


def get_sections():
    config = RawConfigParser()
    config.read(CONFIG_PATH)
    return config.sections()


CONTEXT_SETTINGS = dict(
    ignore_unknown_options=True,
    help_option_names=['-h', '--help'],
)

drivers = ['chrome', 'firefox', 'headless', 'firefoxHeadless']


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode.')
@click.option('--html', is_flag=True, help='Generate html report.')
@click.option('--env', type=click.Choice(get_sections()), default="tst", help='Select test environment.')
@click.option('--browser', '-b', type=click.Choice(drivers), default="chrome", help='Select browser.')
@click.argument('file', type=click.Path(exists=True))
@click.argument('pytest_args', nargs=-1, type=click.UNPROCESSED)
def run_command(verbose, html, env, file, browser, pytest_args):

    """
    A wrapper for py.test.

    For [PYTEST_ARGS] list run:
        py.test --help
    """
    os.environ["TEST_ENV"] = env
    os.environ["BROWSER_ENV"] = browser

    cmdline = ['py.test']

    cmdline = cmdline + list(pytest_args)

    if html:
        if not os.path.exists(REPORT_DIR):
            os.makedirs(REPORT_DIR)
        timestamp = time.strftime('%d-%m-%Y_%H-%M-%S')
        test_name = os.path.splitext(file)[0]
        html_file = "%s/%s_%s.html" % (REPORT_DIR, test_name, timestamp)
        cmdline.append('--html=' + html_file)

    cmdline.append(file)

    if verbose:
        click.echo('Invoking: %s' % ' '.join(cmdline))
    call(cmdline)


if __name__ == '__main__':
    run_command()
