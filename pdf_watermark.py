"""
Applies a watermark to PDF files in a directory and writes the results to a new directory.

This script is designed to be run from the command line and expects three arguments:
1) A PDF file used as the watermark
2) A directory containing PDF files to apply the watermark to
3) A destination directory where the output PDF files will be saved

The input directory is expected to contain only PDF files. Any files that cannot
be opened or processed as PDFs are skipped and reported in the terminal.

Each output file keeps the original filename and is written to the destination
directory. If a file with the same name already exists in the output directory,
it is overwritten. This behavior is intentional, as the script is meant to write
into a dedicated output folder.

The watermark is applied beneath the existing page content.
"""
import sys
import os
import pypdf


def add_watermark(watermark_file, pdf_files, output_directory):
    """
    Adds a watermark to a list of PDF files and writes the results to an output directory.

    The function reads the first page of the watermark PDF and applies it beneath
    the existing content of every page in each input PDF. Each processed PDF is
    written to the output directory using the original filename.

    Files that cannot be opened or processed as PDFs are skipped, and an error
    message is printed to the terminal.

    Args:
        watermark_file (str): Path to the PDF file used as the watermark.
        pdf_files (list[str]): List of file paths to PDF files to be watermarked.
        output_directory (str): Path to the directory where output PDFs are saved.
    """
    watermark = pypdf.PdfReader(watermark_file).pages[0]
    for pdf in pdf_files:
        try:
            writer = pypdf.PdfWriter(clone_from=pdf)
            for page in writer.pages:
                page.merge_page(watermark, over=False)
            d, f = os.path.split(pdf)
            output_directory_path = os.path.join(output_directory, f)
            writer.write(output_directory_path)
        except Exception as e:
            print(f"Skipping {pdf}: {e}")


def main():
    """
    Reads command-line arguments and coordinates the PDF watermarking process.

    The function expects three arguments from the command line: the watermark
    PDF file, an input directory containing PDF files to be processed, and an
    output directory where the watermarked PDFs will be written. The output
    directory is created if it does not already exist.
    """
    watermark_file = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]

    # make folder to store output file
    if not os.path.isdir(output_directory):
        os.makedirs(output_directory)

    # Get files in input directory
    input_file_path_list = []
    input_files = os.listdir(input_directory)
    for input_file in input_files:
        input_file_path = os.path.join(input_directory, input_file)
        input_file_path_list.append(input_file_path)
    add_watermark(watermark_file, input_file_path_list, output_directory)


if __name__ == '__main__':
    main()
