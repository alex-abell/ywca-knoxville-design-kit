# PhotoBand

A full-width photo washed in persimmon by CSS, with a heavy white headline on top.

You provide: a photo from YWCA with alt text, a headline, and optionally a short call to action.

- Store the photo as a normal file. Never bake the color into it. The tint comes from three lines of CSS: a `persimmon` background on the container, and on the image `filter: grayscale(1) brightness(1.3) contrast(1.05)` with `mix-blend-mode: multiply`.
- The result: shadows go to black, highlights go to `persimmon`, and nothing is ever lighter than `persimmon`. If the brand color changes, every photo follows.
- Words never cross a face. The hero enforces this with two zones that cannot overlap: words on the left, photo on the right. `--words` sets where the words zone ends (52% by default). The headline and strip cannot grow past it, and the photo cannot start before it.
- Set `--focus` on every photo to point the crop at the face, for example `--focus: 72% 28%`. Check the crop at phone, tablet, and desktop widths before shipping.
- On screens under 768px the photo sits above the words, never behind them.
- Keep hero headlines to two short lines. If the words do not fit their zone, cut words. Do not shrink the type or widen the zone.
- Band version: the left side fades to solid `persimmon` and the heading stays inside the left half. Use bands for places and textures. A photo with a face goes in the hero, where the zones protect it.
- Only large heavy white text or a white strip goes on a photo. Never body text, links, or small labels. Large white text always passes contrast here, because the photo can only darken the persimmon.
- Alt text describes what the photo shows. If it is only atmosphere, such as a landscape behind a heading, leave the alt text empty.
- Crop wide: about 4 to 1 for bands, 16 to 9 for a hero.
- Never use a photo of a program participant.
