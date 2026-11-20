// YWCA Knoxville design system (unofficial draft). Components are HTML and CSS patterns, not React.
// Copy the markup and styles from each component's preview. The bundle adds only Quick Escape.
declare namespace YWCAKnox {
  const version: string;
  const components: string[];
  /** Leave the site at once. Replaces the page so Back does not return to it. */
  function quickExit(url?: string): void;
  /** Wire a button to quickExit, plus three quick presses of the Shift key. */
  function bindQuickExit(button: HTMLElement | null, url?: string): void;
}
