#!/bin/bash

set -e

isort .
black --skip-string-normalization --line-length 120

git add . -A \
&& git commit -m 'Another day, another puzzle' \
&& git push