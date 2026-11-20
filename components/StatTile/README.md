# StatTile

One big persimmon number with a bold label and a line of context, as in the stats row on ywcaknox.com.

You provide: a value, a label, and a context line.

- The number is `stat` in `persimmon`. The label is `stat-label` in `ink`. The context line is `small` in `ink-muted`.
- Number, label, and context sit in one paragraph, so a screen reader reads them as one statement.
- The context line is required. A percentage always says what it is out of.
- Three or four across, centered. They stack on phones.
- If the count behind a tile is under five, show "Fewer than 5" instead of the number.
- Do not animate the number counting up.
