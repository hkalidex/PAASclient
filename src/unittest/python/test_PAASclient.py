
import unittest
from mock import patch
# from mock import mock_open
from mock import call
from mock import Mock
from PAASclient import PAASclient

import sys
import logging
logger = logging.getLogger(__name__)

consoleHandler = logging.StreamHandler(sys.stdout)
logFormatter = logging.Formatter(
    "%(asctime)s %(threadName)s %(name)s [%(funcName)s] %(levelname)s %(message)s")
consoleHandler.setFormatter(logFormatter)
rootLogger = logging.getLogger()
rootLogger.addHandler(consoleHandler)
rootLogger.setLevel(logging.DEBUG)


class TestPAASclient(unittest.TestCase):

    def setUp(self):

        pass

    def tearDown(self):

        pass

    def test__init_Should_RaiseValueError_When_ApiKeyNotSpecified(self, *patches):
        with self.assertRaises(ValueError):
            PAASclient('api-hostname')

    @patch('PAASclient.paasclient.os.environ.get', return_value='value')
    @patch('PAASclient.paasclient.PAASclient')
    def test__get_PAASclient_Should_GetHostnameFromEnviron_When_HostnameNotSpecified(self, paasclient_patch, *patches):
        paasclient_call = call('value', api_key='some-api-key')
        PAASclient.get_PAASclient(api_key='some-api-key')
        self.assertTrue(paasclient_call in paasclient_patch.mock_calls)

    @patch('PAASclient.paasclient.os.environ.get', return_value=None)
    @patch('PAASclient.paasclient.PAASclient')
    def test__get_PAASclient_Should_GetSetHostnameDefault_When_HostnameNotSpecifiedHostnameNotInEnvironment(self, paasclient_patch, *patches):
        paasclient_call = call('paasapi.intelcloud.intel.com', api_key='some-api-key')
        PAASclient.get_PAASclient(api_key='some-api-key')
        self.assertTrue(paasclient_call in paasclient_patch.mock_calls)

    @patch('PAASclient.paasclient.os.environ.get', return_value='value')
    @patch('PAASclient.paasclient.PAASclient')
    def test__get_PAASclient_Should_GetApiKeyFromEnviron_When_ApiKeyNotSpecified(self, paasclient_patch, *patches):
        paasclient_call = call('api-hostname', api_key='value')
        PAASclient.get_PAASclient(hostname='api-hostname')
        self.assertTrue(paasclient_call in paasclient_patch.mock_calls)

    @patch('PAASclient.PAASclient.get')
    def test__get_iap_usage_Should_SetDefaultMonths_When_MonthsNotSpecified(self, get_patch, *patches):
        client = PAASclient('api-hostname', api_key='some-api-key')
        client.get_iap_usage()
        self.assertTrue(call('/v1/usage/iap?months=6') in get_patch.mock_calls)

    @patch('PAASclient.PAASclient.get')
    def test__get_iap_usage_Should_CallExpected_When_MonthsSpecified(self, get_patch, *patches):
        client = PAASclient('api-hostname', api_key='some-api-key')
        client.get_iap_usage(months=1)
        self.assertTrue(call('/v1/usage/iap?months=1') in get_patch.mock_calls)

    @patch('PAASclient.PAASclient.get')
    def test__get_iap_usage_Should_ReturnExpected_When_Called(self, get_patch, *patches):
        client = PAASclient('api-hostname', api_key='some-api-key')
        result = client.get_iap_usage()
        self.assertEqual(result, get_patch.return_value)
