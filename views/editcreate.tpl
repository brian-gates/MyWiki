<!DOCTYPE html>
<html>
  <head>
    <title>Edit: {{pagename}}</title>
  </head>
  <body>
    <p>
      Editing: {{pagename}}
    </p>
    <div id="PageEntry">
      <form action="/edit/{{pagename}}", method="POST">
        <textarea name="PageData" rows="25" cols="100" placeholder="Enter wiki text..." required></textarea>
        <input type="Submit" value="Publish" />
      </form>
    </div>
  </body>
</html>
