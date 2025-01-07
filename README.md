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

## Renovate

```bash
npx renovate --platform=local
```

## Resources

- <https://hobo.house/2017/09/03/automate-rpm-builds-from-git-sources-using-copr/>
