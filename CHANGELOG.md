# Changelog

All notable changes to this project will be documented in this file.


## [0.0.2] - 2023-07-18

### Fixed
- toolbox-export not working on Debian because of shebang (/bin/sh is not the same as /bin/bash on Debian)

## [0.0.1] - 2023-06-04

### Added
- shell script toolbox-export, based on distrobox-export
- option --container/-c _toolbox_name_
- prevent hosts's root from starting binaries in a toolbox container
- man page toolbox-export.1

### Removed
- short options -el, -ef, -ep
- support for rootful containers
