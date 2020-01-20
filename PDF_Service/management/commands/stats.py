from django.core.management.base import BaseCommand
from ...models import Document as doc
class Command(BaseCommand):
    help = 'Shows statistics of the documents present in the system'

    def add_arguments(self, parser):
        parser.add_argument('--all','-a',
                            action='store_true',
                            help='Shows all document stats',
                            )

    def handle(self, *args, **options):
        documents = doc.objects.all()
        total = 0
        for document in documents:
            if options['all']:
                print('Id Dokumentu =' + str(document.id) +
                      'Nazwa = ' + str(document.name) +
                      'Rozmiar = ' + str(document.size) +
                      'Liczba stron = ' + str(document.page_number) +
                      'Data Wrzucenia = ' + str(document.date)
                      )
            total += document.size
        self.stdout.write(self.style.SUCCESS('Total documents: ' + str(len(documents)) + ' Total documents size: ' +str(total)))

