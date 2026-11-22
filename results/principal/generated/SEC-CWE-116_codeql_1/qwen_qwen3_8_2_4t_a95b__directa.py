import re

def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    return re.sub(
        r'<script\b[^>]*>.*?</script\s*>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
