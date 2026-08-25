"""
Requirement: every external link (LinkedIn, GitHub, Google Scholar, mailto)
on the site must open a valid destination — no typos, no dead domains.

Test case: for each href in index.html starting with http(s):// or mailto:,
confirm the URL is well-formed (has a scheme and a domain).
We are NOT checking live reachability here (that would make CI flaky/slow) —
just structural validity. This scope decision is itself worth stating out loud
in an interview: real QA involves deciding what NOT to test, not just what to test.
"""
import re

def get_external_links(html_text):
    hrefs = re.findall(r'href="([^"]+)"', html_text)
    return [h for h in hrefs if h.startswith("http") or h.startswith("mailto:")]

def is_well_formed(url):
    if url.startswith("mailto:"):
        return "@" in url
    return re.match(r"https?://[^\s/]+\.[^\s/]+", url) is not None