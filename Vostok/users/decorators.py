from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def voluntario_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    """
    Decorator for views that checks that the logged in user is a Voluntario,
    redirects to the log-in page if necessary.
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_voluntario,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def administrador_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    """
    Decorator for views that checks that the logged in user is a Administrador,
    redirects to the log-in page if necessary.
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_administrador,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def adminplus_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/'):
    """
    Decorator for views that checks that the logged in user is a Admin Plus,
    redirects to the log-in page if necessary.
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_adminplus,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator