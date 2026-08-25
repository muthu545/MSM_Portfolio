from check_external_links import get_external_links, is_well_formed

def test_finds_external_links():
    html = '<a href="https://github.com/muthu545">GitHub</a>'
    assert get_external_links(html) == ["https://github.com/muthu545"]

def test_well_formed_url_passes():
    assert is_well_formed("https://github.com/muthu545") is True

def test_malformed_url_fails():
    assert is_well_formed("https://") is False

def test_all_index_links_are_well_formed():
    with open("index.html", encoding="utf-8") as f:
        html = f.read()
    links = get_external_links(html)
    bad = [url for url in links if not is_well_formed(url)]
    assert bad == [], f"Malformed URLs found: {bad}"