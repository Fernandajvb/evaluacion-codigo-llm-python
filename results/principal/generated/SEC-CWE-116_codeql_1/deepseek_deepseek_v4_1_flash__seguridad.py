import re

def filterScriptTags(content):
    if not isinstance(content, str):
        raise TypeError("content must be a string")
    content = re.sub(r'<script\b[^>]*>.*?</script\s*>', '', content, flags=re.IGNORECASE | re.DOTALL)
    content = re.sub(r'<script\b[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'</script\s*>', '', content, flags=re.IGNORECASE)
    return content
