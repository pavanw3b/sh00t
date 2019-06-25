import sys


def generate_secret_key(secret_file):
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


def get_secret_key(secret_file):
    secret_key = " "
    # Do not create secret for migrate
    try:
        if "manage.py" == sys.argv[0]:
            if "migrate" == sys.argv[1]:
                return secret_key
            else:
                try:
                    secret_key = open(secret_file).read().strip()
                except IOError:
                    secret_key = generate_secret_key(secret_file)
                return secret_key
    except IndexError:
        return secret_key