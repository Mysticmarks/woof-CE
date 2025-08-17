# kernel-kit

Tools and configuration snippets for building Puppy Linux kernels.

## Key files
- `build.sh` – entry point for compiling a kernel using the selected `*build.conf` file.
- `configs_*` – default kernel configuration fragments for each architecture.
- `patches/` – optional patch sets applied during kernel compilation.

To build a kernel, adjust the appropriate `*-build.conf` file and run:
```bash
./build.sh
```
