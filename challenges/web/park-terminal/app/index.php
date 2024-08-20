<?php
  session_start();

  function list_dir($dir) {
    if (is_dir($dir)) {
      if ($dh = opendir($dir)) {
        while(($file = readdir($dh)) !== false) {
          if ($file != '.' && $file != '..') {
            $filepath = $dir . '/' . $file;

            if ($file[0] == '.' && !is_admin()) {
              continue;
            }

            echo '<tr>';
            if (is_dir($filepath)) {
              echo '<td style="text-align: left;"><a href="?path=' . urlencode($filepath) . '">' . htmlspecialchars($file) . '/</a></td>';
            } else {
              echo '<td style="text-align: left;">' . htmlspecialchars($file) . '</td>';
            }
            echo '<td>' . filesize($filepath) . '</td>';
            echo '</tr>';
          }
        }
      }
    }
  }
  
  function is_admin() { return isset($_SESSION['user_role']) && $_SESSION['user_role'] == 'admin'; }


  $is_admin = is_admin();
  
  if (isset($_GET['path'])) {
    $path = $_GET['path'];
  } else {
    $path = 'maintenance';
  }
  
?>


<!DOCTYPE html>
<html lang="en" class="tui-bg-blue-black">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>United CTF 2024</title>

    <link rel='stylesheet' href='https://vinibiavatti1.github.io/TuiCss/dist/tuicss.min.css'>
</head>
<body class='center' style="padding: 50px;">
    <h3>UNITED CTF 2024</h3>
    <div class='tui-window' style='text-align: center;'>
        <fieldset class='tui-fieldset'>
            <legend class="center"><?php echo $path;?></legend>
            <table class='tui-table hovered-cyan' style='width: 700px; margin-bottom: 20px;'>
                <thead>
                    <tr>
                        <th>Fichier</th>
                        <th>Taille</th>
                    </tr>
                </thead>
                <tbody>
                  <?php list_dir($path); ?>
                </tbody>
            </table>
              
              <a class='tui-button ' href="?path=<?php echo urlencode(dirname($path)) ?>">←</a>
        </fieldset>
    </div>
    <p>
        service de maintenance
    </p>
</body>
</html>
