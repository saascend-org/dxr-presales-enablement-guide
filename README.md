# DXR Cyber — Pre-Sales enablement guide

Enablement guide for XYP-PRESALES-001: Pre-Sales requests, triage, lifecycle and KPI reporting
in Salesforce. Built from Carl Osborne's Pre-Sales deck (12 Oct 2026), KPI Scorecard v1.0 and
KPI Tracker v2.0.

## The published file is encrypted

`index.html` is a **password gate**, not the guide. The readable page is AES-256-GCM ciphertext
inside it, under a PBKDF2-SHA256 (600k iteration) key derived from the password. The screenshots
are base64-inlined into that payload, so GitHub never has the guide or the screenshots in the clear.

**The password is not in this repo and must never be committed.** `publish.sh` prompts for it.

## Editing and publishing

The source is the guide artifact in the Xypher project (`build/presales/guide/pre-sales-guide.html`
and `pub/img/`), not this repo. Edit it there, then:

```bash
./publish.sh      # build plaintext, encrypt into index.html, delete plaintext, commit, push
```

`python3 build.py` alone writes `build/index.plain.html` for local reading (git-ignored). Serve it
over http to preview: `crypto.subtle` needs a secure context.
