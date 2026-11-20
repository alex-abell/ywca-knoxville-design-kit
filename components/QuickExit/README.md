# QuickExit

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
