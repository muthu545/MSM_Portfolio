from check_links import find_broken_hrefs

def test_valid_href_passes():
    html = '<a href="https://github.com/muthu545">GitHub</a>'
    assert find_broken_hrefs(html) == []

def test_broken_href_dash_is_caught():
    # This is the exact bug you shipped and fixed: href- instead of href=
    html = '<a href-"https://github.com/muthu545">GitHub</a>'
    broken = find_broken_hrefs(html)
    assert len(broken) == 1

def test_index_html_has_no_broken_links():
    with open("index.html", encoding="utf-8") as f:
        html = f.read()
    assert find_broken_hrefs(html) == []