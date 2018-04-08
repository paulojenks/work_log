

class Error(Exception):
    """ Base class for other exceptions """
    pass

class InputError(Error):
    """ Raised when input doesn't match requirements """
    pass
