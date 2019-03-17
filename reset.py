import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from configuration.models import MethodologyMaster, ModuleMaster, CaseMaster
from app.models import Project

print("This will reset everything in the database and set up as fresh.")
print("Are you wanna do this?")
answer = input("[No] | Yes?\n") or ""
if "yes" == answer.lower():
    order = ""
    description_consolidated = ""

    Project.objects.all().delete()  # Deleting Project will trigger to delete everything: Flags, Sh0ts, Assessments
    CaseMaster.objects.all().delete()
    ModuleMaster.objects.all().delete()
    MethodologyMaster.objects.all().delete()

    # WAHH
    methodology_master = MethodologyMaster(name="WAHH")
    methodology_master.save()
    wahh_file = open('configuration/data/wahh.json',  'rt', encoding='latin1')
    methodology = json.load(wahh_file)

    for method in methodology['checklist']['Functionality']:
        module_master = ModuleMaster(name=method, methodology=methodology_master, order=methodology['checklist']['Functionality'][method]['order'])
        module_master.save()
        for case in methodology['checklist']['Functionality'][method]['tests']:
            order = '1' + str(methodology['checklist']['Functionality'][method]['order']) + str(methodology['checklist']['Functionality'][method]['tests'][case]['order'])
            descriptions_json = methodology['checklist']['Functionality'][method]['tests'][case]['description']
            description_consolidated = ""
            for description in descriptions_json:
                description_consolidated = description_consolidated + description + '\n\n'
            case = CaseMaster(name=case, description=description_consolidated, module=module_master, order=order)
            case.save()

    # OWASP Testing Guide v4
    methodology_master = MethodologyMaster(name="OWASP Testing Guide V4")
    methodology_master.save()
    owasp_file = open('configuration/data/owasp_testing_guide_v4.json', 'r')
    methodology = json.load(owasp_file)
    for method in methodology['modules']:
        module_master = ModuleMaster(name=method, methodology=methodology_master, order=methodology['modules'][method]['order'])
        module_master.save()
        for case in methodology['modules'][method]['tests']:
            order = '2' + str(methodology['modules'][method]['order']) + str(methodology['modules'][method]['tests'][case]['order'])
            steps = methodology['modules'][method]['tests'][case]['steps']
            steps_consolidated = ""
            for step in steps:
                steps_consolidated = steps_consolidated + step + '\n\n'
            case = CaseMaster(name=case, description=steps_consolidated, module=module_master, order=order)
            case.save()
