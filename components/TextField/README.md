# TextField

A labeled text input for forms on a white page.

You provide: the label, the input type, a hint if the format is not obvious, and the error message if there is one.

- The label sits above the field and is always visible. No placeholder-only fields.
- Put the expected format in a hint between the label and the field.
- Square corners, 48px tall. The border is 2px `gray-60`, which stands out against white at 5.7:1.
- Show an error with a 4px black border and a message that starts with "Error:" and says how to fix it. Do not use red. Mark the field invalid and tie the message to it, so screen readers announce both. When the message appears after the page has loaded, give it `role="alert"`.
- Set the autofill type for names, emails, and phone numbers.
- On a black band, use the white-outlined field in `NewsletterBand`.
