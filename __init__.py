"""created for Issue #176 based on 
https://packaging.python.org/tutorials/distributing-packages/
#configuring-your-project
"""

# Package meta-data:
NAME = "bank2ynab"
DESCRIPTION = "A common project to consolidate all conversion efforts " \
        "from various banks' export formats into YNAB's import format."
LONG_DESCRIPTION = "A common project to consolidate all conversion efforts " \
        "from various banks' export formats into YNAB's import format."
URL = "https://github.com/torbengb/bank2ynab"
EMAIL = "torben@g-b.dk"
AUTHOR = "https://github.com/torbengb/bank2ynab/graphs/contributors"
KEYWORDS = "ynab bank bank-statement conversion-efforts credit-card" \
        "transactions converter ynab-converter ynab-format money csv" \
        "bank-format conversion conversion-utility"

# define the version numbers:
# !! See also: https://github.com/torbengb/bank2ynab/wiki/VersionNumbers !!
version_major = 1  # must be integer
version_minor = 0  # must be integer
version_patch = "0"  # must be string
version_suffix = "feature-176-pypi-installer"
# I'd like the suffix to *automagically* include the GitHub branch name,
# but that will have to be a separate enhancement, see Issue #180.

# only add the suffix to the patch level if it's not a master release:
if version_suffix != "master":
    version_patch = version_patch + '-' + version_suffix

# version number according to
# https://codereview.stackexchange.com/a/131490 :
version_info = (version_major, version_minor, version_patch)
VERSION = '.'.join(str(c) for c in version_info)
