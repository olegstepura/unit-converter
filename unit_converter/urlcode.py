import urllib.parse

def url_encode(text, _=None):
    """Encode text to URL-encoded format"""
    if _ is None:
        def _(s): return s
    try:
        encoded = urllib.parse.quote(text, safe='')
        return encoded, encoded
    except Exception as e:
        error_msg = _("Error encoding URL: {}").format(str(e))
        return error_msg, ""

def url_decode(text, _=None):
    """Decode URL-encoded text"""
    if _ is None:
        def _(s): return s
    try:
        decoded = urllib.parse.unquote(text, encoding='utf-8', errors='replace')
        return decoded, decoded
    except Exception as e:
        error_msg = _("Error decoding URL: {}").format(str(e))
        return error_msg, ""

