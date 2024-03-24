"""
Django settings for SwordPHISH project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY_FILE = os.path.join(BASE_DIR, 'secretkey.txt')

if os.path.exists(SECRET_KEY_FILE):
    with open(SECRET_KEY_FILE) as f:
        SECRET_KEY = f.read().strip()
else:
    SECRET_KEY = 'DUMMY_KEY_FOR_DEVELOPMENT_DO_NOT_USE_IN_PRODUCTION'

ADMINS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', "127.0.0.1", "::1"]
CSRF_TRUSTED_ORIGINS = ['http://' + h for h in ALLOWED_HOSTS] + ['https://' + h for h in ALLOWED_HOSTS]

PROJECT_NAME = "SwordPHISH"

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_generate_secret_key',
    'django_bootstrap5',
    'bootstrap3_datetime',
    'ckeditor',
    'LocalUsers',
    'Main',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'Swordphish.urls'

WSGI_APPLICATION = 'Swordphish.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swordphish',
        'USER': 'swordphish',
        'PASSWORD': 'FIXME',
        'HOST': 'FIXME',
        'PORT': '',
    }

}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': True,
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),
]

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    'locale',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = 'Authent:login'
LOGOUT_URL = 'Authent:logout'

SESSION_SAVE_EVERY_REQUEST = True

# Default settings
BOOTSTRAP5 = {

    # The complete URL to the Bootstrap CSS file.
    # Note that a URL can be either a string
    # ("https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css"),
    # or a dict with keys `url`, `integrity` and `crossorigin` like the default value below.
    "css_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css",
        "integrity": "sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap bundle JavaScript file.
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS theme file (None means no theme).
    "theme_url": None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap5.html).
    'javascript_in_head': True,

    # Wrapper class for non-inline fields.
    # The default value "mb-3" is the spacing as used by Bootstrap 5 example code.
    'wrapper_class': 'mb-3',

    # Wrapper class for inline fields.
    # The default value is empty, as Bootstrap5 example code doesn't use a wrapper class.
    'inline_wrapper_class': '',

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-2',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-4',

    # Field class used for horizontal fields without a label.
    'horizontal_field_offset_class': 'offset-sm-2',

    # Set placeholder attributes to label if no placeholder is provided.
    'set_placeholder': True,

    # Class to indicate required field (better to set this in your Django form).
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form).
    'success_css_class': '',

    # Enable or disable Bootstrap 5 server side validation classes (separate from the indicator classes above).
    'server_side_validation': True,

    # Renderers (only set these if you have studied the source and understand the inner workings).
    'formset_renderers': {
        'default': 'django_bootstrap5.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'django_bootstrap5.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'django_bootstrap5.renderers.FieldRenderer',
    },
}

CKEDITOR_BASEPATH = STATIC_URL + "ckeditor/ckeditor"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'NumberedList', 'BulletedList', 'HorizontalRule'],
            ['Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'], ['base64image', 'Link', 'Unlink'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['RemoveFormat', 'Source', 'DocProps', 'Maximize']
        ],
        'extraPlugins': 'base64image,docprops,font,maximize',
        'width': '100%',
        'fullPage': 'true',
        'removeDialogTabs': 'link:Upload;link:upload;link:advanced;docProps:meta;docProps:preview;',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
    },
    'withforms': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Table', 'NumberedList', 'BulletedList', 'HorizontalRule'],
            ['Outdent', 'Indent'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor'], ['base64image', 'Link', 'Unlink'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['RemoveFormat', 'Source', 'DocProps', 'Maximize'],
            ['Form', 'TextField', 'Button']
        ],
        'extraPlugins': 'base64image,docprops,font,maximize,forms',
        'width': '100%',
        'fullPage': 'true',
        'removeDialogTabs': 'link:Upload;link:upload;link:advanced;docProps:meta;docProps:preview;',
        'filebrowserBrowseUrl': '',
        'filebrowserImageBrowseUrl': '',
        'filebrowserFlashBrowseUrl': '',
    }
}

# Redis configuration used by Celery
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# Mail address used to send mails
SERVER_EMAIL = "SwordPhish <swordphish@invalid.notld>"

# Mail server information
EMAIL_HOST = "localhost"
EMAIL_PORT = 2525
# EMAIL_HOST_USER = "FIXME"
# EMAIL_HOST_PASSWORD = "FIXME"

# Used to alert when a campaign starts
ALERT_RECIPIENTS = ["fixme@invalid.notld"]

# After AUTOLOCK_DELAY days of inactivity account will be blocked
AUTOLOCK_DELAY = 180

# Mail sent when an account is auto locked
AUTOLOCK_TEMPLATE = u"""Hello %s

You have an active account on Swordphish but you never logged in.

As a security measure, your account has been locked. If you need it reply to this email !

Best regards,

Swordphish administrators
"""

# AUTOLOCK_NEVER_USED_DELAY days after creation an account will be locked if not used
AUTOLOCK_NEVER_USED_DELAY = 30

# Mail sent when an account is never used
AUTOLOCK_NEVER_USED_TEMPLATE = u"""Hello %s

You have an active account on Swordphish but haven't used it during the last %s days.

As a security measure, your account has been locked. If you need it reply to this email !

Best regards,

Swordphish administrators
"""

# After AUTOCLEAN_DELAY days the campaigns / targets will be automatically deleted
AUTOCLEAN_DELAY = 90

# The day of the week when the auto delete is performed
AUTOCLEAN_DAY = "saturday"

# Used to filter access to swordphih pages when reaching phishing pages
HOSTING_DOMAIN = "FIXME"

# Phishing mail header
PHISHING_MAIL_HEADER = "X-Swordphish-Awareness-Campaign"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
    },
}
