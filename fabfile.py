from fabric.api import local


def compile():
    local('browserify index.js -s markdownitTOC > dist/markdown-it-toc.min.js')
