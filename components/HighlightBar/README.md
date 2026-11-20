# HighlightBar

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
