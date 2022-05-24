from panflute import *
from sys import stderr

allHeaders = []


def existingHeaderFilter(item, _):
    if isinstance(item, Header):
        if stringify(item) in allHeaders:
            print('Header already exists: ' + stringify(item), file=stderr)
        else:
            allHeaders.append(stringify(item))


def headerByLevelFilter(item, _):
    if isinstance(item, Header) and item.level > 2:
        return Header(Str(stringify(item).upper()), level=item.level)


def boldify(document):
    document.replace_keyword('BOLD', Strong(Str('BOLD')))


if __name__ == "__main__":
    run_filters([existingHeaderFilter, headerByLevelFilter], prepare=boldify)