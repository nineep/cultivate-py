import sys
import six
import logging
from winterfell.i18n import _, _LE
from pecan import conf as CONF

LOG = logging.getLogger(__Name__)


class WinterfellException(Exception):
    '''Base Winterfell Exception

    To correctly use this class, inherit from it and define
    a 'msg_fmt' property. that msg_fmt will get printf.d
    with the keyword arguments provided to the constructor.
    '''

    msg_fmt = _("An unknown exception occurred.")
    code = 500
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass

        if not message:
            try:
                message = self.msg_fmt % kwargs

            except Exception:
                exc_info = sys.exc_info()
                LOG.exception(_LE('Exception in string format operation'))
                for name, value in six.iteritems(kwargs):
                    LOG.error("%s: %s" % (name, value))

                if CONF.fatal_exception_format_errors:
                    six.reraise(*exc_info)
                else:
                    message = self.msg_fmt

        self.message = message
        super(WinterfellException, self).__init__(message)


class UserUsExist(WinterfellException):
    msg_fmt = _("User %(username)s is exist")
    code = 400


class CreateUserFail(WinterfellException):
    code = 400
    msg_fmt = _("create user %(username)s failed, failed step is %(step)s")


class DeleteUserFail(WinterfellException):
    code = 400
    msg_fmt = _("Delete user %(username)s failed, failed step is %(step)s")


class UpdateUserFail(WinterfellException):
    code = 400
    msg_fmt = _("update user %(name)s failed")


