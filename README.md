# MyWiki
Yet another Wiki. Apparently the world does not have enough of them.

MyWiki (To be renamed at a later point) is/will be a Python based wiki utilizing the Bottle microframework.

Requirements:
Bottle (pip install bottle)
Python 2.x (originally built with 2.7.12)



Goals/Features:
<ul>
  <li>Small/fast Python wiki implementation</li>
  <li>Fully configurable via CSS (look/feel) and config (behavior)</li>
  <li>Media upload</li>
  <li>Search and backtrace</li>
  <li>Custom scripting for edits, avoiding the CamelCase link style of monkey-wiki in favor of a more robust naming convention</li>
  <li>Easy end user set-up (drag and drop w/ optional local server)</li>
  <li>Using Bottle's routing feature to create a fast and robust page creation method</li>
 </ul>

Current functionality:
<ul>
  <li>Detect the existence of pages</li>
  <li>Go to create/edit for pages that do not yet exist</li>
 </ul>
