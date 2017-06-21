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

