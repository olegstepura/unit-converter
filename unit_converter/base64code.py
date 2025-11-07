import base64

def base64_encode(text, _=None):
    """Encode text to Base64 format"""
    if _ is None:
        def _(s): return s
    try:
        # Encode text to bytes, then to base64
        text_bytes = text.encode('utf-8')
        encoded = base64.b64encode(text_bytes).decode('utf-8')
        return encoded, encoded
    except Exception as e:
        error_msg = _("Error encoding to Base64: {}").format(str(e))
        return error_msg, ""

def base64_decode(text, _=None):
    """Decode Base64-encoded text"""
    if _ is None:
        def _(s): return s
    try:
        # Decode base64 to bytes, then to string
        decoded_bytes = base64.b64decode(text)
        decoded = decoded_bytes.decode('utf-8')
        return decoded, decoded
    except Exception as e:
        error_msg = _("Error decoding from Base64: {}").format(str(e))
        return error_msg, ""

