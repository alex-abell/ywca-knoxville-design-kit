# DataTable

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
