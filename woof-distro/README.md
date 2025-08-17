# woof-distro

Configuration data describing supported distributions and architectures.

Each architecture directory (e.g., `x86_64/ubuntu/jammy64`) contains:
- `DISTRO_SPECS` and related files defining repositories and package selections.
- `Packages-*` lists enumerating available Puppy packages.

`merge2out` uses these directories to generate a `woof-out_*` build tree.
