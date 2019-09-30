# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MobileList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the MobileList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileList
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileList
        """
        super(MobileList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/IncomingPhoneNumbers/Mobile.json'.format(**self._solution)

    def stream(self, beta=values.unset, friendly_name=values.unset,
               phone_number=values.unset, origin=values.unset, limit=None,
               page_size=None):
        """
        Streams MobileInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the resources to read
        :param unicode phone_number: The phone numbers of the resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, origin=values.unset, limit=None,
             page_size=None):
        """
        Lists MobileInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the resources to read
        :param unicode phone_number: The phone numbers of the resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance]
        """
        return list(self.stream(
            beta=beta,
            friendly_name=friendly_name,
            phone_number=phone_number,
            origin=origin,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, beta=values.unset, friendly_name=values.unset,
             phone_number=values.unset, origin=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MobileInstance records from the API.
        Request is executed immediately

        :param bool beta: Whether to include new phone numbers
        :param unicode friendly_name: A string that identifies the resources to read
        :param unicode phone_number: The phone numbers of the resources to read
        :param unicode origin: Include phone numbers based on their origin. By default, phone numbers of all origin are included.
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MobileInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobilePage
        """
        params = values.of({
            'Beta': beta,
            'FriendlyName': friendly_name,
            'PhoneNumber': phone_number,
            'Origin': origin,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return MobilePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MobileInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MobileInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobilePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MobilePage(self._version, response, self._solution)

    def create(self, phone_number, api_version=values.unset,
               friendly_name=values.unset, sms_application_sid=values.unset,
               sms_fallback_method=values.unset, sms_fallback_url=values.unset,
               sms_method=values.unset, sms_url=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               voice_application_sid=values.unset,
               voice_caller_id_lookup=values.unset,
               voice_fallback_method=values.unset, voice_fallback_url=values.unset,
               voice_method=values.unset, voice_url=values.unset,
               identity_sid=values.unset, address_sid=values.unset):
        """
        Create a new MobileInstance

        :param unicode phone_number: The phone number to purchase in E.164 format
        :param unicode api_version: The API version to use for incoming calls made to the new phone number
        :param unicode friendly_name: A string to describe the new phone number
        :param unicode sms_application_sid: The SID of the application to handle SMS messages
        :param unicode sms_fallback_method: HTTP method used with sms_fallback_url
        :param unicode sms_fallback_url: The URL we call when an error occurs while executing TwiML
        :param unicode sms_method: The HTTP method to use with sms url
        :param unicode sms_url: The URL we should call when the new phone number receives an incoming SMS message
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback
        :param unicode voice_application_sid: The SID of the application to handle the new phone number
        :param bool voice_caller_id_lookup: Whether to lookup the caller's name
        :param unicode voice_fallback_method: The HTTP method used with voice_fallback_url
        :param unicode voice_fallback_url: The URL we will call when an error occurs in TwiML
        :param unicode voice_method: The HTTP method used with the voice_url
        :param unicode voice_url: The URL we should call when the phone number receives a call
        :param unicode identity_sid: The SID of the Identity resource to associate with the new phone number
        :param unicode address_sid: The SID of the Address resource associated with the phone number

        :returns: Newly created MobileInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'ApiVersion': api_version,
            'FriendlyName': friendly_name,
            'SmsApplicationSid': sms_application_sid,
            'SmsFallbackMethod': sms_fallback_method,
            'SmsFallbackUrl': sms_fallback_url,
            'SmsMethod': sms_method,
            'SmsUrl': sms_url,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'VoiceApplicationSid': voice_application_sid,
            'VoiceCallerIdLookup': voice_caller_id_lookup,
            'VoiceFallbackMethod': voice_fallback_method,
            'VoiceFallbackUrl': voice_fallback_url,
            'VoiceMethod': voice_method,
            'VoiceUrl': voice_url,
            'IdentitySid': identity_sid,
            'AddressSid': address_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return MobileInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileList>'


class MobilePage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the MobilePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobilePage
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobilePage
        """
        super(MobilePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MobileInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance
        """
        return MobileInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobilePage>'


class MobileInstance(InstanceResource):
    """  """

    class AddressRequirement(object):
        NONE = "none"
        ANY = "any"
        LOCAL = "local"
        FOREIGN = "foreign"

    def __init__(self, version, payload, account_sid):
        """
        Initialize the MobileInstance

        :returns: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance
        :rtype: twilio.rest.api.v2010.account.incoming_phone_number.mobile.MobileInstance
        """
        super(MobileInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'address_sid': payload['address_sid'],
            'address_requirements': payload['address_requirements'],
            'api_version': payload['api_version'],
            'beta': payload['beta'],
            'capabilities': payload['capabilities'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'identity_sid': payload['identity_sid'],
            'phone_number': payload['phone_number'],
            'origin': payload['origin'],
            'sid': payload['sid'],
            'sms_application_sid': payload['sms_application_sid'],
            'sms_fallback_method': payload['sms_fallback_method'],
            'sms_fallback_url': payload['sms_fallback_url'],
            'sms_method': payload['sms_method'],
            'sms_url': payload['sms_url'],
            'status_callback': payload['status_callback'],
            'status_callback_method': payload['status_callback_method'],
            'trunk_sid': payload['trunk_sid'],
            'uri': payload['uri'],
            'voice_application_sid': payload['voice_application_sid'],
            'voice_caller_id_lookup': payload['voice_caller_id_lookup'],
            'voice_fallback_method': payload['voice_fallback_method'],
            'voice_fallback_url': payload['voice_fallback_url'],
            'voice_method': payload['voice_method'],
            'voice_url': payload['voice_url'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, }

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def address_sid(self):
        """
        :returns: The SID of the Address resource associated with the phone number
        :rtype: unicode
        """
        return self._properties['address_sid']

    @property
    def address_requirements(self):
        """
        :returns: Whether the phone number requires an Address registered with Twilio.
        :rtype: MobileInstance.AddressRequirement
        """
        return self._properties['address_requirements']

    @property
    def api_version(self):
        """
        :returns: The API version used to start a new TwiML session
        :rtype: unicode
        """
        return self._properties['api_version']

    @property
    def beta(self):
        """
        :returns: Whether the phone number is new to the Twilio platform
        :rtype: bool
        """
        return self._properties['beta']

    @property
    def capabilities(self):
        """
        :returns: Indicate if a phone can receive calls or messages
        :rtype: unicode
        """
        return self._properties['capabilities']

    @property
    def date_created(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The RFC 2822 date and time in GMT that the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def identity_sid(self):
        """
        :returns: The SID of the Identity resource associated with number
        :rtype: unicode
        """
        return self._properties['identity_sid']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def origin(self):
        """
        :returns: The phone number's origin. Can be twilio or hosted.
        :rtype: unicode
        """
        return self._properties['origin']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def sms_application_sid(self):
        """
        :returns: The SID of the application that handles SMS messages sent to the phone number
        :rtype: unicode
        """
        return self._properties['sms_application_sid']

    @property
    def sms_fallback_method(self):
        """
        :returns: The HTTP method used with sms_fallback_url
        :rtype: unicode
        """
        return self._properties['sms_fallback_method']

    @property
    def sms_fallback_url(self):
        """
        :returns: The URL that we call when an error occurs while retrieving or executing the TwiML
        :rtype: unicode
        """
        return self._properties['sms_fallback_url']

    @property
    def sms_method(self):
        """
        :returns: The HTTP method to use with sms_url
        :rtype: unicode
        """
        return self._properties['sms_method']

    @property
    def sms_url(self):
        """
        :returns: The URL we call when the phone number receives an incoming SMS message
        :rtype: unicode
        """
        return self._properties['sms_url']

    @property
    def status_callback(self):
        """
        :returns: The URL to send status information to your application
        :rtype: unicode
        """
        return self._properties['status_callback']

    @property
    def status_callback_method(self):
        """
        :returns: The HTTP method we use to call status_callback
        :rtype: unicode
        """
        return self._properties['status_callback_method']

    @property
    def trunk_sid(self):
        """
        :returns: The SID of the Trunk that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['trunk_sid']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    @property
    def voice_application_sid(self):
        """
        :returns: The SID of the application that handles calls to the phone number
        :rtype: unicode
        """
        return self._properties['voice_application_sid']

    @property
    def voice_caller_id_lookup(self):
        """
        :returns: Whether to lookup the caller's name
        :rtype: bool
        """
        return self._properties['voice_caller_id_lookup']

    @property
    def voice_fallback_method(self):
        """
        :returns: The HTTP method used with voice_fallback_url
        :rtype: unicode
        """
        return self._properties['voice_fallback_method']

    @property
    def voice_fallback_url(self):
        """
        :returns: The URL we call when an error occurs in TwiML
        :rtype: unicode
        """
        return self._properties['voice_fallback_url']

    @property
    def voice_method(self):
        """
        :returns: The HTTP method used with the voice_url
        :rtype: unicode
        """
        return self._properties['voice_method']

    @property
    def voice_url(self):
        """
        :returns: The URL we call when the phone number receives a call
        :rtype: unicode
        """
        return self._properties['voice_url']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.MobileInstance>'
