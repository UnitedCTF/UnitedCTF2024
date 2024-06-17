<?php
require_once("./partials/header.php");
?>

<p>
<div style="font-size: 2em">Tired of the normal plain white cloud? Host your website directly into our cotton candy powered servers!</div>
</p>
<p>
<div>How to use:
  <div class="bullet">Create a static website containing an 'index.html' file</div>
  <div class="bullet">Compress it into a '.tar.gz' archive (use the command 'tar -czf website.tar.gz .' in linux)</div>
  <div class="bullet">Upload it using the button below</div>
  <div class="bullet">Share your new website with your friends!</div>
</div>
</p>

<form action="upload.php" method="post" enctype="multipart/form-data">
  Select a website archive to upload:
  <input type="file" accept=".tgz,.tar.gz" name="website" onchange="document.forms[0].submit()">
</form>

<p>
<div style="font-size: 0.5em">DISCLAIMERS:
  <div class="bullet">Uploaded websites are deleted after 1 hour, reupload it before then to keep it alive.</div>
  <div class="bullet">We are not responsible of any side effects happening for hosting a website on our platform.</div>
</div>
</p>

<?php
require_once("./partials/footer.php");
?>