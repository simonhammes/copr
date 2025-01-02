# COPR

## Prerequisites

- distrobox

## Instructions

```bash
# Setup
distrobox create fedora --image fedora:41
distrobox enter fedora
sudo dnf install rpmdevtools

spectool -Rg $FILE
rpmbuild -ba $FILE
```
