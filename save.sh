#!/bin/bash

isort .
black --skip-string-normalization --line-length 120 .

git add . -A \
&& git commit -m 'Another day, another puzzle' \
&& git push