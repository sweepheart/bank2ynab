# created for Issue #176 based on 
# https://packaging.python.org/tutorials/distributing- \
# packages/#configuring-your-project

# Package meta-data:
NAME = "bank2ynab"
DESCRIPTION = "Convert CSV from various banks' export formats into " \
        "YNAB's import format."
LONG_DESCRIPTION = "A common project to consolidate all conversion efforts " \
        "from various banks' export formats into YNAB's import format."
URL = "https://github.com/torbengb/bank2ynab"
EMAIL = "torben@g-b.dk"
AUTHOR = "https://github.com/torbengb/bank2ynab/graphs/contributors"
KEYWORDS = "ynab bank bank-statement conversion-efforts credit-card" \
        "transactions converter ynab-converter ynab-format money csv" \
        "bank-format conversion conversion-utility"
VERSION = "1.0.0.dev201803020943"

# define the version numbers:
# !! See also: https://github.com/torbengb/bank2ynab/wiki/VersionNumbers !!
# version_major = 1  # must be integer
# version_minor = 0  # must be integer
# version_patch = 1000003  # must be integer
# version_suffix = "feature-176-pypi-installer"
# I'd like the suffix to *automagically* include the GitHub branch name,
# but that will have to be a separate enhancement, see Issue #180.

# only add the suffix to the patch level if it's not empty 
# and not a master release:
# if (version_suffix != "") and (version_suffix != "master"):
#    version_patch = version_patch + '-' + version_suffix
## NOT ALLOWED: VERSION NUMBER MUST BE ONLY DIGITS and . and _ and -.

# version number according to
# https://codereview.stackexchange.com/a/131490 :
# version_info = (version_major, version_minor, version_patch)
# VERSION = '.'.join(str(c) for c in version_info)

# Apparently, version numbers must follow this format:
# [N!]N(.N)*[{a|b|rc}N][.postN][.devN]
# sources:
# https://packaging.python.org/tutorials/distributing-packages/#standards- \
# compliance-for-interoperability
# https://www.python.org/dev/peps/pep-0440/#public-version-identifiers
# Notes:
# Hyphens are not allowed! That's unfortunate, as the branches contain them.
