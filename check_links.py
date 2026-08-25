import re
import sys

def find_broken_hrefs(html_text):
    """Find <a> tags missing a valid href='...' attribute."""
    all_anchor_tags = re.findall(r"<a\s[^>]*>", html_text)
    broken = [tag for tag in all_anchor_tags if not re.search(r'href="[^"]+"', tag)]
    return broken

if __name__ == "__main__":
    with open("index.html", encoding="utf-8") as f:
        html = f.read()
    broken = find_broken_hrefs(html)
    if broken:
        print("Broken anchor tags found:")
        for tag in broken:
            print(" ", tag)
        sys.exit(1)
    print("All anchor tags OK.")