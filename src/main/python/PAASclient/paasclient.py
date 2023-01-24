import os
from RESTclient import RESTclient

import logging
logger = logging.getLogger(__name__)

logging.getLogger('urllib3.connectionpool').setLevel(logging.CRITICAL)


class PAASclient(RESTclient):

    def __init__(self, hostname, **kwargs):
        """ class constructor

            Args:
                kwargs (dict): arbritrary number of key word arguments

            Returns:
                PAASclient: instance of PAASclient
        """
        logger.debug('executing PAASclient constructor')

        if 'api_key' not in kwargs:
            raise ValueError('an api_key must be provided to PAASclient')

        super(PAASclient, self).__init__(hostname, **kwargs)

    def get_iap_usage(self, months=None):
        """ return iap usage for number of months

            Args:
                months (str): months of iap usage data to return

            Returns:
                dict: iap usage information
        """
        if not months:
            months = '6'
        logger.debug('getting iap usage for {} months'.format(months))
        return self.get('/v1/usage/iap?months={}'.format(months))

    @classmethod
    def get_PAASclient(cls, hostname=None, api_key=None):
        """ return instance of PAASclient

            Args:
                hostname (str): the host and endpoint for the PAAS REST API
                api_key (str): the PAAS REST API key

            Returns:
                PAASclient: instance of PAASclient
        """
        if not hostname:
            hostname = os.environ.get('PAAS_H')
            if not hostname:
                hostname = 'paasapi.intelcloud.intel.com'

        return PAASclient(
            hostname,
            api_key=api_key if api_key else os.environ.get('PAAS_API_KEY'))
