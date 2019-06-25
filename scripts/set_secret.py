import os
import django
import sys
from os.path import dirname, abspath

sh00t_path = dirname(dirname(abspath(__file__)))
sys.path.append(sh00t_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()


def generate_secret_key():
    secret_file = settings.SECRET_FILE
    try:
        # Ref: https://gist.github.com/ndarville/3452907#file-secret-key-gen-py
        import random
        secret_key = ''.join(
            [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in
             range(50)])
        secret = open(secret_file, 'w')
        secret.write(secret_key)
        secret.close()
        # First installation secret doesn't exists or upgraded so that the secret has changed. Reset user
        from scripts.createsuperuser import reset_user
        reset_user()
    except IOError:
        Exception('Looks like permission issue. Please create a %s file with random characters \
        to generate your secret key!' % secret_file)

    return securet_key


if __name__ == "__main__":
    generate_secret_key()
