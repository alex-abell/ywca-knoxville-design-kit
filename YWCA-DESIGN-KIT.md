# YWCA Knoxville design kit, in one file

This file holds the whole kit so an AI assistant can read it in one go. Give it to the assistant
at the start of a chat, then ask for what you need. People can read it too.

It is made from the other files in this repo by `scripts/build_kit.py`. Change those files, not this one.

## Instructions for the AI assistant reading this

You are helping staff and volunteers at YWCA Knoxville & the Tennessee Valley make things that
look and sound like YWCA: charts, reports, slides, flyers, web pages, and writing.

- Follow every rule in this file. When a request conflicts with a rule, say so in one sentence,
  then offer the closest thing that follows the rules.
- This kit is an unofficial working draft made by volunteers. YWCA has not reviewed it. Where
  this file and YWCA staff disagree, YWCA staff are right.
- Use only the colors, type styles, spacing, and components named here. Do not invent new ones.
- Never ask for, accept, or repeat a resident's name, birth date, address, room number, case
  note, or photo. If someone pastes one, tell them to remove it and carry on without it.
- Never show a count below five. Show "Fewer than 5" in its place.
- Write "YWCA", never "the YWCA". Write "women", "participants", or "residents".
- Never write a number, quote, or story about YWCA that you were not given. Ask for it.
- When you write code, use the token names (for example `var(--persimmon)`), not raw values.
- When you are not sure a rule applies, say what you assumed.

## Brand rules

Unofficial working draft for the volunteer team building the Keys of Hope dashboard. YWCA has not reviewed it. Where this page and YWCA staff disagree, YWCA is right.

### Voice

Write bold, inspirational, and authentic. Those are the brand guide's three words for tone. Its values are courage, compassion, and commitment.

- Say "YWCA", never "the YWCA".
- Lead with action. "Women find safe housing here" beats "Housing services are provided".
- Write "women", "participants", or "residents". Never "cases" or "clients" in anything a funder or the public reads.
- Use short sentences and plain words. A board member should understand every chart title without a glossary.
- Speak as "we" and "our work". Write "YWCA Knoxville", not "the YWCA in Knoxville".
- End with a clear next step: advocate, take part, or donate.
- No emoji.

The full writing rules, with examples, are in `guides/voice-and-writing.md`.

### Color

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

### Type

- Set headlines, headings, big numbers, and button labels in the `display` family, in capitals. That is Avenir Next Pro Heavy where it is licensed and Arial Black everywhere else.
- Set everything else in the `body` family. That is Source Sans, free from Google Fonts, with Arial as the fallback.
- Build a two-color headline the way YWCA does: one phrase in `persimmon`, the rest in `black`. See `MissionHeadline`.
- Use `heading` in `persimmon` for section headings on white, and in `white` on black or persimmon.
- In Power BI, use Arial Black and Arial. They are the brand guide's approved substitutes, and they are on every computer.

### Logo

Two logos are in `assets/logos/`. The white one is YWCA Knoxville's own file, unchanged. The persimmon one was made for this system from that file. Only the ink color changed.

- Use the white logo on `persimmon`, on `black`, or on a simple dark photo.
- Use the persimmon logo on `white` and on `gray-10`. Never on a photo, on `black`, or on `persimmon`.
- The logo is one color, always: all white or all `persimmon`. Do not recolor it any other way, outline it, stretch it, or split its parts.
- Keep clear space around the logo equal to the height of the "w" in it.
- Never show it smaller than 100px wide on screen or one inch in print.
- Do not recolor, stretch, crop, shadow, or box it. Do not redraw it.

### Layout

- Keep every corner square with `radius-none`.
- Give each web page section `space-6` above and below. Report page margins are `space-4`.
- On posters, slides, and covers, follow the brand guide: a persimmon field, a heavy headline, one white strip with a call to action, the white logo low on the page. See `CallToActionStrip` and `SlideTitle`.
- Alternate white sections with full-width bands of black, persimmon, or a persimmon-toned photo.
- Center short headings and their text, as the website does. Left-align anything longer than three lines.
- No drop shadows.
- Show keyboard focus with a 3px `black` ring, offset 2px, with a 2px `white` edge inside it. That one ring shows on white, black, and persimmon.
- Every button and field is at least 48px tall. Text links have at least 24px of height to themselves.
- Every layout must work at 320px wide with no sideways scrolling.

### Charts

- Make one point per chart. Write that point as the title.
- Color the bar or line that carries the point `persimmon`. Color the rest `gray-50`.
- When two series both need names, use `persimmon` and `gray-80`, and label them on the chart.
- Label values directly. Drop the legend when you can.
- Start bar charts at zero. No 3D, no pie with more than three slices.
- Always show what a percentage is out of.

### Privacy

Many women in YWCA programs are survivors of domestic violence. Design for their safety first.

- Never show a name, birth date, address, or photo of a participant.
- Hide any count below five. Show "Fewer than 5" in its place, using the `DataTable` and `PrivacyNotice` patterns.
- Put `QuickExit` on every public web page. Both YWCA websites do.

### Imagery

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

### Iconography

ywcaknox.com uses Font Awesome 5 solid icons in white on its action tiles and contact line. This system carries no icon files. Use words first. If an icon is needed, use Font Awesome 5 solid in one color, with a label beside it.

### Where each part comes from

From ywca.org, measured on the live site: `persimmon`, `gray-10`, the black `QuickExit`.

From ywcaknox.com, measured on the live site: the `display`, `heading`, `button`, `body`, `nav`, and `stat-label` type styles, `space-6`, `radius-none`, and the components `Button`, `QuickExit`, `MissionHeadline`, `ValueTrio`, `LocationCard`, `ActionTile`, `StatTile`, `NewsletterBand`, `SiteFooter`, and the photo treatment in `PhotoBand`.

From the 2018 YWCA USA brand guide, read in full: the font families, black, white, the brand gray, the logo rules, the photo rules, the components `CallToActionStrip` and `SlideTitle`, and the guides `voice-and-writing.md` and `print-slides-and-other-uses.md`.

Added for dashboards and for contrast, as proposals: `gray-50`, `gray-60`, `gray-80`, the names `ground`, `ink`, `ink-muted`, `rule`, the `headline`, `deck`, `small`, and `label` type styles, `space-1` to `space-5`, the components `HighlightBar`, `DataTable`, `PrivacyNotice`, `TextField`, and the Power BI theme and rules.

## Tokens

The same values are in `tokens/tokens.json` and, as CSS variables, in `tokens/tokens.css`.

### Color

| Token | Value | Use |
| --- | --- | --- |
| `persimmon` | #FA4616 | YWCA's persimmon as used on the official site, ywca.org. A fill color first: buttons, tiles, bands, link underlines, and the one bar that carries a chart's point. As type, only for headings and big numbers at 24px and up, or bold at 19px and up, because it measures 3.5 to 1 against a white page. Never beside gray-10 (2.96 to 1). |
| `on-persimmon` | #000000 (same as `black`) | The safe text color on persimmon fills at any size: black, 6.0 to 1. Footer addresses, links, and small labels use it. |
| `black` | #000000 | Primary brand color. Body text, links, small text on persimmon, half of a two-color headline, caption blocks under photos, the newsletter band, Quick Escape, the focus ring. |
| `white` | #FFFFFF | Primary brand color. Page and report background, and text over black. Over a persimmon fill, white is for large type and the logo only: 24px and up, or bold at 19px and up. That pair measures 3.5 to 1, which meets AA for large text and fails it for body text. Smaller text over persimmon uses on-persimmon. |
| `gray-10` | #EBEBEB | The panel gray on ywca.org. Quiet panel fills, card grounds, notices. |
| `gray-20` | #CCCCCC | The brand gray (Pantone Cool Gray 5, hex as printed in the brand guide). Hairlines between table rows, gridlines, the short rule above a value heading. Decoration only. It measures 1.6 to 1 against a white page, so never text, never a chart mark, never a field border. |
| `gray-50` | #808080 | 50% black. Chart bars and lines that give context beside the persimmon one. Meets the 3 to 1 minimum for graphics against a white page (3.9 to 1). Not for text. |
| `gray-60` | #666666 | 60% black. Secondary text on white (5.7:1) and gray-10 (4.8:1), and form field borders on white. |
| `gray-80` | #333333 | 80% black. A second chart series when two things must be named. |
| `ground` | #FFFFFF (same as `white`) | Default surface behind everything. |
| `ink` | #000000 (same as `black`) | Default text on ground and gray-10. |
| `ink-muted` | #666666 (same as `gray-60`) | Captions, labels, and footnotes on ground and gray-10. |
| `rule` | #CCCCCC (same as `gray-20`) | Dividers and chart gridlines on ground. |

### Type families

| Family | Font stack |
| --- | --- |
| `display` | "avenir-next-pro-heav", "Avenir Next", "Avenir Next Pro", "Arial Black", Arial, sans-serif |
| `body` | "Source Sans 3", "Source Sans Pro", Arial, sans-serif |

### Type styles

| Style | Family | Size | Line height | Weight | Use |
| --- | --- | --- | --- | --- | --- |
| `display` | display | 80px | 96px | 900 | The hero headline on ywcaknox.com, in capitals. One per page. |
| `stat` | display | 64px | 64px | 900 | The number in a StatTile. Size estimated from ywcaknox.com. |
| `headline` | display | 40px | 44px | 900 | Page titles in reports and dashboards, in capitals. Added; the website jumps from 80px to 25px. |
| `heading` | display | 25px | 30px | 900 | Section, card, and tile headings on ywcaknox.com, in capitals. |
| `button` | display | 19px | 24px | 900 | Button labels, in capitals. ywcaknox.com sets them at 15px; raised to 19px so white on persimmon passes AA as large bold text. |
| `deck` | body | 24px | 32px | 400 | The sentence under a headline, as in the brand guide. |
| `stat-label` | body | 20px | 26px | 700 | The label under a StatTile number, and chart titles. |
| `body` | body | 18px | 30px | 400 | Body copy on ywcaknox.com. |
| `nav` | body | 16px | 16px | 600 | Navigation links on ywcaknox.com, in capitals. |
| `small` | body | 16px | 24px | 400 | Table cells, chart labels, captions, footnotes. Added. |
| `label` | body | 14px | 20px | 700 | Field labels, in capitals. Added. |

### Spacing

| Token | Value | Use |
| --- | --- | --- |
| `space-1` | 4px | Between a label and its field or value. |
| `space-2` | 8px | Inside table cells; the Power BI snap grid. |
| `space-3` | 16px | Card padding, gaps between tiles. |
| `space-4` | 24px | Report page margins, gaps between sections of a report page. |
| `space-5` | 32px | Between columns on the web. |
| `space-6` | 64px | Top and bottom padding of every page section on ywcaknox.com. |

### Corners

| Token | Value | Use |
| --- | --- | --- |
| `radius-none` | 0 | Everything on ywcaknox.com: buttons, fields, cards, photos, tiles. |
| `radius-pill` | 15px | Buttons on ywca.org only. YWCA Knoxville does not round its buttons. |

## Components

Each one is plain HTML and CSS. The working markup is in `components/<Name>/preview.html`.

### ActionTile

A wide persimmon block with a white label, for the two or three things you most want a visitor to do.

You provide: a label of one or two words and a link. An icon is optional.

- Label in `heading`, capitals, `white`. At 25px heavy it passes contrast as large text.
- At least 96px tall. On hover it turns `black`.
- ywcaknox.com puts a white Font Awesome icon to the left of each label. Leave it out unless you have that icon set. If you add one, hide it from screen readers.
- Two or three in a row, over a photo band or on white. They stack on phones.
- For a single action inside text, use `Button`.

### Button

The one button style: a square persimmon block with white heavy capitals.

You provide: the label and where it goes.

- Label in the `button` type style, capitals, two or three words: "Learn more", "Subscribe", "Give now".
- Square corners. At least 48px tall, with `space-4` on each side.
- On hover it turns `black`. On keyboard focus it gets a 3px black ring with a white edge, which shows on white, black, and persimmon.
- It looks the same on white, black, and photo backgrounds.
- Text links in body copy are `ink`, weight 600, with a 3px `persimmon` underline. The text is black so it passes contrast at any size.
- Contrast: white on `persimmon` is 3.5:1. That passes AA only for large bold text, which is why the label is 19px heavy. ywcaknox.com uses 15px, which does not pass. Never shrink the label.
- ywca.org rounds its buttons with `radius-pill`. YWCA Knoxville does not.

### CallToActionStrip

A white strip on a persimmon field holding a few heavy black capitals, as on the brand guide's banners and ads.

You provide: two or three words. Optionally one word to color persimmon.

- Keep it to a short command or phrase: "Join us.", "To empower", "Give today."
- The strip is `white`. The words are `black` in the `display` family, 28px or larger. One word may be `persimmon`.
- It sits on a `persimmon` field or a persimmon-toned photo, touching the left edge.
- One strip per layout. The preview shows two only to show both versions.
- For a clickable action on a web page, use `Button` or `ActionTile`.

### DataTable

A plain table for the detail behind a chart.

You provide: a caption, column headers, rows, and a total.

- Give the table a caption that says what it shows.
- Mark column headers and row labels as headers, so screen readers can read a cell with its row and column.
- Left-align words, right-align numbers.
- One black rule under the header and above the total. `rule` hairlines between rows. No zebra stripes.
- Always end with a total row, so readers can see what the shares add up to.
- Replace any count under five with "Fewer than 5" and its share with "Hidden". Fold the hidden amount into an "all other" row so nobody can work it out by subtraction.
- Wrap it in a scrolling region that the keyboard can reach, so a very wide table never breaks the page.
- Keep it under about 640px wide so numbers stay close to their labels.
- Sort by the column people will scan, largest first.

### HighlightBar

A bar chart where one bar is persimmon and the rest are gray.

Use it to compare a handful of groups when one of them is the point.

You provide: the title, written as the finding, plus a label, a group size, and a value for each bar, and which bar to highlight.

- Highlight one bar only. If nothing stands out, make every bar `gray-50`.
- The highlighted row is also bold, so the point does not depend on color.
- Print the value right at the end of each bar. No legend, no axis.
- Put the group size under each label. A percentage always says what it is out of.
- Bars start at zero. `persimmon` and `gray-50` both stand out against white at 3:1 or better.
- Rows are a real list and every value is real text, so screen readers read the chart as a short list.
- Name the highlighted group in the title.

### LocationCard

A photo with a black caption block under it, linking to a place or a program.

You provide: a photo from YWCA with alt text, a name, and a link.

- The whole card is one link. The photo sits flush on top of the caption. No gap, no border, square corners.
- The caption is `black` with a white `heading` in capitals, centered. Captions in a row are the same height.
- On hover the caption turns `persimmon`.
- Give every photo alt text that says what it shows. If the photo adds nothing, give it empty alt text.
- Three across on wide screens, stacked on phones.
- Never use a photo of a program participant.

### MissionHeadline

A headline in heavy capitals with one phrase in a second color.

You provide: the words, and which phrase carries the second color.

- On white: one phrase in `persimmon`, the rest in `black`. "YWCA is on a mission" colors "YWCA".
- On persimmon: one phrase in `white`, the rest in `black`, as on the brand guide's tote bag and sticker. All white over a photo.
- Color the subject or the payoff, never a filler word.
- Persimmon and white-on-persimmon words must be 24px or larger. A headline always is.
- Mark it up as a real heading (`h1` once per page, then `h2`). Type the words in normal case and let CSS make the capitals, so screen readers do not spell them out.
- Use `display` for the one hero headline on a page and `heading` in `persimmon` for section headings.
- YWCA USA treats "YWCA IS ON A MISSION" as a graphic with three fixed arrangements and minimum sizes. Those rules are on the "Print, slides, and other uses" page.
- Do not add a third color.

### NewsletterBand

A full-width black band with a short pitch on one side and an email field with a persimmon button on the other.

You provide: a heading, one sentence, and where the form sends the address.

- The band is `black`. Heading and text are `white`.
- The field has a visible label above it, a 3px white border, and white text. ywcaknox.com uses a placeholder as the only label. A placeholder disappears when you type, so this version adds a real label.
- The field is 52px tall and marked for email autofill.
- The button is a full-width `Button`. On this black band its hover turns white.
- Focus rings are white here.
- The two halves stack on phones.
- One per page, just above the footer.

### PhotoBand

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

### PrivacyNotice

A short note that explains why some numbers are missing.

Put one at the bottom of any page or report that hides small counts.

You provide: nothing. The wording is fixed so every page says it the same way.

- A `gray-10` panel with `ink` text. No border, no icon.
- It informs, it does not warn. Do not color it.
- Do not use it for errors or for marketing messages.

### QuickExit

A button that takes a visitor off the site at once, for someone whose screen may be watched.

You provide: the neutral page to send people to, such as a weather or search site.

- Fix it to the bottom right of the window on every public page, with `position: fixed`. Leave 80px of padding at the bottom of the page so it never covers content.
- Label it "Quick escape". Both YWCA websites use those words. It is a real `button`, so screen readers and keyboards reach it.
- White on `black`, at least 48px tall, square corners. ywca.org makes its Quick Escape black, which gives 21:1 contrast and keeps it from looking like a donate button.
- On click, replace the current page so the Back button does not return to it. The bundle does this for you: `YWCAKnox.bindQuickExit(button, url)`.
- Make it the first thing the Tab key reaches on the page, before the skip link.
- Give it a hidden description that says where it goes, such as "Leaves this site right away and opens a weather site."
- Its focus ring is white and drawn inside the button, so it shows over any band and is not cut off at the window edge.
- Add `scroll-padding-bottom: 72px` to the page so the button never hides the control that has keyboard focus.
- Do not bind it to the Esc key. Esc already closes menus and dialogs and switches screen reader modes, so it would fire by accident. For a keyboard shortcut, follow the UK government's "Exit this page" pattern: pressing Shift three times. Say so in visible text.
- Tell visitors the button exists, in a line near the top of the page.
- ywca.org hangs it as a tab on the right edge. ywcaknox.com puts it bottom right. Either place works.
- Staff-only Power BI reports do not need it.

### SiteFooter

The closing band of a page: the white logo on persimmon, with a column for each YWCA Knoxville location.

You provide: the address, email, and phone for each location.

- The ground is solid `persimmon`. ywcaknox.com puts a photo behind its footer, but small contact text over a photo cannot hold contrast, so this one stays solid.
- The logo is the white YWCA Knoxville logo from the Logos group, at least 100px wide, with clear space around it and alt text that names YWCA.
- Location names are headings in white heavy capitals at 20px, which passes as large bold text.
- Contact lines are `black`, 16px, weight 600, underlined when they are links. ywcaknox.com sets them in white, which fails contrast at that size.
- Wrap the band in a `footer` and each location in an `address`.
- The logo sits on its own row above three even columns. Address lines stay level even when a location name wraps. Everything stacks on phones.
- Show the real address, email, and phone as the link text.
- This is also the pattern for a report header strip: white logo left, on persimmon.

### SlideTitle

The title slide from the brand guide's PowerPoint template: a persimmon field, a white Arial title, the white logo bottom left.

You provide: a title, a subtitle, and optionally a portrait photo from YWCA for the right side.

- Title in Arial Bold 44pt, white. Subtitle in Arial Regular 24pt, white. Both are large enough to pass contrast on persimmon. Do not go smaller than 24pt for white text on persimmon.
- The white logo sits bottom left, at least 100px wide on screen.
- The one-line "ON A MISSION" graphic sits on a white strip bottom right. Use YWCA's artwork if you have it. The strip's type never drops below 19px heavy, so the persimmon word stays readable.
- Slides use Arial so they look the same on every computer. The Power BI theme uses Arial for the same reason.
- Ask YWCA Knoxville for the official PowerPoint template before building one.

### StatTile

One big persimmon number with a bold label and a line of context, as in the stats row on ywcaknox.com.

You provide: a value, a label, and a context line.

- The number is `stat` in `persimmon`. The label is `stat-label` in `ink`. The context line is `small` in `ink-muted`.
- Number, label, and context sit in one paragraph, so a screen reader reads them as one statement.
- The context line is required. A percentage always says what it is out of.
- Three or four across, centered. They stack on phones.
- If the count behind a tile is under five, show "Fewer than 5" instead of the number.
- Do not animate the number counting up.

### TextField

A labeled text input for forms on a white page.

You provide: the label, the input type, a hint if the format is not obvious, and the error message if there is one.

- The label sits above the field and is always visible. No placeholder-only fields.
- Put the expected format in a hint between the label and the field.
- Square corners, 48px tall. The border is 2px `gray-60`, which stands out against white at 5.7:1.
- Show an error with a 4px black border and a message that starts with "Error:" and says how to fix it. Do not use red. Mark the field invalid and tie the message to it, so screen readers announce both. When the message appears after the page has loaded, give it `role="alert"`.
- Set the autofill type for names, emails, and phone numbers.
- On a black band, use the white-outlined field in `NewsletterBand`.

### ValueTrio

Three short ideas side by side, each under a small gray rule and a persimmon heading.

ywcaknox.com uses it for the three YWCA values. It also suits three program areas or three findings.

You provide: three headings of one or two words, and one or two sentences for each.

- The rule is 91px wide and 3px thick in `gray-20`. It is decoration and is hidden from screen readers.
- Headings are real headings in the `heading` style, `persimmon`. At 25px heavy they pass contrast as large text.
- Text is `body` in `ink`, centered, no wider than about 30 characters.
- Columns stack on narrow screens.
- Keep it to three. Four or more become a list.

## Power BI

Import `assets/power-bi/ywca-knoxville-theme.json` first. It sets the colors and fonts below so nobody has to pick them by hand. It has not been tested in Power BI Desktop yet.

### Page

- Use the 16:9 canvas at 1280 by 720.
- Keep a 24px margin on every side (`space-4`). Snap visuals to an 8px grid (`space-2`).
- Keep the page white. No background images, no shadows, no rounded visual borders.
- Put the YWCA Knoxville logo top left, at least 100px wide, with nothing crowding it. The white logo needs a persimmon or black strip behind it.
- Give each page one job and name it in the page title: "WHO WE SERVE", "ENGAGEMENT", "OUTCOMES".

### Layout of a page

| Zone | What goes there |
| --- | --- |
| Top strip | Logo, page title, the date the data was last refreshed |
| Row one | Up to four cards, each one number with its label |
| Middle | One or two charts that answer the page's question |
| Bottom | A plain table for detail, and the privacy note |
| Left or top | Slicers for period and program. Keep them the same on every page. |

### Color

- The first data color is persimmon (#FA4616). Use it for the one bar or line that carries the point.
- Recolor every other series gray. In a bar chart, set the default color to #808080 and use conditional formatting to turn the highlighted bar #FA4616.
- Every data color in the theme is at least 3:1 against white, so marks stay visible. Do not add light grays as series colors.
- Do not use red and green for bad and good. The theme sets those slots to grays on purpose. Say the direction in words.
- Do not use a persimmon gradient. The theme's gradient runs mid gray to dark gray, so the lightest value still shows against white.

### Type

- Titles and big numbers: Arial Black. Everything else: Arial.
- Card numbers are persimmon, the way stat numbers are on YWCA's websites. Keep them at 24pt or larger. Smaller persimmon text on white fails contrast.
- Write page titles in capitals to match YWCA's headings. Keep them short.
- Power BI only shows fonts installed on each viewer's computer, so the web fonts in this system will not work here. Arial Black and Arial are the brand guide's approved substitutes.
- Nothing smaller than 10pt. Body and label text is black or #333333.

### Charts

- Write the title as the finding or the question. "Women who attend more finish more often" beats "Completion by engagement".
- Turn on data labels and place them outside the end of each bar, in black. Labels inside a persimmon or gray bar fail contrast.
- Turn off the legend when one series is shown.
- Mark the highlighted bar with more than color: put it first, and name that group in the title. On line charts, label each line directly.
- Start value axes at zero. Remove axis titles the chart title already covers.
- Use bars for comparing groups, lines for change over time, and cards for single numbers.
- Avoid pies, donuts, gauges, and 3D.

### Protecting small groups

Hide any count under five in pages shared outside program staff. This measure returns a blank instead of a small number. It uses the table names from the Keys of Hope data template.

```
Women (safe) =
VAR n = DISTINCTCOUNT ( Enrollments[participant_id] )
RETURN IF ( n < 5, BLANK (), n )
```

Add a text box at the bottom of the page: "Numbers under 5 are hidden to protect privacy."

### Accessibility

- Add alt text to every visual. Say the finding, not the chart type.
- Set the tab order to follow reading order: title, cards left to right, charts, table.
- Never rely on color alone. The chart title names the highlighted group.
- Give the logo image alt text: "YWCA Knoxville and the Tennessee Valley".
- Give every page and visual a title, so screen reader users can move between them.
- Check each page with Power BI's high-contrast view before sharing.

### How the web components map to Power BI

| Component | Power BI visual |
| --- | --- |
| `StatTile` | Card, with the label as its title and the context line as a subtitle |
| `HighlightBar` | Clustered bar chart with one bar set to persimmon |
| `DataTable` | Table, with no row banding and the header rule in black |
| `PrivacyNotice` | Text box at the bottom of the page |
| `SlideTitle` | A cover page: persimmon background, white Arial title at 24pt or larger, white logo bottom left |
| `Button` | Bookmark or page navigation button, persimmon fill with white bold capitals at 14pt or larger |

### The Power BI theme file

```json
{
  "name": "YWCA Knoxville (unofficial draft)",
  "dataColors": [
    "#FA4616",
    "#808080",
    "#333333",
    "#666666",
    "#000000"
  ],
  "background": "#FFFFFF",
  "foreground": "#000000",
  "tableAccent": "#FA4616",
  "good": "#333333",
  "neutral": "#808080",
  "bad": "#666666",
  "maximum": "#333333",
  "center": "#808080",
  "minimum": "#949494",
  "null": "#949494",
  "textClasses": {
    "callout": {
      "fontFace": "Arial Black",
      "fontSize": 30,
      "color": "#FA4616"
    },
    "title": {
      "fontFace": "Arial Black",
      "fontSize": 12,
      "color": "#000000"
    },
    "header": {
      "fontFace": "Arial",
      "fontSize": 11,
      "color": "#000000"
    },
    "label": {
      "fontFace": "Arial",
      "fontSize": 10,
      "color": "#333333"
    }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background": [
          {
            "show": true,
            "color": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "transparency": 0
          }
        ],
        "border": [
          {
            "show": false
          }
        ],
        "dropShadow": [
          {
            "show": false
          }
        ]
      }
    },
    "page": {
      "*": {
        "background": [
          {
            "color": {
              "solid": {
                "color": "#FFFFFF"
              }
            },
            "transparency": 0
          }
        ]
      }
    }
  },
  "firstLevelElements": "#000000",
  "secondLevelElements": "#333333",
  "thirdLevelElements": "#CCCCCC",
  "fourthLevelElements": "#666666"
}
```

## Voice and writing

From the 2018 YWCA USA brand guide, pages 20 to 26, restated in plain rules. The example sentences are invented for a Keys of Hope dashboard. They are not YWCA's.

### The tone

Bold, inspirational, authentic. Professional but easy to approach. YWCA takes clear positions on race, gender, and social justice, and it writes to connect with people, never to push them away.

### What a reader should feel

| Feeling | Staff should feel | The community should feel |
| --- | --- | --- |
| Pride | Proud to be part of this work | Proud to be part of this work |
| Solidarity | Part of something bigger | That they belong here |
| Empowerment | Important to making change happen | Able to change their own life and others' |
| Inspiration | That progress leads to more progress | Moved to act for family and community |
| Possibility | That together it can be done | That they can do this, with YWCA behind them |
| Ownership | Responsible for leading the way | Equipped with the tools to change things |

### Five ways to write

| Rule | What it means | On-brand | Off-brand |
| --- | --- | --- | --- |
| Action oriented | Active voice. Show urgency and progress. | 95 women moved into stable housing this year. | Stable housing was obtained by a number of participants. |
| Personable and personal | Pair the number with a real person's story, with her consent. | One resident finished her job training and signed a lease in March. | Employment outcomes improved across the cohort. |
| Clear and consistent | Tie each program back to the mission. Say things the same way each time. | Keys of Hope gives women a safe home while they rebuild. | The transitional housing initiative offers wraparound supports. |
| Honest and accurate | Show real results in simple words. Say what a number is out of. | 60 of 162 women who left had finished the program. | Our program has an outstanding success rate. |
| Inspirational and positive | End on hope and a clear next step. | Help the next woman find her keys. Give today. | Homelessness remains a serious problem. |

### Five habits

- Connect the work to what is happening now. History supports the story. It is not the story.
- End every piece with a call to action: advocate, take part, or donate.
- Write "YWCA", never "the YWCA". YWCA is a movement people join, not a building.
- Speak as "we" and "our work". For one association, write "YWCA Knoxville", not "the YWCA in Knoxville".
- Show before you tell. A specific success story, backed by data, beats a description of a program.

For grammar the guide does not cover, YWCA USA follows MLA style.

### Social media

| Channel | Good for | Tone | Best length |
| --- | --- | --- | --- |
| Blog | Authenticity and authority | Knowledgeable, conversational | 500 words |
| Facebook | Community and reach | Savvy, inspiring | 80 words or 250 characters |
| Twitter | Real time | Active, bold | 140 characters |
| LinkedIn | Professional and industry updates | Formal, confident | 250 characters |

These lengths are from 2018. Check them against each platform today.

## Print, slides, and other uses

How the 2018 YWCA USA brand guide applies the brand, pages 38 to 62. The guide says its templates should be used where they fit, and anything new should keep the same look. YWCA USA supplies the template files to local associations. Ask YWCA Knoxville for them before rebuilding anything here.

### The look in one paragraph

A persimmon field. A photo of a woman washed in persimmon. A huge headline in heavy capitals. One white strip with a short call to action in black. The white logo low on the page. Nothing else.

### The four building blocks

| Block | What it is | Where it appears |
| --- | --- | --- |
| Persimmon photo | A portrait or candid photo toned in persimmon, bleeding off the edges | Banners, ads, brochure cover, folder, slides |
| Heavy headline | "YWCA IS ON A MISSION" or a short phrase in heavy capitals | Everywhere |
| White strip | A white band holding a few black heavy capitals, such as "JOIN US." | Banners, ads, slides, email headers |
| Logo sign-off | The white logo bottom left, the web address in black heavy capitals beside it | Banners, ads, tote, folder |

In the guide the white strip has a torn-paper edge. That texture comes from YWCA's artwork files. Without them, use a clean white strip. See `CallToActionStrip`.

### The "ON A MISSION" graphic

YWCA USA treats "YWCA IS ON A MISSION" as a graphic with fixed arrangements. Use YWCA's artwork where you can.

| Arrangement | Use | Smallest width |
| --- | --- | --- |
| Stacked on three lines | First choice | 0.75 inch |
| One line | Where height is tight | 1.5 inches |
| Two lines | Only when the other two do not fit | 1 inch |

- On white: "YWCA" in `persimmon`, the rest in `black`.
- On persimmon: "YWCA" in `white` and the rest in `black`, or the reverse. All white over a photo.
- Spanish versions exist ("YWCA TIENE UNA MISION") with the same minimum widths.
- YWCA Knoxville's website sets the phrase as live text. `MissionHeadline` follows that.

### Slides

- Title slide: persimmon field, portrait on the right, white logo bottom left, the one-line "ON A MISSION" graphic on a white strip bottom right.
- Title in Arial Bold 44pt, white. Subtitle in Arial Regular 24pt, white.
- See `SlideTitle`.

### Stationery

- Letterhead: the stacked "ON A MISSION" graphic top right. At the foot, the persimmon logo, then the association name and address, over a persimmon bar on the bottom edge.
- Business card: one side persimmon with the graphic, one side white with the logo, name, and contacts.
- The association name is Source Sans Bold in persimmon. Contact labels (T, F, E) are persimmon. Details are black.

### Email

- Signature, top to bottom: the one-line graphic, name and title, phone and email with persimmon labels, a thin gray rule, the logo, the association name in persimmon, the address, social icons.
- Newsletter header: a persimmon banner with the white logo top left, a persimmon photo, the stacked graphic, and the issue date in black heavy capitals.

### Fact sheet

- Top left: the two-line "ON A MISSION" graphic. Top right: the persimmon logo.
- An intro paragraph in persimmon, larger than the body.
- Body and bullets in black Source Sans.
- Foot: the web address in heavy capitals on the left, the association name and address on the right.

This is the closest pattern in the guide to a printed data report. Use it for a one-page Keys of Hope summary for funders.

### Ads and banners

- Mission ads: persimmon photo, stacked white headline, a white strip with one line on what YWCA does and "JOIN US.", then the logo.
- Program ads: the same, with the strip reading "TO EMPOWER", "TO ADVANCE", or "TO STRENGTHEN" (the verb in persimmon), a two-line program name in white heavy capitals, and a white footer holding the persimmon logo with the association name.
- Building banners: persimmon, with the headline in white and black, and the white logo at the foot.

### Brochure and page layout

- A thin persimmon bar across the top of the spread.
- A full-color photo band with the white logo in its top right corner.
- The two-color headline over body text on white.
- A grid of persimmon-toned photos with short white captions.

### Social media

- Profile picture: the persimmon logo on white.
- Cover image: persimmon field, the two-line graphic, a portrait on the right.
- Posts: one word from the values in white heavy capitals over a persimmon photo.

### Folder, tote, buttons, sticker

- Persimmon ground. The stacked graphic large. White logo bottom left, web address in black heavy capitals.
- Buttons come in two kinds: white with the stacked graphic, and persimmon with the white logo.

### File formats

| Format | Use it for |
| --- | --- |
| EPS (vector) | Printers and vendors, large displays, merchandise. Scales to any size. |
| JPG, PNG | Word documents and screens. 300 dpi for print, 72 dpi for screens. Do not scale above 100%. |
| DOC, DOCX | Stationery and layouts edited in-house |
| PSD | Editing photos and pixel artwork |
| INDD, IDML | Complex print layouts |

White logos come as transparent PNG and EPS. They look empty until placed on a dark background.

## Logos

`ywca-knoxville-logo-white.svg` is YWCA Knoxville's own logo file, supplied by the team coach and unchanged. Its ink is white, so it shows only on persimmon, black, or a simple dark photo. On a white page it looks empty.

`ywca-knoxville-logo-persimmon.svg` is for white and light gray backgrounds. It was made for this system from the white file by changing the ink color to `persimmon` (#FA4616, the color on ywca.org). Nothing else changed.

YWCA Knoxville's website serves its own one-color version, `YWCA-Knoxville-Logo-Color.svg`, in a slightly redder shade (#EF4923). If YWCA staff supply an official file, use theirs and retire this one.

The files are in `assets/logos/`.
