#!/bin/bash

# easier on the eyes:
clear
# reuse this function:
get_input ()
{ if [ -z "$2" ] # Is parameter #2 zero length?
  then
    echo "I didn't get 2 parameters. Exiting." ; echo "" ; exit
  else
    while true; do
      read -p "$1 Press 'Y' to continue, or any other key to skip: " -n 1 response
      case $response in
        [Yy]* ) 
          $2
          result=$?
          if [ $result -eq ""0"" ]; then 
            echo "" ; echo "--OK--" ; echo ""
            break
          else
            echo "" ; echo "An error occurred: " $result ". Exiting!" ; echo ""
            exit
          fi
          ;; # yes I know that 'break' is never going to run, but it feels proper to have it there.
        *     ) echo "" ; echo "Nothing done."; echo "" ; break;;
      esac
    done
  fi
}

# do the actual work:

# remove old build files:
if [ -f "dist/*" ] 
then rm dist/*
fi

get_input "Are you ready to BUILD the package?" "python setup.py bdist_wheel"

get_input "Are you ready to UPLOAD the package?" "twine upload -u bank2ynab_username --repository-url https://test.pypi.org/legacy/ dist/*"
if [ $response == ""y"" ]
then echo "Package will be listed at https://test.pypi.org/project/bank2ynab/#history in a few minutes." ; echo ""
fi

get_input "Wait 2 minutes and install new build?" " "
if [ $response == ""y"" ]; then
  echo "Removing..." ; echo ""
  sudo -H pip uninstall -y bank2ynab
  echo "Waiting, then installing..."
  sleep 120
  sudo -H pip install --no-cache-dir --index-url https://test.pypi.org/simple/ bank2ynab
fi
