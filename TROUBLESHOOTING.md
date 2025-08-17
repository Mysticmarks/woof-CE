# Troubleshooting

Common issues and quick fixes:

- **Missing packages**: Ensure build dependencies such as `debootstrap`, `xorriso` and `zstd` are installed. The CI workflow shows the full list.
- **Permission errors**: Many scripts expect to run as root. Use `sudo` where appropriate.
- **Failed downloads**: Check your network connectivity and the URLs in `DISTRO_COMPAT_REPOS-*` files. Mirrors sometimes change.
- **Stale output directories**: Remove any existing `woof-out_*` directories before starting a new build to avoid contamination from previous runs.

For more help, consult the project wiki or open an issue with detailed logs.
