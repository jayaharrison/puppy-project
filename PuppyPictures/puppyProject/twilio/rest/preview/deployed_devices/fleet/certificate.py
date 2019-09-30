# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CertificateList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid):
        """
        Initialize the CertificateList

        :param Version version: Version that contains the resource
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateList
        """
        super(CertificateList, self).__init__(version)

        # Path Solution
        self._solution = {'fleet_sid': fleet_sid, }
        self._uri = '/Fleets/{fleet_sid}/Certificates'.format(**self._solution)

    def create(self, certificate_data, friendly_name=values.unset,
               device_sid=values.unset):
        """
        Create a new CertificateInstance

        :param unicode certificate_data: The public certificate data.
        :param unicode friendly_name: The human readable description for this Certificate.
        :param unicode device_sid: The unique identifier of a Device to be authenticated.

        :returns: Newly created CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        data = values.of({
            'CertificateData': certificate_data,
            'FriendlyName': friendly_name,
            'DeviceSid': device_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CertificateInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'], )

    def stream(self, device_sid=values.unset, limit=None, page_size=None):
        """
        Streams CertificateInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode device_sid: Find all Certificates authenticating specified Device.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(device_sid=device_sid, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, device_sid=values.unset, limit=None, page_size=None):
        """
        Lists CertificateInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode device_sid: Find all Certificates authenticating specified Device.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance]
        """
        return list(self.stream(device_sid=device_sid, limit=limit, page_size=page_size, ))

    def page(self, device_sid=values.unset, page_token=values.unset,
             page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of CertificateInstance records from the API.
        Request is executed immediately

        :param unicode device_sid: Find all Certificates authenticating specified Device.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        params = values.of({
            'DeviceSid': device_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CertificatePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CertificateInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CertificatePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CertificateContext

        :param sid: A string that uniquely identifies the Certificate.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        return CertificateContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CertificateContext

        :param sid: A string that uniquely identifies the Certificate.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        return CertificateContext(self._version, fleet_sid=self._solution['fleet_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.CertificateList>'


class CertificatePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CertificatePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificatePage
        """
        super(CertificatePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CertificateInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return CertificateInstance(self._version, payload, fleet_sid=self._solution['fleet_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.CertificatePage>'


class CertificateContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid, sid):
        """
        Initialize the CertificateContext

        :param Version version: Version that contains the resource
        :param fleet_sid: The fleet_sid
        :param sid: A string that uniquely identifies the Certificate.

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        super(CertificateContext, self).__init__(version)

        # Path Solution
        self._solution = {'fleet_sid': fleet_sid, 'sid': sid, }
        self._uri = '/Fleets/{fleet_sid}/Certificates/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CertificateInstance

        :returns: Fetched CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the CertificateInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, device_sid=values.unset):
        """
        Update the CertificateInstance

        :param unicode friendly_name: The human readable description for this Certificate.
        :param unicode device_sid: The unique identifier of a Device to be authenticated.

        :returns: Updated CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'DeviceSid': device_sid, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return CertificateInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.CertificateContext {}>'.format(context)


class CertificateInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, fleet_sid, sid=None):
        """
        Initialize the CertificateInstance

        :returns: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        super(CertificateInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'url': payload['url'],
            'friendly_name': payload['friendly_name'],
            'fleet_sid': payload['fleet_sid'],
            'account_sid': payload['account_sid'],
            'device_sid': payload['device_sid'],
            'thumbprint': payload['thumbprint'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {'fleet_sid': fleet_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CertificateContext for this CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateContext
        """
        if self._context is None:
            self._context = CertificateContext(
                self._version,
                fleet_sid=self._solution['fleet_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Certificate.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: URL of this Certificate.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description for this Certificate.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def fleet_sid(self):
        """
        :returns: The unique identifier of the Fleet.
        :rtype: unicode
        """
        return self._properties['fleet_sid']

    @property
    def account_sid(self):
        """
        :returns: The unique SID that identifies this Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def device_sid(self):
        """
        :returns: The unique identifier of a mapped Device.
        :rtype: unicode
        """
        return self._properties['device_sid']

    @property
    def thumbprint(self):
        """
        :returns: A Certificate unique payload hash.
        :rtype: unicode
        """
        return self._properties['thumbprint']

    @property
    def date_created(self):
        """
        :returns: The date this Certificate was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Certificate was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    def fetch(self):
        """
        Fetch a CertificateInstance

        :returns: Fetched CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CertificateInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, device_sid=values.unset):
        """
        Update the CertificateInstance

        :param unicode friendly_name: The human readable description for this Certificate.
        :param unicode device_sid: The unique identifier of a Device to be authenticated.

        :returns: Updated CertificateInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.certificate.CertificateInstance
        """
        return self._proxy.update(friendly_name=friendly_name, device_sid=device_sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.CertificateInstance {}>'.format(context)
