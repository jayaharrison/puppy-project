# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.version import Version
from twilio.rest.trunking.v1.trunk import TrunkList


class V1(Version):

    def __init__(self, domain):
        """
        Initialize the V1 version of Trunking

        :returns: V1 version of Trunking
        :rtype: twilio.rest.trunking.v1.V1.V1
        """
        super(V1, self).__init__(domain)
        self.version = 'v1'
        self._trunks = None

    @property
    def trunks(self):
        """
        :rtype: twilio.rest.trunking.v1.trunk.TrunkList
        """
        if self._trunks is None:
            self._trunks = TrunkList(self)
        return self._trunks

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Trunking.V1>'