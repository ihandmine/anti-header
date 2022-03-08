from __future__ import absolute_import, unicode_literals


class AntiUserAgentError(Exception):
    pass


class HeaderDeprecationWarning(Warning):
    pass


class NotFoundParamError(Exception):
    pass


class UnSupportMethodError(Exception):
    pass


UserAgentError = AntiUserAgentError
