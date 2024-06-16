#!/bin/bash
# Requires both tar and 7z
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "[!] Missing website"
  exit 1
fi

OUT_FOLDER_PREFIX="${OUT_FOLDER_PREFIX:-/var/www/html/websites}"
TEST_FOLDER_PREFIX="${TEST_FOLDER_PREFIX:-/tmp/website-extractor}"

TARGZ="$1"
if [ ! -f "$TARGZ" ]; then
  echo "[!] Website archive '$TARGZ' not found"
  exit 1
fi

echo "[*] Validating archive ..."
if [ "$(file -b --mime-type "$TARGZ")" != "application/gzip" ]; then
  echo " [!] Archive is not of type 'gzip'"
  exit 1
fi
echo " [+] Archive is of type 'gzip'"

METADATA=$(7z l "$TARGZ" | tail -n +11)
FILES=$(tail -n +5 <<<"$METADATA" | sed -E 's/^.{26}//g')
read FILE_SIZE FILE_COMPRESSED FILE_NAME _ < <(tail -n3 <<<"$FILES" | head -n1 | tr -s " ")
read TOTAL_SIZE TOTAL_COMPRESSED TOTAL_COUNT _ < <(tail -n1 <<<"$FILES" | tr -s " ")

if [ "$TOTAL_SIZE" -gt 5242880 ]; then
  echo " [!] Archive is bigger than 5mb when extracted"
  exit 1
fi
echo " [+] Archive is smaller than 5mb when extracted"

if [ "$TOTAL_COUNT" -ne 1 ]; then
  echo " [!] Archive contains more than one file"
  exit 1
fi
echo " [+] Archive only contains a single file"

MD5SUM=$(md5sum "$TARGZ" | cut -d" " -f1)
OUT_FOLDER="${OUT_FOLDER_PREFIX}/${MD5SUM}"
echo "[*] Validating website ..."
if [ ! -d "$OUT_FOLDER" ]; then
  TEST_FOLDER="${TEST_FOLDER_PREFIX}/${MD5SUM}"
  trap "rm -rf \"$TEST_FOLDER\"" EXIT

  7z x "$TARGZ" -so "$FILE_NAME" | \
    7z x -aoa -si -ttar -o"$TEST_FOLDER" >/dev/null

  if [ ! -f "${TEST_FOLDER}/index.html" ]; then
    echo " [!] Website does not contain an 'index.html' file at its root"
    exit 1
  fi
  echo " [+] Website contains an 'index.html' file at its root"

  if [ $(find "${TEST_FOLDER}" \( -type l \) -or \( -type f -and \( -iname "*.php" -or -iname ".htaccess" \) \) | wc -l) -ne 0 ]; then
    echo " [!] Website contains disallowed files"
    exit 1
  fi
  echo " [+] Website does not contain any disallowed files"
else
  echo " [+] Website has already been validated, skipping!"
fi

echo "[*] Extracting website to '$OUT_FOLDER' ..."
mkdir -p "$OUT_FOLDER"
tar xzvf "$TARGZ" -C "$OUT_FOLDER" | \
  while read line; do echo " [+] $line"; done

echo "[*] Done!"
