from fabric.api import local


def compile():
    local('browserify index.js -s markdownitTOC > markdown-it-toc.min.js')
    copy()

def copy():
    local('cp markdown-it-toc.min.js ~/src/js/markdown-core/')
