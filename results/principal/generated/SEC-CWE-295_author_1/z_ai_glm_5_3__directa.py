import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_default_certs()
    return context
