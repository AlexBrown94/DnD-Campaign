#!/bin/bash

# Directory containing Markdown files
MARKDOWN_DIR="C:/Users/alexd/Git/quartz/content"

# Python script for preprocessing Markdown
PREPROCESS_SCRIPT="C:/Users/alexd/Git/quartz/content/gm-format.py"

# Path to Python interpreter
PYTHON="python"

# Run preprocessing script on Markdown files
$PYTHON "$PREPROCESS_SCRIPT" "$MARKDOWN_DIR"

# Run "nxp quartz sync" command
nxp quartz sync