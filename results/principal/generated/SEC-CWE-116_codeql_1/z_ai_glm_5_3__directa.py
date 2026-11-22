import re


def filterScriptTags(content):
    '''
    Remove <script> tags from the content argument.
    '''
    # Remove well-formed <script ...> ... </script> blocks (case-insensitive,
    # spanning multiple lines), including any content inside them.
    content = re.sub(
        r'<\s*script\b[^>]*>.*?<\s*/\s*script\s*>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Remove self-closing or unclosed opening <script ...> tags.
    content = re.sub(
        r'<\s*script\b[^>]*/?>',
        '',
        content,
        flags=re.IGNORECASE,
    )

    # Remove any stray closing </script> tags.
    content = re.sub(
        r'<\s*/\s*script\s*>',
        '',
        content,
        flags=re.IGNORECASE,
    )

    return content
