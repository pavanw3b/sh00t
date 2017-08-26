import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from configuration.models import ModuleMaster, CaseMaster


print("This will reset everything in the database and set up as fresh.")
print("Are you wanna do this?")
try:
    answer = raw_input("[No] | Yes?\n") or ""
except NameError:
    answer = input("[No] | Yes?\n") or ""
if "yes" == answer.lower():
    ModuleMaster.objects.all().delete()
    CaseMaster.objects.all().delete()
    j = 0  # The counter in inner loop gets reset for each outer loop
    with open('configuration/data/wahh.json') as wahh_file:
        methodology = json.load(wahh_file)
    for i, method in enumerate(methodology['checklist']['Functionality']):
        module = ModuleMaster(name=method, order=i)
        module.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            descriptions_json = methodology['checklist']['Functionality'][method]['tests'][case]['description']
            descriptions = ""
            for description in descriptions_json:
                descriptions = descriptions + description + '\n\n'
            case = CaseMaster(name=case, description=descriptions, module=module, order=j)
            case.save()
            j += 1
