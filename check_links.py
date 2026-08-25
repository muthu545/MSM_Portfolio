{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from check_links import find_broken_hrefs\
\
def test_valid_href_passes():\
    html = '<a href="https://github.com/muthu545">GitHub</a>'\
    assert find_broken_hrefs(html) == []\
\
def test_broken_href_dash_is_caught():\
    # This is the exact bug you shipped and fixed: href- instead of href=\
    html = '<a href-"https://github.com/muthu545">GitHub</a>'\
    broken = find_broken_hrefs(html)\
    assert len(broken) == 1\
\
def test_index_html_has_no_broken_links():\
    with open("index.html", encoding="utf-8") as f:\
        html = f.read()\
    assert find_broken_hrefs(html) == []}