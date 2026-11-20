# Instructions for AI agents working in this repo

This repo is a design kit for YWCA Knoxville & the Tennessee Valley. It is an unofficial draft that YWCA has not reviewed.

## If you are making something for YWCA

Read `YWCA-DESIGN-KIT.md` before you write or design anything. It holds every rule. Follow it.

The short version:

- Use only the kit's colors, type styles, spacing, and components. Use token names, not raw values.
- Persimmon (`#FA4616`) is for fills, and for text only at 24px and up, or bold at 19px and up.
- Square corners. No shadows.
- Write "YWCA", never "the YWCA". Write "women", "participants", or "residents".
- Never show a count below five. Show "Fewer than 5".
- Never ask for, store, or repeat a resident's name, birth date, address, room number, case note, or photo.
- Never invent a number, quote, or story about YWCA.

## If you are changing the kit

- The source of truth is `tokens/tokens.json`, the files in `guides/`, and each `components/<Name>/README.md`.
- `YWCA-DESIGN-KIT.md` and `tokens/tokens.css` are made by `scripts/build_kit.py`. Do not edit them by hand.
- Do not add photos of people. Do not add YWCA artwork that YWCA did not supply.
- Do not add colors. The palette is persimmon, black, white, and gray.
- Keep every file in plain words. A board member should be able to read it.
