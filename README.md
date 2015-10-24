# markdown-it-toc

Table of contents plugin for [markdown-it](https://github.com/markdown-it/markdown-it).


## Install

```
bower install markdown-it-toc
```


## Use (in browser)

```javascript
var md = window.markdownit();
md = md.use(window.markdownitTOC);
console.log(md.render('# test\n\n[TOC]\n\n## something'));
```
