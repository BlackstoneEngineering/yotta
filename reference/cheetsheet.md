---
layout: default
title: ARMmbed yotta cheat-sheet
byline: yotta is the open source modular orchestrator that facilitates building mbedOS and other embedded projects. This cheat sheet summarizes commonly used yotta command line instructions for quick reference.
leadingpath: ../
---

{% capture colOne %}
## Install yotta
### Manually
`pip install -U yotta`

### Required Packages
- cmake
- ninja
- python 2/3
- arm-gcc

### Instructions
Install playlist: [YouTube playlist](https://goo.gl/cJT1tO)
#### yotta for Linux 
[yottadocs.mbed.com/#installing-on-linux](yottadocs.mbed.com/#installing-on-linux)

#### yotta for OS X
[yottadocs.mbed.com/#installing-on-osx](http://yottadocs.mbed.com/#installing-on-osx)

#### yotta for Windows
[yottadocs.mbed.com/#installing-on-windows](http://yottadocs.mbed.com/#installing-on-windows)

## Modules
There are two types of modules, executable and library.

### Library Modules
Library modules are re-usable code modules such as network stacks, drivers, API's... etc. Library modules can be found on the yotta registry and are meant to be shared and re-used.

#### Creating Library Modules
YouTube : [insert youtube video](TODO)

### Executable Modules
Executable modules compile into a binary. Executable modules should **not** be published to the yotta registry, instead they should published on github or other scm tools.

#### Creating Executable Modules
YouTube:
[build from scratch](https://www.youtube.com/watch?v=qYgHSZbl0RE&index=4&list=PLiVCejcvpsevVVpgdIo4QxSl563ToLOIB),
[clone from existing repo](https://www.youtube.com/watch?v=gay1Jy6lMkQ&index=5&list=PLiVCejcvpsevVVpgdIo4QxSl563ToLOIB)

{% endcapture %}
<div class="col-md-6">
{{ colOne | markdownify }}
</div>


{% capture colTwo %}

## yotta Registry

`yotta search ___` - search online registry of library modules and targets.

`yotta search --limit 1000` - get more results from the registry

## Library Modules

`yotta search module <moduleName>` - search registry for modules

`yotta install <moduleName>` - install module as dependency


## Targets
Targets specify hardware specific compiler settings.

`yotta search target <targetName>` - search the online registry for targets.

`yotta target <targetName>` - set the target for the current yotta module.

`yotta target `**`--global`**` <targetName>` - set a global target for all yotta project on system. 

## Tests
```./tests/``` - tests folder


## [Semantic Versioning](semver.org)
Major.Minor.Patch
Major - breaking API changes
Minor - backwards compatible API changes
Patch - minor bug fixes, works the same way, just better.

**Note:** A major number of `0.x.y` indicated the module is not realy for public consumption and can change at any time, it is reccomended to start here and `yotta version major` to `1.x.y` when the module is ready for public release.

## Publishing to Registry
Library modules only!!!

```yotta publish``` - publish current module to registry

```yotta version <major/minor/patch>``` - Incriment the major, minor or patch version number respectively 


{% endcapture %}
<div class="col-md-6">
{{ colTwo | markdownify }}
</div>
<div class="clearfix"></div>

---

{% capture colThree %}

## Super Ultra Handy Commands

`yt` - Shorthand for `yotta`


```yotta build``` - Build the project.


```yotta clean``` - Wipe the project clean and start fresh, clean all temp build files.


```yotta debug``` - Lauch the GDB debugger


```yotta update``` - Update a module(s) to the latest revision


```yotta outdated``` - Check if module is out of date and has updates. 


{% endcapture %}
<div class="col-md-6">
{{ colThree | markdownify }}
</div>

{% capture colFour %}

## Other cool tools we do

### Greentea
An awesome testing framework for mbed-enabled boards

### PyOCD
Are you OCD about debugging and love Python? Then PyOCD is for you!

### PyGen
An awesome series of python scripts used to generate project files for various IDE's. Open source and welcoming contributions! Have an IDE you like and we don't? Submit a PR and get it added today!

{% endcapture %}
<div class="col-md-6">
{{ colFour | markdownify }}
</div>
