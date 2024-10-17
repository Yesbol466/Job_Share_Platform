import pandas as pd
from django.core.management.base import BaseCommand
from skills.models import Job

class Command(BaseCommand):
    help = 'Import Google job data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        try:
            # Read the CSV file using pandas
            data = pd.read_csv(csv_file)

            # Iterate over the CSV rows and create Job objects
            for index, row in data.iterrows():
                job, created = Job.objects.get_or_create(
                    company=row['Company'],
                    title=row['Title'],
                    category=row['Category'],
                    location=row['Location'],
                    responsibility=row['Responsibilities'],
                    minimum_qualifications=row['Minimum Qualifications'],
                    preferred_qualifications=row['Preferred Qualifications']
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Successfully added: {job.title} at {job.company}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Job already exists: {job.title} at {job.company}"))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV file not found'))
        except pd.errors.EmptyDataError:
            self.stdout.write(self.style.ERROR('CSV file is empty'))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f"Missing column in CSV: {e}"))
