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


class OutgoingCallerIdList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the OutgoingCallerIdList

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdList
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdList
        """
        super(OutgoingCallerIdList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds.json'.format(**self._solution)

    def stream(self, phone_number=values.unset, friendly_name=values.unset,
               limit=None, page_size=None):
        """
        Streams OutgoingCallerIdInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode phone_number: The phone number of the OutgoingCallerId resources to read
        :param unicode friendly_name: The string that identifies the OutgoingCallerId resources to read
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            phone_number=phone_number,
            friendly_name=friendly_name,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, phone_number=values.unset, friendly_name=values.unset,
             limit=None, page_size=None):
        """
        Lists OutgoingCallerIdInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode phone_number: The phone number of the OutgoingCallerId resources to read
        :param unicode friendly_name: The string that identifies the OutgoingCallerId resources to read
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance]
        """
        return list(self.stream(
            phone_number=phone_number,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, phone_number=values.unset, friendly_name=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately

        :param unicode phone_number: The phone number of the OutgoingCallerId resources to read
        :param unicode friendly_name: The string that identifies the OutgoingCallerId resources to read
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdPage
        """
        params = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return OutgoingCallerIdPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return OutgoingCallerIdPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a OutgoingCallerIdContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        """
        return OutgoingCallerIdContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a OutgoingCallerIdContext

        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        """
        return OutgoingCallerIdContext(self._version, account_sid=self._solution['account_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdList>'


class OutgoingCallerIdPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the OutgoingCallerIdPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The SID of the Account that created the resource

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdPage
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdPage
        """
        super(OutgoingCallerIdPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of OutgoingCallerIdInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        return OutgoingCallerIdInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdPage>'


class OutgoingCallerIdContext(InstanceContext):
    """  """

    def __init__(self, version, account_sid, sid):
        """
        Initialize the OutgoingCallerIdContext

        :param Version version: Version that contains the resource
        :param account_sid: The SID of the Account that created the resource to fetch
        :param sid: The unique string that identifies the resource

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        """
        super(OutgoingCallerIdContext, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'sid': sid, }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json'.format(**self._solution)

    def fetch(self):
        """
        Fetch a OutgoingCallerIdInstance

        :returns: Fetched OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def update(self, friendly_name=values.unset):
        """
        Update the OutgoingCallerIdInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: Updated OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        data = values.of({'FriendlyName': friendly_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return OutgoingCallerIdInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the OutgoingCallerIdInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdContext {}>'.format(context)


class OutgoingCallerIdInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the OutgoingCallerIdInstance

        :returns: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        super(OutgoingCallerIdInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'account_sid': payload['account_sid'],
            'phone_number': payload['phone_number'],
            'uri': payload['uri'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: OutgoingCallerIdContext for this OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdContext
        """
        if self._context is None:
            self._context = OutgoingCallerIdContext(
                self._version,
                account_sid=self._solution['account_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

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
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def phone_number(self):
        """
        :returns: The phone number in E.164 format
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def uri(self):
        """
        :returns: The URI of the resource, relative to `https://api.twilio.com`
        :rtype: unicode
        """
        return self._properties['uri']

    def fetch(self):
        """
        Fetch a OutgoingCallerIdInstance

        :returns: Fetched OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        return self._proxy.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the OutgoingCallerIdInstance

        :param unicode friendly_name: A string to describe the resource

        :returns: Updated OutgoingCallerIdInstance
        :rtype: twilio.rest.api.v2010.account.outgoing_caller_id.OutgoingCallerIdInstance
        """
        return self._proxy.update(friendly_name=friendly_name, )

    def delete(self):
        """
        Deletes the OutgoingCallerIdInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdInstance {}>'.format(context)
