#!/usr/bin/env python3
"""
ai-images.py - TRUE AI image modernization for the Bedek dental site.

This script is READY TO RUN but does nothing useful until you provide an
image-capable API key (none was available when the deterministic prep ran).

It performs:
  A) PORTRAIT modernization (identity-preserving image *edit*) for the two
     dentists -> public/images/team/<name>-modern.<ext>
  B) ROOM modernization (image-to-image renovation, same geometry) for every
     old gallery photo in assets/praxis-original/ -> public/images/praxis/<name>-modern.jpeg

------------------------------------------------------------------------------
TLS NOTE: this machine does TLS interception. truststore.inject_into_ssl()
below makes Python trust the locally-installed CA so HTTPS calls succeed.
------------------------------------------------------------------------------

SUPPORTED PROVIDERS (pick one by setting the env var; auto-detected in order):

  1) GOOGLE GEMINI  (recommended - true image edit + img2img)
     env: GEMINI_API_KEY  (or GOOGLE_API_KEY)
     model: gemini-2.5-flash-image  (a.k.a. "Nano Banana")
     pip install: google-genai
     Best for identity-preserving portrait edits and room renovation.

  2) OPENAI
     env: OPENAI_API_KEY   (optionally OPENAI_BASE_URL for Azure/proxy)
     model: gpt-image-1  via the images.edit endpoint
     pip install: openai>=1.0
     Note: gpt-image-1 edit preserves composition reasonably but is weaker at
     exact identity preservation than Gemini for faces.

  3) STABILITY AI
     env: STABILITY_API_KEY
     endpoint: https://api.stability.ai/v2beta/stable-image/control/structure
     Good for room img2img (keeps geometry); NOT ideal for face identity.

Run:
    python scripts/ai-images.py            # does portraits + rooms
    python scripts/ai-images.py portraits  # portraits only
    python scripts/ai-images.py rooms      # rooms only
"""

import truststore
truststore.inject_into_ssl()  # MUST stay first: TLS-interception environment

import base64
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEAM_DIR = os.path.join(ROOT, "public", "images", "team")
PRAXIS_SRC = os.path.join(ROOT, "assets", "praxis-original")
PRAXIS_OUT = os.path.join(ROOT, "public", "images", "praxis")

# Identity-preserving portrait edit. The pair must end up consistent: same 4:5
# framing, similar head size, clean neutral light-grey studio background.
PORTRAIT_PROMPT = (
    "Professional dental-practice headshot retouch. Keep the EXACT same person, "
    "same face, same identity, same age, same hairstyle and same expression - do "
    "not alter facial features. Improve lighting to soft even studio light, "
    "increase sharpness and clarity, fix color balance to natural skin tones. "
    "Replace the background with a clean, smooth, neutral light-grey studio "
    "backdrop. Frame as a 4:5 vertical portrait, head and shoulders, head "
    "centered in the upper third, consistent professional medical look."
)

ROOM_PROMPT = (
    "Photorealistic renovation of THIS dental practice room. Keep the exact same "
    "room geometry, same camera angle, same window and door positions, same "
    "equipment layout. Modernize the finish: fresh clean white and soft-blue "
    "walls, new bright LED lighting, modern flooring, contemporary dental "
    "furniture, spotless and bright. Keep it realistic, same perspective."
)


def detect_provider():
    if os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
        return "gemini"
    if os.environ.get("OPENAI_API_KEY"):
        return "openai"
    if os.environ.get("STABILITY_API_KEY"):
        return "stability"
    return None


# ----------------------------- GEMINI ---------------------------------------
def gemini_edit(src_path, dst_path, prompt):
    from google import genai
    from google.genai import types
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=key)
    with open(src_path, "rb") as f:
        img_bytes = f.read()
    mime = "image/png" if src_path.lower().endswith(".png") else "image/jpeg"
    resp = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[prompt, types.Part.from_bytes(data=img_bytes, mime_type=mime)],
    )
    for part in resp.candidates[0].content.parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            with open(dst_path, "wb") as out:
                out.write(part.inline_data.data)
            return True
    raise RuntimeError(f"Gemini returned no image for {src_path}")


# ----------------------------- OPENAI ---------------------------------------
def openai_edit(src_path, dst_path, prompt, size="1024x1024"):
    from openai import OpenAI
    client = OpenAI()  # reads OPENAI_API_KEY / OPENAI_BASE_URL
    with open(src_path, "rb") as f:
        resp = client.images.edit(
            model="gpt-image-1", image=f, prompt=prompt, size=size,
        )
    b64 = resp.data[0].b64_json
    with open(dst_path, "wb") as out:
        out.write(base64.b64decode(b64))
    return True


# ----------------------------- STABILITY ------------------------------------
def stability_edit(src_path, dst_path, prompt):
    import requests
    key = os.environ["STABILITY_API_KEY"]
    url = "https://api.stability.ai/v2beta/stable-image/control/structure"
    with open(src_path, "rb") as f:
        resp = requests.post(
            url,
            headers={"authorization": f"Bearer {key}", "accept": "image/*"},
            files={"image": f},
            data={"prompt": prompt, "control_strength": 0.7, "output_format": "jpeg"},
            timeout=180,
        )
    if resp.status_code != 200:
        raise RuntimeError(f"Stability error {resp.status_code}: {resp.text[:300]}")
    with open(dst_path, "wb") as out:
        out.write(resp.content)
    return True


EDITORS = {"gemini": gemini_edit, "openai": openai_edit, "stability": stability_edit}


def run_portraits(edit):
    jobs = [
        ("dr-ivan-bedek.png", "dr-ivan-bedek-modern.png"),
        ("dr-martina-laktic.jpg", "dr-martina-laktic-modern.png"),
    ]
    for src, dst in jobs:
        sp = os.path.join(TEAM_DIR, src)
        dp = os.path.join(TEAM_DIR, dst)
        if not os.path.exists(sp):
            print(f"  skip (missing source): {sp}")
            continue
        print(f"  portrait: {src} -> {dst}")
        edit(sp, dp, PORTRAIT_PROMPT)


def run_rooms(edit):
    os.makedirs(PRAXIS_OUT, exist_ok=True)
    srcs = sorted(glob.glob(os.path.join(PRAXIS_SRC, "*.jpeg")))
    for sp in srcs:
        name = os.path.splitext(os.path.basename(sp))[0]
        dp = os.path.join(PRAXIS_OUT, f"{name}-modern.jpeg")
        print(f"  room: {os.path.basename(sp)} -> {os.path.basename(dp)}")
        edit(sp, dp, ROOM_PROMPT)


def main():
    provider = detect_provider()
    if not provider:
        print("ERROR: no image-capable API key found in environment.")
        print("Set ONE of: GEMINI_API_KEY (recommended) | OPENAI_API_KEY | STABILITY_API_KEY")
        print("Then re-run:  python scripts/ai-images.py")
        sys.exit(1)
    edit = EDITORS[provider]
    print(f"Using provider: {provider}")
    what = sys.argv[1] if len(sys.argv) > 1 else "all"
    if what in ("all", "portraits"):
        print("== Portraits ==")
        run_portraits(edit)
    if what in ("all", "rooms"):
        print("== Rooms ==")
        run_rooms(edit)
    print("Done.")


if __name__ == "__main__":
    main()
