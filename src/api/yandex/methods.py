from .requests import (
    make_oauth_request,
    make_disk_request
)


def get_access_token(**kwargs):
    """
    https://yandex.ru/dev/oauth/doc/dg/reference/auto-code-client-docpage/#auto-code-client__get-token

    - see `api/request.py` documentation for more.
    """
    return make_oauth_request("token", kwargs)


def upload_file_with_url(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/upload-ext-docpage

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="POST",
        api_method="resources/upload",
        data=kwargs,
        user_token=user_token
    )


def create_folder(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/create-folder-docpage

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="PUT",
        api_method="resources",
        data=kwargs,
        user_token=user_token
    )


def publish(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/publish-docpage/

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="PUT",
        api_method="resources/publish",
        data=kwargs,
        user_token=user_token
    )


def unpublish(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/publish-docpage/

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="PUT",
        api_method="resources/unpublish",
        data=kwargs,
        user_token=user_token
    )


def get_disk_info(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/capacity-docpage/

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="GET",
        api_method="",
        data=kwargs,
        user_token=user_token
    )


def get_element_info(user_token: str, **kwargs):
    """
    https://yandex.ru/dev/disk/api/reference/meta.html/

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="GET",
        api_method="resources",
        data=kwargs,
        user_token=user_token
    )


def get_element_public_info(user_token: str, **kwargs):
    """
    https://dev.yandex.net/disk-polygon/?lang=ru&tld=ru#!/v147disk47public47resources/GetPublicResource # noqa

    - see `api/request.py` documentation for more.
    """
    return make_disk_request(
        http_method="GET",
        api_method="public/resources",
        data=kwargs,
        user_token=user_token
    )
