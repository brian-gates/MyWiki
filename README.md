# MyWiki
Yet another Wiki. Apparently the world does not have enough of them.

MyWiki (To be renamed at a later point) is/will be a Python based wiki utilizing the Bottle microframework.

Requirements:
Bottle (pip install bottle)
Python 2.x (originally built with 2.7.12)



Goals/Features:
  • Small/fast Python wiki implementation
  • Fully configurable via CSS (look/feel) and config (behavior)
  • Media upload
  • Search and backtrace
  • Custom scripting for edits, avoiding the CamelCase link style of monkey-wiki in favor of a more robust naming convention
  • Easy end user set-up (drag and drop w/ optional local server)
  • Using Bottle's routing feature to create a fast and robust page creation method

Current functionality:
  • Detect the existence of pages
  • Go to create/edit for pages that do not yet exist
