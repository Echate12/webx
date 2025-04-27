#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
birthday_page.py
A tiny one-file Python web server that shows
a romantic, animated “Happy Birthday” page.
"""

import http.server
import socketserver
from datetime import date

# ──────────────────────────────────────
#  HTML / CSS / JS page (Restyled for Romance)
# ──────────────────────────────────────
# Use the current date from the server
today_date = date.today()
HTML = f"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Happy Birthday, My Darling 💖</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
    /* === Base layout - Warmer & Softer === */
    html,body {{
        margin:0;padding:0;height:100%;overflow:hidden;
        display:flex;justify-content:center;align-items:center;
        /* Using a more classic serif font for base */
        font-family: Georgia, 'Times New Roman', Times, serif;
        color:#f0e6f0; /* Softer off-white/lavender */
        /* Warmer gradient background */
        background:#1f0d24; /* Dark base */
        background:radial-gradient(circle at bottom, #6d1f4f 0%, #1f0d24 70%);
    }}

    /* === Center card - Elegant & Glowing === */
    .card {{
        text-align:center;
        backdrop-filter:blur(5px); /* Slightly more blur */
        /* Softer, slightly more opaque background */
        background:rgba(255,255,255,.1);
        /* Soft pink border */
        border:1px solid rgba(255, 182, 193, 0.4);
        border-radius:20px; /* More rounded */
        padding:45px 60px; /* Slightly more padding */
        max-width:650px;
        /* Pinkish glow effect */
        box-shadow:0 10px 30px rgba(255, 105, 180, 0.2),
                   0 0 15px rgba(255, 182, 193, 0.15) inset;
        animation: fadeInCard 1.5s ease-out; /* Fade in effect */
    }}
    @keyframes fadeInCard {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to   {{ opacity: 1; transform: scale(1); }}
    }}

    h1 {{
        font-family: 'Georgia', serif; /* Elegant serif */
        font-style: italic;
        font-size:2.8rem; /* Slightly adjusted size */
        font-weight: 500; /* Not too bold */
        margin-bottom:.4em;
        letter-spacing:.03em;
        color:#ffc0cb; /* Light Pink */
        /* Softer shadow + subtle pink glow */
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.4),
                     0 0 8px rgba(255, 182, 193, 0.5);
    }}
    p {{
        font-size:1.2rem; /* Adjusted size */
        line-height:1.65; /* More spacing */
        margin:0;
        color:#e8dcec; /* Lighter lavender */
    }}
    p strong {{
        color: #ffdae0; /* Highlight date gently */
        font-weight: 600;
    }}

    /* === Floating petals - Richer color, slower drift === */
    @keyframes drift {{
        0%   {{transform:translateY(-12vh) translateX(0vw) rotateZ(-30deg) scale(.7); opacity:0;}}
        15%  {{opacity:0.9;}} /* Fade in quicker */
        85%  {{opacity:0.9;}} /* Hold opacity longer */
        100% {{transform:translateY(112vh) translateX(2vw) rotateZ(680deg) scale(1.1); opacity:0;}} /* Slower fall, more rotation, slight growth */
    }}
    .petal {{
        position:fixed;top:-12vh;left:0; /* Start slightly higher */
        width:30px;height:28px; /* Slightly smaller */
        /* Richer Pink SVG Fill: #f75c92 */
        background:url('data:image/svg+xml;utf8,\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 30">\
<path fill="%23f75c92" d="M16 3c-4-6-16 1-8 12 3 4 8 9 8 9s5-5 8-9c8-11-4-18-8-12z"/></svg>') no-repeat center/contain;
        pointer-events:none;
        animation:drift linear infinite;
        /* Add a subtle flutter effect */
        animation-timing-function: cubic-bezier(0.3, 0, 0.7, 1);
    }}
</style>
<script>
// spawn petals forever
function spawnPetal() {{
  const p=document.createElement('div');
  p.className='petal';
  p.style.left=Math.random()*100+'vw';
  // Slower, more varied animation duration
  p.style.animationDuration = 8 + Math.random() * 8 + 's';
  
  document.body.appendChild(p);
  // Increase timeout to ensure petals complete animation
  setTimeout(()=>p.remove(),17000);
}}
// Slightly fewer petals for a calmer effect
setInterval(spawnPetal, 600);
</script>
</head>
<body>
  <div class="card">
    <h1>Happy Birthday, My Darling!</h1>
    <p>
      On <strong>{today_date:%B %d, %Y}</strong> the universe<br>
      still echoes with the joy of the day you arrived,<br>
      filling my world with light and love.<br><br>
      May your heart’s deepest wishes drift upwards tonight,<br>
      like stardust catching the moonlight—that’s how infinite<br>
      my love shines for you. ✨💖
    </p>
  </div>
</body>
</html>
"""

# ──────────────────────────────────────
#  Server handler
# ──────────────────────────────────────
class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML.encode("utf-8"))
        else:
            self.send_error(404, "Not Found")

# ──────────────────────────────────────
#  Launch
# ──────────────────────────────────────
PORT = 8000
# Use 0.0.0.0 to make it accessible on the network if needed, otherwise "" or "localhost"
HOST = "localhost"
with socketserver.TCPServer((HOST, PORT), Handler) as server:
    print(f"🚀 Romantic Birthday page running at http://{HOST}:{PORT}/ (Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Wishing you both a wonderful celebration! 💕")