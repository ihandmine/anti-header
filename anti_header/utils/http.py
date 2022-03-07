

def headers_dict_to_raw(headers_dict):
    r"""
    Returns a raw HTTP headers representation of headers

    For example:

    >>> import w3lib.http
    >>> w3lib.http.headers_dict_to_raw({b'Content-type': b'text/html', b'Accept': b'gzip'}) # doctest: +SKIP
    'Content-type: text/html\\r\\nAccept: gzip'
    >>>

    Note that keys and values must be bytes.

    Argument is ``None`` (returns ``None``):

    >>> w3lib.http.headers_dict_to_raw(None)
    >>>

    """

    if headers_dict is None:
        return None
    raw_lines = []
    for key, value in headers_dict.items():
        if isinstance(value, bytes):
            raw_lines.append(b": ".join([key, value]))
        elif isinstance(value, (list, tuple)):
            for v in value:
                raw_lines.append(b": ".join([key, v]))
    return b'\r\n'.join(raw_lines)
