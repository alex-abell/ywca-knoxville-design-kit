# Power BI

Import `assets/power-bi/ywca-knoxville-theme.json` first. It sets the colors and fonts below so nobody has to pick them by hand. It has not been tested in Power BI Desktop yet.

## Page

- Use the 16:9 canvas at 1280 by 720.
- Keep a 24px margin on every side (`space-4`). Snap visuals to an 8px grid (`space-2`).
- Keep the page white. No background images, no shadows, no rounded visual borders.
- Put the YWCA Knoxville logo top left, at least 100px wide, with nothing crowding it. The white logo needs a persimmon or black strip behind it.
- Give each page one job and name it in the page title: "WHO WE SERVE", "ENGAGEMENT", "OUTCOMES".

## Layout of a page

| Zone | What goes there |
| --- | --- |
| Top strip | Logo, page title, the date the data was last refreshed |
| Row one | Up to four cards, each one number with its label |
| Middle | One or two charts that answer the page's question |
| Bottom | A plain table for detail, and the privacy note |
| Left or top | Slicers for period and program. Keep them the same on every page. |

## Color

- The first data color is persimmon (#FA4616). Use it for the one bar or line that carries the point.
- Recolor every other series gray. In a bar chart, set the default color to #808080 and use conditional formatting to turn the highlighted bar #FA4616.
- Every data color in the theme is at least 3:1 against white, so marks stay visible. Do not add light grays as series colors.
- Do not use red and green for bad and good. The theme sets those slots to grays on purpose. Say the direction in words.
- Do not use a persimmon gradient. The theme's gradient runs mid gray to dark gray, so the lightest value still shows against white.

## Type

- Titles and big numbers: Arial Black. Everything else: Arial.
- Card numbers are persimmon, the way stat numbers are on YWCA's websites. Keep them at 24pt or larger. Smaller persimmon text on white fails contrast.
- Write page titles in capitals to match YWCA's headings. Keep them short.
- Power BI only shows fonts installed on each viewer's computer, so the web fonts in this system will not work here. Arial Black and Arial are the brand guide's approved substitutes.
- Nothing smaller than 10pt. Body and label text is black or #333333.

## Charts

- Write the title as the finding or the question. "Women who attend more finish more often" beats "Completion by engagement".
- Turn on data labels and place them outside the end of each bar, in black. Labels inside a persimmon or gray bar fail contrast.
- Turn off the legend when one series is shown.
- Mark the highlighted bar with more than color: put it first, and name that group in the title. On line charts, label each line directly.
- Start value axes at zero. Remove axis titles the chart title already covers.
- Use bars for comparing groups, lines for change over time, and cards for single numbers.
- Avoid pies, donuts, gauges, and 3D.

## Protecting small groups

Hide any count under five in pages shared outside program staff. This measure returns a blank instead of a small number. It uses the table names from the Keys of Hope data template.

```
Women (safe) =
VAR n = DISTINCTCOUNT ( Enrollments[participant_id] )
RETURN IF ( n < 5, BLANK (), n )
```

Add a text box at the bottom of the page: "Numbers under 5 are hidden to protect privacy."

## Accessibility

- Add alt text to every visual. Say the finding, not the chart type.
- Set the tab order to follow reading order: title, cards left to right, charts, table.
- Never rely on color alone. The chart title names the highlighted group.
- Give the logo image alt text: "YWCA Knoxville and the Tennessee Valley".
- Give every page and visual a title, so screen reader users can move between them.
- Check each page with Power BI's high-contrast view before sharing.

## How the web components map to Power BI

| Component | Power BI visual |
| --- | --- |
| `StatTile` | Card, with the label as its title and the context line as a subtitle |
| `HighlightBar` | Clustered bar chart with one bar set to persimmon |
| `DataTable` | Table, with no row banding and the header rule in black |
| `PrivacyNotice` | Text box at the bottom of the page |
| `SlideTitle` | A cover page: persimmon background, white Arial title at 24pt or larger, white logo bottom left |
| `Button` | Bookmark or page navigation button, persimmon fill with white bold capitals at 14pt or larger |
