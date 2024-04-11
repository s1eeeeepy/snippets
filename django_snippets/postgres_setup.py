# install dependancy

pip install psycopg2 

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'DB_NAME',
        'USER': 'USER_NAME',
        'OPTIONS': {
            'passfile': '.pass_data',
        }
    },
}

# create and use .pass_data file to hide sensitive data

localhost:5432:NAME:USER:PASSWORD



