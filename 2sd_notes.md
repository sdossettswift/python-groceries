# TWO SCOOPS OF DJANGO NOTES
## Introduction
### Twelve Factor Approach
1. Codebase : one codebase tracked in revision control, many deploys
1. Dependencies: Explicity declare and isolate dependencies
1. Config: Store config in the environment
1. Backing Services: Treat backing services as attached resources
1. Build, Release, Run: Strictly separate build nad run stages
1. Processeses: Execute the app as one or more stateless processes
1. Port Binding: Export services by port binding
1. Concurrency: Scale out via process method
1. Disposability: maximize robustness w/ fast startup, graceful shutdown
1. Dev/Prod Parity: Keep development, staging, and production as similar as possible
1. Logs: Treat logs as event streams
1. Admin Processes: Run admin/mgmt tasks as one-off processes

## Coding Style
### Make Code Readable 
- Avoid abbreviating variable names
- write out function argument names
- document classes and methods
- comment code
- refactor code into resuable functions & methods
- keep things short
### Style Guide: PEP 8 
- 4 spaces per indentation level
- separate top-level function and class definitions by 2 blank lines
- separate method definitions inside a class w/ 1 blank line
- Flake 8 as a linter (installed!)
- 79-charachter limit  - safe for text-wrapping editors 
### Importing
- Per PEP8, the order for importing is:
1. standard library imports
1. Django core 
1. related third-party imports
1. local application/library specific imports
- Make sure to import explicit relative imports as opposed to hardcoded imports 
   bad:  ``from cones.models import WaffleCone``
   good: ``from .models import WaffleCone``
- Void using `import *`, instead, import everything explicitly, i.e., `from django import forms`, `from django.db import models` 
### Underscores >> Dashes
- use underscores over dashes, it is the python way
	- urls
	- template block names
### Other Style Guides
1. idiomatic.js(https://github.com/rwaldron/idiomatic.js/) 
1. pragmatic.js(https://github.com/madrobby/pragmatic.js)
1. airbnb js styleguide(https://github.com/felixge/node-style-guide)
1. idiomatic css(https://github.com/necolas/idiomatic-css)
1. code guide for html & css (http://codeguide.co)

## Setting Up Django Environment 
### Use same db everywhere
- Makes life easier
- Deal w/ the same constraints everywhere
- PostgreSQL works well for development, production, staging, etc. 
- Fixtures aren't a cureall to abstract differences away for different production/development dbs
- PIP - python package index - manages installation of python packages
- Virtualenv - creates isolated python environments to manage dependencies, etc. 
- Use a virtualenvwarpper to activate virtual environment (http://virtualenvwrapper.readthedocs.io/en/latest/)
### Next Level:
1. Using Isolated Docker Containers
1. Vagrant and VirtualBox
1. Identical Environments

1. 

