# Brand rules

Unofficial working draft for the volunteer team building the Keys of Hope dashboard. YWCA has not reviewed it. Where this page and YWCA staff disagree, YWCA is right.

## Voice

Write bold, inspirational, and authentic. Those are the brand guide's three words for tone. Its values are courage, compassion, and commitment.

- Say "YWCA", never "the YWCA".
- Lead with action. "Women find safe housing here" beats "Housing services are provided".
- Write "women", "participants", or "residents". Never "cases" or "clients" in anything a funder or the public reads.
- Use short sentences and plain words. A board member should understand every chart title without a glossary.
- Speak as "we" and "our work". Write "YWCA Knoxville", not "the YWCA in Knoxville".
- End with a clear next step: advocate, take part, or donate.
- No emoji.

The full writing rules, with examples, are in `guides/voice-and-writing.md`.

## Color

Persimmon is the signal. The brand guide says it must never be overpowered or replaced by other colors, and that the palette should feel "bright, crisp and optimistic".

- Use `persimmon` for button and tile fills, headings, big numbers, and the one mark that matters in a chart. Large type and the logo on it are `white`. Anything smaller on it is `on-persimmon`, which is black.
- Set body text in `ink` on `ground`. Use `ink-muted` for captions.
- Use `persimmon` for text only at 24px and up, or bold at 19px and up. Smaller text is `ink`.
- White text on `persimmon` follows the same size rule. Smaller text on persimmon is `black`.
- Links are `ink` with a `persimmon` underline.
- Never put `persimmon` on `gray-10`.
- Use black as the second voice: caption blocks under photos, the newsletter band, half of a two-color headline.
- Use the grays for context: `gray-50` for supporting bars, `rule` for gridlines, `gray-10` for quiet panels.
- Do not build a ramp of persimmon tints. YWCA USA told local associations this weakens the color.
- Never use red and green to mean bad and good. Say it in words.

The whole palette is persimmon, black, white, and gray, with values from the official YWCA site, ywca.org. There are no other colors. ywcaknox.com uses a slightly redder persimmon (#EF4923) and the 2018 brand guide prints #FD5A1E. Neither is used here.

## Type

- Set headlines, headings, big numbers, and button labels in the `display` family, in capitals. That is Avenir Next Pro Heavy where it is licensed and Arial Black everywhere else.
- Set everything else in the `body` family. That is Source Sans, free from Google Fonts, with Arial as the fallback.
- Build a two-color headline the way YWCA does: one phrase in `persimmon`, the rest in `black`. See `MissionHeadline`.
- Use `heading` in `persimmon` for section headings on white, and in `white` on black or persimmon.
- In Power BI, use Arial Black and Arial. They are the brand guide's approved substitutes, and they are on every computer.

## Logo

Two logos are in `assets/logos/`. The white one is YWCA Knoxville's own file, unchanged. The persimmon one was made for this system from that file. Only the ink color changed.

- Use the white logo on `persimmon`, on `black`, or on a simple dark photo.
- Use the persimmon logo on `white` and on `gray-10`. Never on a photo, on `black`, or on `persimmon`.
- The logo is one color, always: all white or all `persimmon`. Do not recolor it any other way, outline it, stretch it, or split its parts.
- Keep clear space around the logo equal to the height of the "w" in it.
- Never show it smaller than 100px wide on screen or one inch in print.
- Do not recolor, stretch, crop, shadow, or box it. Do not redraw it.

## Layout

- Keep every corner square with `radius-none`.
- Give each web page section `space-6` above and below. Report page margins are `space-4`.
- On posters, slides, and covers, follow the brand guide: a persimmon field, a heavy headline, one white strip with a call to action, the white logo low on the page. See `CallToActionStrip` and `SlideTitle`.
- Alternate white sections with full-width bands of black, persimmon, or a persimmon-toned photo.
- Center short headings and their text, as the website does. Left-align anything longer than three lines.
- No drop shadows.
- Show keyboard focus with a 3px `black` ring, offset 2px, with a 2px `white` edge inside it. That one ring shows on white, black, and persimmon.
- Every button and field is at least 48px tall. Text links have at least 24px of height to themselves.
- Every layout must work at 320px wide with no sideways scrolling.

## Charts

- Make one point per chart. Write that point as the title.
- Color the bar or line that carries the point `persimmon`. Color the rest `gray-50`.
- When two series both need names, use `persimmon` and `gray-80`, and label them on the chart.
- Label values directly. Drop the legend when you can.
- Start bar charts at zero. No 3D, no pie with more than three slices.
- Always show what a percentage is out of.

## Privacy

Many women in YWCA programs are survivors of domestic violence. Design for their safety first.

- Never show a name, birth date, address, or photo of a participant.
- Hide any count below five. Show "Fewer than 5" in its place, using the `DataTable` and `PrivacyNotice` patterns.
- Put `QuickExit` on every public web page. Both YWCA websites do.

## Imagery

Rules drawn from the brand guide and from the six banner photos on ywcaknox.com.

- Show three kinds of picture: a woman smiling straight at the camera, people doing something together (hands, a group), and places people in Knoxville know (the river, the mountains).
- Wash banner photos in one color. Use the `PhotoBand` CSS so shadows go black and highlights go `persimmon`. Never bake the color into the file.
- Words never cross a face, a logo never crosses a face, and nothing crops a face at the eyes or mouth. Give words and faces separate zones, as `PhotoBand` does.
- Keep faces sharp and backgrounds soft. Pick photos with the subject off center, so there is a calm side for words.
- Put only a heavy white headline or a white strip on a photo. Never small text.
- Crop wide: about 4 to 1 for bands, 16 to 9 for a hero.
- Full-color photos are fine in cards and grids, as the brand guide shows. Do not mix tinted and full-color photos in one row.
- Use only photos YWCA supplies. Never show a program participant.
- Write alt text for every photo that carries meaning.

## Iconography

ywcaknox.com uses Font Awesome 5 solid icons in white on its action tiles and contact line. This system carries no icon files. Use words first. If an icon is needed, use Font Awesome 5 solid in one color, with a label beside it.

## Where each part comes from

From ywca.org, measured on the live site: `persimmon`, `gray-10`, the black `QuickExit`.

From ywcaknox.com, measured on the live site: the `display`, `heading`, `button`, `body`, `nav`, and `stat-label` type styles, `space-6`, `radius-none`, and the components `Button`, `QuickExit`, `MissionHeadline`, `ValueTrio`, `LocationCard`, `ActionTile`, `StatTile`, `NewsletterBand`, `SiteFooter`, and the photo treatment in `PhotoBand`.

From the 2018 YWCA USA brand guide, read in full: the font families, black, white, the brand gray, the logo rules, the photo rules, the components `CallToActionStrip` and `SlideTitle`, and the guides `voice-and-writing.md` and `print-slides-and-other-uses.md`.

Added for dashboards and for contrast, as proposals: `gray-50`, `gray-60`, `gray-80`, the names `ground`, `ink`, `ink-muted`, `rule`, the `headline`, `deck`, `small`, and `label` type styles, `space-1` to `space-5`, the components `HighlightBar`, `DataTable`, `PrivacyNotice`, `TextField`, and the Power BI theme and rules.
