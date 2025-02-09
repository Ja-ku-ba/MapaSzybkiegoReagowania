SECRET_KEY = 'django-insecure-0tpgicc64n0)v8ddik%jy8_k@eu!df=46kkp0nx=bgx+w(3rtn'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'masteruser',
        'PASSWORD': '12345678',
        'HOST': 'w3-django-project.cdxmgq9zqqlr.us-east-1.rds.amazonaws.com',
        'PORT': '5432'
    }
}

ALLOWED_HOSTS = []
