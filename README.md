# File Playground

This repository is a personal scripting playground for working with non-image file types using Python.

It contains small, focused scripts that handle file system operations, file transformations, and automation tasks. The goal of this repo is to practice practical Python scripting, working with real file formats, and building simple command-line tools.

Some scripts are inspired by exercises from the Zero To Mastery Python course, but the code here reflects my own implementations, adaptations, and extensions based on reading documentation and experimenting independently.

---

## Current Scripts

### PDF Watermark Script

A command-line utility that applies a watermark to PDF files in a directory.

**What it does:**

* Takes a PDF file to use as a watermark
* Processes all PDF files in an input directory
* Applies the watermark beneath the existing page content
* Writes the watermarked PDFs to a separate output directory
* Keeps original filenames for the output files
* Overwrites existing files in the output directory if they already exist
* Skips files that cannot be processed as PDFs and reports them in the terminal

---

## Usage

Run the script from the command line with three arguments:

```
python pdf_watermark.py <watermark.pdf> <input_directory> <output_directory>
```

Example:

```
python pdf_watermark.py watermark.pdf input_pdfs output_pdfs
```

The input directory is expected to contain PDF files only. The output directory will be created automatically if it does not exist.

---

## Purpose of This Repository

* Practice Python scripting and automation
* Work with non-image file formats such as PDFs
* Learn file system traversal and batch processing
* Build simple, reusable command-line tools
* Experiment and improve scripts over time

This repository is expected to grow as additional file-handling scripts are added.

---

## Requirements

* Python 3
* pypdf

---

## Notes

* This is a learning-focused repository.
* Scripts prioritize clarity and correctness over advanced abstractions.
* Course material from Zero To Mastery is used as a reference, but code is written and adapted independently.
