import sys

from django.core.management.base import BaseCommand, CommandError

from bills.models import Bill
from search import queue

class Command(BaseCommand):
    help = "Load canonical bill data from leginfo.legislature.gov into Bill model."

    def output(self, msg):
        self.stdout.write(self.style.SUCCESS(msg))

    def output_error(self, msg):
        self.stdout.write(self.style.ERROR(msg))

    def handle(self, *args, **options):
        clear_existing = True # make this an arg

        self.output("Fetching latest bill records from state website...")

        if queue.is_available():
            recs = queue.fetch_bills()
        else:
            recs = Bill.objects.fetch()

        if not recs:
            self.output_error("Warning. No bill records were fetched.")
            sys.exit(1)
        else:
            self.output("Done. {} records fetched.".format(len(recs)))

        self.output("Loading bills into app using fetched records...")
        bills = Bill.objects.load(recs, clear_existing=clear_existing)
        if not bills:
            self.output_error("Warning. No new bills were created.")
            sys.exit(1)
        else:
            self.output("Complete! {} new bills created.".format(len(bills)))