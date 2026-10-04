#!/usr/bin/env python3
"""Generates the static A S Builders site. Edit CONFIG / PROJECTS then run: python3 build.py"""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
CONFIG = dict(
    name="A S Builders",
    tagline="Masonry · Restoration · Waterproofing",
    address="Your Street Address, City, State",
    phone1="+00 00000 00000",
    phone2="+00 00000 00001",
    email="info@asbuilders.homes",
    domain="asbuilders.homes",
    linkedin="#", instagram="#",
)
C = CONFIG

PROJECTS = [
    dict(slug="loft-facade-restoration", title="Loft Façade Restoration", scope="Brick Restoration · Scaffolding · Cleaning",
         cover=19, imgs=[19, 14, 16, 17, 18, 20, 21, 23],
         desc="Full façade restoration of a multi-storey brick loft building, with street-level scaffolding and sidewalk protection throughout the works."),
    dict(slug="corner-building-restoration", title="Corner Building Restoration", scope="Boom Lift Access · Brick Repair · Pointing",
         cover=24, imgs=[24, 22, 25, 26, 27, 30, 31, 32, 33, 34, 35, 36, 37],
         desc="Restoration of a corner mixed-use building using boom-lift access, including day and night shifts to keep the street clear."),
    dict(slug="high-rise-swing-stage", title="High-Rise Swing Stage Works", scope="Swing Stage · Brick Repair · Caulking",
         cover=15, imgs=[15, 9, 11, 12, 13],
         desc="Façade repairs on a high-rise residential tower carried out from suspended swing stages."),
    dict(slug="warehouse-facade", title="Industrial Warehouse Façade", scope="Masonry · Façade Cleaning · Repairs",
         cover=38, imgs=[38, 39, 41],
         desc="Façade maintenance and masonry repair on a large industrial-style warehouse building."),
    dict(slug="stucco-concrete-repair", title="Stucco & Concrete Repair", scope="Patching · Window Surrounds · Sealants",
         cover=3, imgs=[3, 1, 2, 4, 5, 6, 7, 8, 10],
         desc="Test openings, stucco patching and window-surround repairs, masked and sealed to a clean finish."),
    dict(slug="parapet-rooftop-works", title="Parapet & Rooftop Works", scope="Roof Rigging · Parapet · Chimney Repair",
         cover=50, imgs=[50, 28, 29, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 54],
         desc="Rooftop rigging, parapet and chimney restoration, plus swing-stage setup for upper-wall repairs."),
    dict(slug="cooperative-brick-pointing", title="Cooperative Brick Pointing", scope="Pointing · Brick Replacement · Lintels",
         cover=57, imgs=[57, 56, 58, 59, 60, 61],
         desc="Brick replacement, pointing and lintel work across a residential cooperative complex."),
    dict(slug="historic-red-brick", title="Historic Red Brick Restoration", scope="Heritage Masonry · Fire Escapes · Façade",
         cover=68, imgs=[68, 63, 64, 65, 66, 67, 69],
         desc="Careful restoration of a historic red-brick façade, preserving original character while repairing damaged masonry."),
    dict(slug="structural-steel-interior", title="Structural Steel & Interior Works", scope="Steel Beams · Shoring · Structural Repair",
         cover=73, imgs=[73, 70, 71, 72, 74],
         desc="Structural steel reinforcement and interior shoring carried out by our skilled in-house crew."),
]

SERVICES = [
    ("Façade Inspections & Compliance", ["Façade Inspections", "Emergency Repairs", "Safety Equipment Inspections", "Annual Compliance Reports", "Energy-Efficient Window Installation", "Rigging, Scaffolding & Sidewalk Sheds"]),
    ("Masonry Façade", ["Brick Replacement", "Pointing and Caulking", "Lintel & Shelf-Angle Repair", "Façade Cleaning"]),
    ("Metal & Glass Façades", ["Curtain Wall Installation", "Glass Replacement", "Scaffolding Installation", "Sidewalk Shed Installation"]),
    ("Pre-Cast Stone & Concrete", ["Concrete Repairs", "Pre-Cast Stone Installation", "Balcony Restoration", "Concrete Coating", "Railing Replacement"]),
    ("Roofing & Waterproofing", ["Liquid Membrane Waterproofing", "Roof Repair", "Parapet Restoration", "Windows"]),
]

def img(n, w=None):
    return f"images/p{n:02d}.jpg"

def logo(dark=False):
    return f'<span class="logo"><span class="logo-mark">A S</span><span class="logo-text">BUILDERS</span></span>'

def head(title, desc, depth=""):
    return f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#000000">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head><body>'''

def header(active):
    def a(href, label, key):
        return f'<a href="{href}"{" class=active" if active==key else ""}>{label}</a>'
    return f'''<header id="hdr"><div class="bar">
<a href="index.html" class="brand" aria-label="{C['name']} home">{logo()}</a>
<nav class="nav" id="nav">
{a("index.html","Home","home")}{a("index.html#services","Services","services")}{a("index.html#projects","Projects","projects")}{a("about-us.html","About Us","about")}
<a href="contact-us.html" class="btn btn-dark nav-cta">Contact Us</a>
</nav>
<button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>'''

def footer():
    return f'''<section class="cta"><div class="wrap"><h2>Have a project in mind?</h2><a class="btn btn-light" href="contact-us.html">Get in touch</a></div></section>
<footer><div class="wrap fgrid">
<div><a href="index.html" class="brand">{logo()}</a>
<p class="faddr"><strong>{C['name']}</strong><br>{C['address']}</p>
<p><a href="tel:{C['phone1'].replace(' ','')}">{C['phone1']}</a><br><a href="tel:{C['phone2'].replace(' ','')}">{C['phone2']}</a><br><a href="mailto:{C['email']}">{C['email']}</a></p></div>
<nav class="flinks"><a href="index.html#services">Services</a><a href="index.html#projects">Projects</a><a href="about-us.html">About Us</a><a href="contact-us.html">Contact Us</a></nav>
</div><div class="wrap copy">© 2026 {C['name']}. All rights reserved.</div></footer>
<script src="js/main.js"></script></body></html>'''

def card(p):
    return f'''<a class="pcard" href="project-{p['slug']}.html"><img loading="lazy" src="{img(p['cover'])}" alt="{html.escape(p['title'])}">
<div class="pcap"><h3>{html.escape(p['title'].upper())}</h3><p>{html.escape(p['scope'])}</p></div></a>'''

def build_index():
    hero = [38, 57, 15, 69, 50]
    slides = "".join(f'<div class="slide{" on" if i==0 else ""}" style="background-image:url({img(n)})"></div>' for i, n in enumerate(hero))
    svc = "".join(f'<div class="scol"><h3>{html.escape(t)}</h3><ul>{"".join(f"<li>{html.escape(i)}</li>" for i in items)}</ul></div>' for t, items in SERVICES)
    cards = "".join(card(p) for p in PROJECTS)
    s = head(f"{C['name']} | Masonry, Restoration & Waterproofing", f"{C['name']} is a general contractor specializing in building envelope restoration, masonry and waterproofing.")
    s += header("home")
    s += f'''<main>
<section class="hero">{slides}<div class="hero-ov"></div>
<div class="hero-in"><p class="eyebrow">TRUSTED BUILDING ENVELOPE CONTRACTORS</p>
<h1><span>MASONRY</span><i></i><span>RESTORATION</span><i></i><span>WATERPROOFING</span></h1>
<a href="#about" class="btn btn-light">Learn More</a></div>
<div class="dots" id="dots">{"".join(f'<button aria-label="Slide {i+1}"{" class=on" if i==0 else ""}></button>' for i in range(len(hero)))}</div></section>

<section class="welcome" id="about"><div class="wrap narrow center">
<h2>Welcome to {C['name']}</h2>
<p>{C['name']} is a leading general contractor specializing in comprehensive building envelope restoration. With a skilled in-house crew, we deliver exceptional results across a wide range of projects, from small-scale repairs to large-scale renovations.</p>
<p>We combine the personalized attention of a boutique firm with the quality, resources and safety standards you would expect from a major industry player.</p></div></section>

<section class="dark mission"><div class="wrap">
<div class="mrow"><div><h2>Our Mission &amp; Values</h2>
<p>To foster seamless collaboration among all project stakeholders, leveraging collective expertise to restore, preserve and rebuild our community's structures with purpose, integrity and sustainability.</p>
<a class="btn btn-light" href="about-us.html">More About Us</a></div>
<img src="{img(73)}" alt="{C['name']} crew installing structural steel" loading="lazy"></div>
<div class="vals">
<div><h3>Craftsmanship</h3><p>Dedicated to the highest standards in every project, ensuring excellence and durability.</p></div>
<div><h3>Commitment</h3><p>Committed to timely and efficient project completion, catering to each client's unique needs.</p></div>
<div><h3>Integrity</h3><p>Operating with transparency and trust, fostering strong client relationships.</p></div></div></div></section>

<section class="services" id="services"><div class="wrap"><h2 class="center">What We Do</h2><div class="sgrid">{svc}</div></div></section>

<section class="projects" id="projects"><div class="wrap"><h2 class="center">Featured Projects</h2><div class="pgrid">{cards}</div></div></section>
</main>'''
    s += footer()
    open(f"{OUT}/index.html", "w").write(s)

def build_about():
    s = head(f"About Us | {C['name']}", f"About {C['name']}: our story, mission and values.")
    s += header("about")
    s += f'''<main><section class="phero" style="background-image:url({img(38)})"><div class="hero-ov"></div><h1>About Us</h1></section>
<section class="wrap narrow about"><h2>Who We Are</h2>
<p>{C['name']} is a general contractor specializing in building envelope restoration: masonry, façade repair, waterproofing, roofing and structural work. Our crews work on everything from small repairs to full-building restorations.</p>
<p>We pair hands-on supervision with proven safety practices, so every job site stays organised, compliant and on schedule.</p>
<h2>Our Mission</h2>
<p>To foster seamless collaboration among all project stakeholders, leveraging collective expertise to restore, preserve and rebuild our community's structures with purpose, integrity and sustainability.</p></section>
<section class="dark"><div class="wrap"><div class="vals">
<div><h3>Craftsmanship</h3><p>Dedicated to the highest standards in every project, ensuring excellence and durability.</p></div>
<div><h3>Commitment</h3><p>Committed to timely and efficient project completion, catering to each client's unique needs.</p></div>
<div><h3>Integrity</h3><p>Operating with transparency and trust, fostering strong client relationships.</p></div></div></div></section>
<section class="wrap about-img"><img src="{img(74)}" alt="Crew at work" loading="lazy"><img src="{img(44)}" alt="Rooftop rigging" loading="lazy"></section></main>'''
    s += footer()
    open(f"{OUT}/about-us.html", "w").write(s)

def build_contact():
    s = head(f"Contact Us | {C['name']}", f"Contact {C['name']} for a free project consultation.")
    s += header("contact")
    s += f'''<main><section class="phero" style="background-image:url({img(57)})"><div class="hero-ov"></div><h1>Contact Us</h1></section>
<section class="wrap cgrid"><div><h2>Get in touch</h2>
<p>Tell us about your building and what needs fixing. We'll get back to you quickly.</p>
<p><strong>{C['name']}</strong><br>{C['address']}</p>
<p><a href="tel:{C['phone1'].replace(' ','')}">{C['phone1']}</a><br><a href="tel:{C['phone2'].replace(' ','')}">{C['phone2']}</a><br><a href="mailto:{C['email']}">{C['email']}</a></p></div>
<form id="cform" class="cform" novalidate>
<label>Name<input name="name" required></label>
<label>Phone<input name="phone" type="tel"></label>
<label>Email<input name="email" type="email" required></label>
<label>Message<textarea name="msg" rows="5" required></textarea></label>
<button class="btn btn-dark" type="submit">Send Message</button>
<p class="note" id="cnote"></p></form></section></main>'''
    s += footer().replace('<script src="js/main.js">', f'<script>window.CONTACT_EMAIL="{C["email"]}";</script><script src="js/main.js">')
    open(f"{OUT}/contact-us.html", "w").write(s)

def build_projects():
    for i, p in enumerate(PROJECTS):
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        g = "".join(f'<a href="{img(n)}" class="gi" data-i="{k}"><img loading="lazy" src="{img(n)}" alt="{html.escape(p["title"])} photo {k+1}"></a>' for k, n in enumerate(p["imgs"]))
        s = head(f"{p['title']} | {C['name']}", p["desc"])
        s += header("projects")
        s += f'''<main><section class="phero" style="background-image:url({img(p['cover'])})"><div class="hero-ov"></div><div><h1>{html.escape(p['title'])}</h1><p>{html.escape(p['scope'])}</p></div></section>
<section class="wrap narrow center"><p class="lead">{html.escape(p['desc'])}</p></section>
<section class="wrap"><div class="gallery">{g}</div>
<div class="pnav"><a href="index.html#projects">← All Projects</a><a href="project-{nxt['slug']}.html">Next: {html.escape(nxt['title'])} →</a></div></section></main>
<div class="lb" id="lb" hidden><button class="lb-x" aria-label="Close">×</button><button class="lb-p" aria-label="Previous">‹</button><img alt=""><button class="lb-n" aria-label="Next">›</button></div>'''
        s += footer()
        open(f"{OUT}/project-{p['slug']}.html", "w").write(s)

os.makedirs(f"{OUT}/css", exist_ok=True); os.makedirs(f"{OUT}/js", exist_ok=True)
build_index(); build_about(); build_contact(); build_projects()
print("built", 3 + len(PROJECTS), "pages")
