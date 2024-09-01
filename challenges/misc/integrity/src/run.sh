#!/bin/bash


gcp() {
  local message="$1"

  git add .
  git add .
  GIT_AUTHOR_NAME="Marc" \
  GIT_AUTHOR_EMAIL="Marc@coaster.com" \
  GIT_COMMITTER_EMAIL="Marc@coaster.com" \
  GIT_COMMITTER_NAME="Marc" \
  git commit -m "$message"
}


cleanup_folder() {
  local folder="$1"

  rm -rf $folder

  mkdir $folder
  cd $folder

  git init
}

setup_chal() {
  echo "$(sed 's/MESSAGE/0/g' '../templates/readme.md')" > readme.md  
  gcp "Init"

  echo "$(cat ../templates/hash.py)" >> hash.py
  gcp "Script génération intégrité"

  for ((i=1; i <=763;i++)); do
    sed "s/MESSAGE/$i/g" '../templates/readme.md' > readme.md
    hash_value=$(md5sum "readme.md" | awk '{ print $1 }')

    if [ "$i" == "117" ]; then
      hash_value="3c2234a7ce973bc1700e0c743d6a819c"
    fi

    gcp "Update of view count $hash_value"
  done
}

cleanup_folder "integrity"
setup_chal

cd ..
zip -r integrity.zip  integrity
rm -rf integrity
