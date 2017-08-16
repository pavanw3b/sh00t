import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()
from app.models import Module, Case

print("This will reset everything in the database and set up as fresh.")
print("Are you wanna do this?")
try:
    answer = raw_input("[No] | Yes?\n") or "no"
except NameError:
    answer = input("[No] | Yes?\n") or "no"
if "yes" == answer.lower():
    Module.objects.all().delete()
    Case.objects.all().delete()

    with open('config/wahh.json') as wahh_file:
        methodology = json.load(wahh_file)
    for method in methodology['checklist']['Functionality']:
        module = Module(name=method)
        module.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            case = Case(name=case, module=module)
            case.save()




