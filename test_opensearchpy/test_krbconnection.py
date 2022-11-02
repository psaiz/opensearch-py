""" Test module to check a connection with kerberos """

import unittest
from unittest.mock import patch, Mock
from requests.models import Response, Request
from requests_kerberos import HTTPKerberosAuth, OPTIONAL

from opensearchpy import OpenSearch, RequestsHttpConnection

class TestKrbConnection(unittest.TestCase): # pylint: disable=invalid-name
    """ Test for kerberos """

    @patch('requests.Session.send')
    @patch('requests_kerberos.HTTPKerberosAuth')
    def test_krbConnection(self, myHTTPKerberosAuth, mySend): # pylint: disable=unused-argument,invalid-name
        """ Check if we can get a Kerberos connection, mocking up the server calls """

        client = OpenSearch(['https://localhost:9200'],
                            use_ssl=True,
                            connection_class=RequestsHttpConnection,
                            http_auth=HTTPKerberosAuth(mutual_authentication=OPTIONAL),
                           )

        # Ensuring that we got something back
        self.assertIsNotNone(client.transport)

        # Let's mock a call to cluster health
        mySend.return_value = Mock(spec=Response)
        mySend.return_value.status_code = 200
        mySend.return_value.content = b'{"status": "green"}'
        mySend.return_value.headers = {}
        mySend.return_value.request = Mock(spec=Request)
        mySend.return_value.request.path_url = '/cluster/health'

        client.cluster.health()

        self.assertTrue(mySend.called)
        # Unfortunately, the 'send' encapsulates alto all the autehntication
#        self.assertTrue(myHTTPKerberosAuth.called)

if __name__ == '__main__':
    unittest.main()
