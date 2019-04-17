import click

from . import config
from . import scraper
from . import sms
from . import alerts
import requests


@click.command()
@click.option('-f', '--from_', default=None)
@click.option('-t', '--to', default=None)
@click.option('-th', '--threshold', default=None)
@click.option('-s', '--send-alerts', is_flag=True, default=False)
def cli(from_, to, threshold, send_alerts):
    from_ = from_ or config.from_
    to = to or config.to
    threshold = threshold or config.threshold
    
    url = config.URL(from_, to)
    result = scraper.Result(url)
    print(result)
    if send_alerts:
        alert = alerts.create_message(result, threshold)
        sms.send_text_message(alert)
