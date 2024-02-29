"""
registration_app Django application initialization.
"""

from django.apps import AppConfig


class RegistrationAppConfig(AppConfig):
    """
    Configuration for the registration_app Django application.
    """

    name = 'registration_app'
    plugin_app = {
        'url_config': {
            'lms.djangoapp': {
                'namespace': 'registration_app',
                'relative_path': 'urls',
            }
        },
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings'},
            }
        },
    } 