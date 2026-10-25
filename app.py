from flask import Flask, render_template_string
import os

app = Flask(__name__)
ROOT = os.path.dirname(os.path.abspath(__file__))

PAGE = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alpana Jewellery | Handmade with Love</title>
<meta name="description" content="Discover handcrafted jewellery made with love at Alpana Jewellery.">
<style>
:root{--bg:#080b09;--panel:#101713;--gold:#d9b36b;--cream:#fff3d7;--green:#173b2b;--muted:#c4bda9}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--cream);font-family:Georgia,'Times New Roman',serif}
a{color:inherit;text-decoration:none}.topbar{display:flex;align-items:center;justify-content:space-between;gap:24px;padding:14px clamp(18px,5vw,72px);border-bottom:1px solid #c49a4a55;background:#080b09ee;position:sticky;top:0;z-index:10;backdrop-filter:blur(12px)}
.brand{display:flex;align-items:center;gap:14px;min-width:0}.brand img{width:64px;height:64px;object-fit:contain;border-radius:50%}.brandname{font-size:clamp(18px,2.2vw,27px);color:var(--gold);letter-spacing:1px}.tagline{font:10px Arial,sans-serif;letter-spacing:3px;color:var(--muted);margin-top:5px}
nav{display:flex;gap:22px;flex-wrap:wrap;font:12px Arial,sans-serif;letter-spacing:1.5px;text-transform:uppercase}nav a:hover{color:var(--gold)}
.hero{min-height:78vh;display:grid;grid-template-columns:1.05fr .95fr;align-items:center;gap:30px;padding:64px clamp(22px,8vw,120px);background:radial-gradient(ellipse at 75% 45%,#21412d55,transparent 45%),linear-gradient(135deg,#080b09,#101711)}
.kicker{color:var(--gold);letter-spacing:4px;text-transform:uppercase;font:12px Arial,sans-serif}.hero h1{font-size:clamp(42px,6.5vw,82px);font-weight:400;line-height:1.04;margin:20px 0}.hero h1 em{color:var(--gold);font-weight:400}.hero p{color:var(--muted);font:16px/1.9 Arial,sans-serif;max-width:520px}.actions{display:flex;gap:14px;flex-wrap:wrap;margin-top:30px}.btn{padding:14px 22px;border:1px solid var(--gold);font:12px Arial,sans-serif;letter-spacing:1.4px;text-transform:uppercase;transition:.25s}.btn.primary{background:var(--gold);color:#10120d}.btn:hover{transform:translateY(-3px);box-shadow:0 8px 25px #d9b36b22}.hero-logo{display:flex;justify-content:center;align-items:center}.hero-logo img{width:min(100%,440px);height:auto;border-radius:50%;box-shadow:0 0 70px #c9a35a18;animation:float 5s ease-in-out infinite}
section{padding:76px clamp(22px,8vw,120px)}.section-head{text-align:center;margin-bottom:38px}.section-head .kicker{font-size:11px}.section-head h2{font-size:clamp(30px,4vw,48px);font-weight:400;margin:12px 0}.section-head p{color:var(--muted);font:14px/1.8 Arial,sans-serif}
.products{background:#0c100d}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.card{border:1px solid #d9b36b33;background:linear-gradient(145deg,#141b16,#0c100d);padding:28px 24px;min-height:210px;transition:.3s}.card:hover{transform:translateY(-6px);border-color:var(--gold)}.gem{font-size:32px;color:var(--gold)}.card h3{font-size:23px;font-weight:400;margin:18px 0 8px}.card p{font:13px/1.8 Arial,sans-serif;color:var(--muted)}.note{font:12px/1.7 Arial,sans-serif;color:#b7ad96;text-align:center;margin-top:25px}
.story{display:grid;grid-template-columns:1fr 1fr;gap:45px;align-items:center}.story h2{font-size:clamp(32px,4vw,50px);font-weight:400}.story p{font:15px/2 Arial,sans-serif;color:var(--muted)}.story-mark{border:1px solid #d9b36b66;padding:34px;text-align:center;color:var(--gold);font-size:28px;line-height:1.7}
.contact{background:linear-gradient(135deg,#111a13,#080b09);text-align:center}.contact-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}.contact-item{border:1px solid #d9b36b44;padding:24px}.contact-item small{font:11px Arial,sans-serif;letter-spacing:2px;color:var(--gold);text-transform:uppercase}.contact-item p{font:14px/1.7 Arial,sans-serif;color:var(--muted);overflow-wrap:anywhere}
footer{padding:28px 20px;border-top:1px solid #d9b36b33;text-align:center;color:var(--muted);font:12px/1.8 Arial,sans-serif}footer strong{color:var(--gold)}
.reveal{opacity:0;transform:translateY(22px);transition:opacity .7s ease,transform .7s ease}.reveal.visible{opacity:1;transform:translateY(0)}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@media(max-width:760px){.topbar{align-items:flex-start}.brand img{width:48px;height:48px}nav{gap:10px;justify-content:flex-end;font-size:10px}.hero{grid-template-columns:1fr;text-align:center;padding-top:50px}.hero p{margin-inline:auto}.actions{justify-content:center}.hero-logo{grid-row:1}.hero-logo img{width:min(72%,300px)}.grid,.contact-grid,.story{grid-template-columns:1fr}.story-mark{order:-1}section{padding-top:55px;padding-bottom:55px}}
</style>
</head>
<body>
<header class="topbar">
<a class="brand" href="#home"><img src="/static/alpana-logo.png" alt="Original Alpana Jewellery logo"><span><div class="brandname">Alpana Jewellery</div><div class="tagline">HANDMADE WITH LOVE</div></span></a>
<nav><a href="#home">Home</a><a href="#collection">Collection</a><a href="#story">Our Story</a><a href="#contact">Contact</a></nav>
</header>
<main>
<section class="hero" id="home">
<div class="reveal"><div class="kicker">Elegance in every detail</div><h1>Jewellery that<br><em>tells your story.</em></h1><p>Thoughtfully handcrafted pieces, made to celebrate your style, your moments, and the beauty that makes you uniquely you.</p><div class="actions"><a class="btn primary" href="#collection">Explore Collection</a><a class="btn" href="#contact">Get in Touch</a></div></div>
<div class="hero-logo reveal"><img src="/static/alpana-logo.png" alt="Alpana Jewellery original logo"></div>
</section>
<section class="products" id="collection"><div class="section-head reveal"><div class="kicker">Made for your moments</div><h2>The Collection</h2><p>Discover your next favourite piece.</p></div>
<div class="grid">
<article class="card reveal"><div class="gem">✧</div><h3>Statement Necklaces</h3><p>Beautiful pieces to bring a little extra glow to every occasion.</p></article>
<article class="card reveal"><div class="gem">❋</div><h3>Handcrafted Earrings</h3><p>Delicate details and standout designs, made to express your style.</p></article>
<article class="card reveal"><div class="gem">◇</div><h3>Bangles & Accessories</h3><p>Finishing touches for festive days, celebrations, and everyday elegance.</p></article>
</div><p class="note">Demo collection: replace these categories and add real product photos, prices, and ordering details before publishing.</p>
</section>
<section id="story"><div class="story"><div class="reveal"><div class="kicker">Our little world</div><h2>Handmade with love.<br><em style="color:var(--gold)">Chosen by you.</em></h2><p>At Alpana Jewellery, every detail is inspired by the joy of dressing up and the memories we make along the way. We believe jewellery should feel personal, special, and full of character.</p><p>Replace this introduction with your brand's real story whenever you're ready.</p></div><div class="story-mark reveal">A little sparkle.<br>A lasting memory.<br><span style="font-size:15px;letter-spacing:3px">ALPANA JEWELLERY</span></div></div></section>
<section class="contact" id="contact"><div class="section-head reveal"><div class="kicker">We would love to hear from you</div><h2>Let's Connect</h2><p>Update the demo contact details below with your real information.</p></div><div class="contact-grid">
<div class="contact-item reveal"><small>Visit Us</small><p>Demo Address<br>Replace with your shop address</p></div>
<div class="contact-item reveal"><small>Call / WhatsApp</small><p>+91 90000 00000<br>Replace with your contact number</p></div>
<div class="contact-item reveal"><small>Follow Along</small><p><a href="#" aria-label="Facebook demo link">Facebook</a> &nbsp;·&nbsp; <a href="#" aria-label="Instagram demo link">Instagram</a><br>Replace # with your page links</p></div>
</div></section>
</main>
<footer><strong>Alpana Jewellery</strong> · Handmade with Love<br>Demo website — update placeholder details before sharing publicly.</footer>
<script>
const observer = new IntersectionObserver(entries => entries.forEach(entry => { if(entry.isIntersecting){entry.target.classList.add('visible');observer.unobserve(entry.target)}}), {threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
</script>
</body></html>
"""

@app.route("/")
def home():
    return render_template_string(PAGE)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
