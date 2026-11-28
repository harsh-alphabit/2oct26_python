from django.core.management.base import BaseCommand
from django.db.models import Count, Max, Q

from stdata.models import user_signup


class Command(BaseCommand):
    help = 'Show common ORM queries using the saved student records (read only).'

    def handle(self, *args, **options):
        # QuerySets can be filtered and sorted before we ask for their results.
        all_students = user_signup.objects.all()
        self.stdout.write('all(): ' + str(list(all_students.values_list('name', flat=True))))

        # filter() keeps matching rows. __icontains means contains, ignoring case.
        matching = user_signup.objects.filter(name__icontains='a')
        self.stdout.write("filter(name__icontains='a'): " + str(list(matching.values_list('name', flat=True))))

        # exclude() leaves out matching rows.
        others = user_signup.objects.exclude(name__icontains='a')
        self.stdout.write('exclude(): ' + str(list(others.values_list('name', flat=True))))

        # order_by() sorts rows; -id gives newest records first.
        newest = user_signup.objects.order_by('-id')
        self.stdout.write('order_by(-id): ' + str(list(newest.values_list('name', flat=True))))

        # first() and last() return one object or None.
        first = user_signup.objects.order_by('id').first()
        last = user_signup.objects.order_by('id').last()
        self.stdout.write('first(): ' + (first.name if first else 'None'))
        self.stdout.write('last(): ' + (last.name if last else 'None'))

        # get() expects exactly one row; use an ID we know exists.
        if first:
            one = user_signup.objects.get(id=first.id)
            self.stdout.write('get(id=' + str(first.id) + '): ' + one.name)

        # count() returns a number; exists() returns True or False.
        self.stdout.write('count(): ' + str(user_signup.objects.count()))
        self.stdout.write('exists(): ' + str(user_signup.objects.exists()))

        # values() returns dictionaries. values_list() returns field values.
        self.stdout.write('values(): ' + str(list(user_signup.objects.values('id', 'name'))))
        self.stdout.write('values_list(): ' + str(list(user_signup.objects.values_list('name', flat=True))))

        # distinct() removes repeated address values.
        addresses = user_signup.objects.order_by().values_list('address', flat=True).distinct()
        self.stdout.write('distinct addresses: ' + str(list(addresses)))

        # __gt means greater than. Q lets us say OR between two conditions.
        higher_ids = user_signup.objects.filter(id__gt=1)
        self.stdout.write('filter(id__gt=1): ' + str(list(higher_ids.values_list('name', flat=True))))
        either = user_signup.objects.filter(Q(name__icontains='a') | Q(address__icontains='city'))
        self.stdout.write('Q(... OR ...): ' + str(list(either.values_list('name', flat=True))))

        # aggregate() calculates one summary for the whole table.
        summary = user_signup.objects.aggregate(total=Count('id'), highest_id=Max('id'))
        self.stdout.write('aggregate(): ' + str(summary))

        # values() + annotate() makes one count for each address.
        by_address = user_signup.objects.values('address').annotate(total=Count('id')).order_by('address')
        self.stdout.write('annotate() by address: ' + str(list(by_address)))

        # [:2] asks the database for only the first two rows of this ordering.
        two_newest = user_signup.objects.order_by('-id')[:2]
        self.stdout.write('first two newest: ' + str(list(two_newest.values_list('name', flat=True))))
