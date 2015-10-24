from fabric.api import local


def compile():
    local('browserify index.js -s markdownitTOC > dist/markdown-it-toc.js')
    local('uglifyjs --compress -- dist/markdown-it-toc.js > dist/markdown-it-toc.min.js')
    local('rm -rf dist/markdown-it-toc.js')


def copy():
    local('cp dist/markdown-it-toc.min.js ~/src/js/markdown-core/vendor/markdown-it-toc/dist/markdown-it-toc.min.js')
