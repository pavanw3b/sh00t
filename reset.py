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
    order = ""
    description_consolidated = ""
    ModuleMaster.objects.all().delete()
    CaseMaster.objects.all().delete()
    wahh_file = open('configuration/data/wahh.json', 'r')
    methodology = json.load(wahh_file)
    for method in methodology['checklist']['Functionality']:
        module = ModuleMaster(name=method, order=methodology['checklist']['Functionality'][method]['order'])
        module.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            order = methodology['checklist']['Functionality'][method]['tests'][case]['order']
            descriptions_json = methodology['checklist']['Functionality'][method]['tests'][case]['description']
            description_consolidated = ""
            for description in descriptions_json:
                description_consolidated = description_consolidated + description + '\n\n'
            case = CaseMaster(name=case, description=description_consolidated, module=module, order=order)
            case.save()
