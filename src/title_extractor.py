def extract_title(markdown):
    for mark in markdown.splitlines():
        if mark.startswith("# "):
            return mark[2:].strip()
    raise Exception("No h1 header found in markdown.")