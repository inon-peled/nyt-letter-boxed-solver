"""

List of English words was extracted from
https://dumps.wikimedia.org/enwiktionary/20231201/enwiktionary-20231201-pages-articles-multistream-index.txt.bz2
via
```cat ./enwiktionary-20231201-pages-articles-multistream-index.txt |
    cut -f3 -d:
    | grep -E '^[a-z]*$'
    > ./only_small_caps.csv
```
"""
