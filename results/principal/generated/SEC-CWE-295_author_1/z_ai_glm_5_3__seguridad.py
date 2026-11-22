import ssl


def getSSLContext():
    '''
    Create an SSL context and return it.
    '''
    # Client-side context with secure defaults:
    # certificate verification and hostname checking enabled,
    # system CA certificates loaded automatically.
    context = ssl.create_default_context()

    # Enforce TLS 1.2 as the minimum protocol version to avoid
    # deprecated and insecure protocol versions.
    context.minimum_version = ssl.TLSVersion.TLSv1_2

    # Defense in depth: explicitly require certificate verification.
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED

    # Disable TLS compression to mitigate CRIME-style attacks.
    context.options |= ssl.OP_NO_COMPRESSION

    return context
