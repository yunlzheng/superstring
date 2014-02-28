#!/usr/bin/env python
#*-*coding:utf-8*-*

from cinderclient.v1.client import Client as CinderClient
from cinderclient import client
from cinderclient import exceptions

from superstring.common.clients.token_cache_storage import CINDER_TOKEN_CACHE


try:
    from eventlet import sleep
except ImportError:
    from time import sleep

import requests


class CinderHTTPClient(client.HTTPClient):

    def __init__(self, *args, **kwargs):
        super(CinderHTTPClient, self).__init__(*args, **kwargs)

        # >> CACHING TOKEN <<
        self._token_cache_key = (self.user, self.password, self.projectid, self.auth_url)
        if not self.management_url or not self.auth_token:
            self.management_url, self.auth_token = CINDER_TOKEN_CACHE.get(
                self._token_cache_key, (None, None)
            )

    def authenticate(self):
        # >> CACHING TOKEN <<
        super(CinderHTTPClient, self).authenticate()
        CINDER_TOKEN_CACHE[self._token_cache_key] = (self.management_url, self.auth_token)

    def _cs_request(self, url, method, **kwargs):
        auth_attempts = 0
        attempts = 0
        backoff = 1
        while True:
            attempts += 1
            if not self.management_url or not self.auth_token:
                self.authenticate()

            kwargs.setdefault('headers', {})['X-Auth-Token'] = self.auth_token

            if self.projectid:
                kwargs['headers']['X-Auth-Project-Id'] = self.projectid
            try:
                resp, body = self.request(self.management_url + url, method,
                                          **kwargs)
                return resp, body
            except exceptions.Unauthorized:
                self.authenticate()
                if attempts > self.retries:
                    self._logger.debug("Authorized failed", exc_info=True)
                    raise
            except exceptions.BadRequest:
                if attempts > self.retries:
                    raise
            except exceptions.Unauthorized:
                if auth_attempts > 0:
                    raise
                self._logger.debug("Unauthorized, reauthenticating.")
                self.management_url = self.auth_token = None
                # First reauth. Discount this attempt.
                attempts -= 1
                auth_attempts += 1
                continue
            except exceptions.ClientException as e:
                if attempts > self.retries:
                    raise
                if 500 <= e.code <= 599:
                    pass
                else:
                    raise
            except requests.exceptions.ConnectionError as e:
                # Catch a connection refused from requests.request
                self._logger.debug("Connection refused: %s" % e)
                raise
            self._logger.debug(
                "Failed attempt(%s of %s), retrying in %s seconds" %
                (attempts, self.retries, backoff))
            sleep(backoff)
            backoff *= 2


class Client(CinderClient):

    def __init__(self, username, api_key, project_id=None, auth_url='',
                 insecure=False, timeout=None, tenant_id=None,
                 proxy_tenant_id=None, proxy_token=None, region_name=None,
                 endpoint_type='publicURL', extensions=None,
                 service_type='volume', service_name=None,
                 volume_service_name=None, retries=3,
                 http_log_debug=False,
                 cacert=None):
        password = api_key
        super(Client, self).__init__(username, password, project_id=None, auth_url='',
                                     insecure=False, timeout=None, tenant_id=None,
                                     proxy_tenant_id=None, proxy_token=None, region_name=None,
                                     endpoint_type='publicURL', extensions=None,
                                     service_type='volume', service_name=None,
                                     volume_service_name=None, retries=None,
                                     http_log_debug=False,
                                     cacert=None)
        self.client = CinderHTTPClient(
            username,
            password,
            project_id,
            auth_url,
            insecure=insecure,
            timeout=timeout,
            tenant_id=tenant_id,
            proxy_token=proxy_token,
            proxy_tenant_id=proxy_tenant_id,
            region_name=region_name,
            endpoint_type=endpoint_type,
            service_type=service_type,
            service_name=service_name,
            volume_service_name=volume_service_name,
            retries=retries,
            http_log_debug=http_log_debug,
            cacert=cacert)


def request_client(username, password, tenant_name, auth_url, timeout=30):
    return Client(username, password, tenant_name, auth_url, timeout=timeout)


if __name__ == "__main__":
    cl = request_client('admin', 'admin', 'admin', 'http://192.168.0.55:5000/v2.0', 15)
    print cl.volumes.list()
