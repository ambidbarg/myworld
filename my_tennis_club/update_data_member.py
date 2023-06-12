import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_tennis_club.settings")

import django
django.setup()

from members.models import Member
x = Member.objects.all()[0]
x.phone = 5551234
x.joined_date = '2022-01-05'
x.save()
print(Member.objects.all().values())
