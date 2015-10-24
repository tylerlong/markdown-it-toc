from fabric.api import local


def compile():
    local('browserify index.js -s markdownitTOC > dist/markdown-it-toc.min.js')


def copy():
    local('cp dist/markdown-it-toc.min.js ~/src/js/markdown-core/vendor/markdown-it-toc/dist/markdown-it-toc.min.js')
