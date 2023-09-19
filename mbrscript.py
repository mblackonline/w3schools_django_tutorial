import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cd_tech_backend.settings')
django.setup()

from members.models import Member

member1 = Member(firstname='Tobias', lastname='Refsnes')
member2 = Member(firstname='Linus', lastname='Refsnes')
member3 = Member(firstname='Lene', lastname='Refsnes')
member4 = Member(firstname='Stale', lastname='Refsnes')
member5 = Member(firstname='Jane', lastname='Doe')
members_list = [member1, member2, member3, member4, member5]

for x in members_list:
    x.save()
