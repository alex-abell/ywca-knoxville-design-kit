# SiteFooter

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
