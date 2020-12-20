[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Plingo

_An image says more than 1.000 commands_

## Introduction

**Plingo** is a programming language made for pixel-based image manipulation. Its main goal is to omit writing text based code so it uses the image itself as the program.

Each pixel of the inpupt image is a command with up to two parameters. Each command gets executed and thereby modifies a copy of the image creating a new image. So the source image is the input data and the code ifself.

For more details see the [github page](https://github.com/fezde/plingo).

## Short tutorial
```shell
pip install Plingo
plingo yourimage.png
```
Now check the result at `yourimage.png_out.png`
