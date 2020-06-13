#!/bin/bash

xgettext --language=Python --from-code=UTF-8 --keyword=_ --output=encadra.pot `find ~/dev/encadra/src/ -name "*.py"`

exit 0


