Lampy
======


Naming conventions for the Repo:
--------------------------------
1. Packages/Directores: all lowercase with no underscores
2. Modules/files:       all lowercase with underscores for readability
3. Classes:             UpperCamelCase
4. Functions:           all lowercase with underscores for readability
5. Variables:           lowerCamelCase
5. Private functions/variables: leading underscore
6. Constants:           ALL_CAPS

DEMO BRANCH: 

This branch runs a brief demo of Lampy's basic functionality.
Alarms are triggered as usual, but the behavior of the 'MINUTE'
button outside of SET ALARM MODE has been overwritten to update
the morning alarm time to the current clock time. The evening
alarm has likewise been set to one minute after the morning alarm
rather than 9 hours prior. Lamp bulb transition times have been
reduced to facilitate quicker demonstration.

Changes made in this branch WILL affect the intended standard be-
havior of the system. As such, this branch SHOULD NOT be merged into
Master. If major updates or changes to the code are made, the changes
should instead only be pulled into this branch.
