# woof-code

Core build scripts executed to assemble a Puppy Linux distribution.

## Workflow
1. `0setup` – prepare package repositories and resolve compatibility files.
2. `1download` – fetch upstream packages and sources.
3. `2createpackages` – generate Puppy-compliant packages.
4. `3builddistro` – assemble the final ISO/SFS artifacts.

Each script should be run in sequence inside a `woof-out_*` directory produced by `merge2out`.
