# Candy hosting 🍭☁️

## Write-up

We can upload anything in a PHP web root, which is very dangerous, but there is a validation in place that blocks us from uploading `.php` or `.htaccess` files.

When uploading the same website twice, we can see it skips the validation on the second upload.

First upload:

```sh
[*] Validating archive ...
 [+] Archive is of type 'gzip'
 [+] Archive is smaller than 5mb when extracted
 [+] Archive only contains a single file
[*] Validating website ...
 [+] Website contains an 'index.html' file at its root
 [+] Website does not contain any disallowed files
[*] Extracting website to '/var/www/html/websites/75a6369cc918990ce067865d81809dcb' ...
 [+] index.html
[*] Done!
[*] Exit code 0
```

Second upload:

```sh
[*] Validating archive ...
 [+] Archive is of type 'gzip'
 [+] Archive is smaller than 5mb when extracted
 [+] Archive only contains a single file
[*] Validating website ...
 [+] Website has already been validated, skipping!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[*] Extracting website to '/var/www/html/websites/75a6369cc918990ce067865d81809dcb' ...
 [+] index.html
[*] Done!
[*] Exit code 0
```

Both website archives are extracted to the folder `75a6369cc918990ce067865d81809dcb` which represents the MD5 hash of the archive.

MD5 is known for having collisions using FastColl or Unicoll when the input can be controlled.

We can refer to the following [Github repository](https://github.com/corkami/collisions) for a collection of scripts to generate MD5 collisions in different file formats such as [Gzip](https://github.com/corkami/collisions?tab=readme-ov-file#gzip).

Steps (see [exploit.sh](exploit.sh) script):

- Create 2 archives, one containing an valid website and one containing a php webshell
- Use the collision script to make the hash of both archives match
- Upload the valid website
- Upload the webshell website, validation is skipped since it was already analyzed before
- Profit 😁

## Flag

`flag-684385ac3cefd18c73705c87ab7ff6ae`
