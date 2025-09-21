# Python Content Downloader

This utility script helps you download, collect, and organize all Python content from the Sheridan Vault repository.

## Quick Start

```bash
# Show all available options
python3 python_content_downloader.py --help

# List all Python files in the repository
python3 python_content_downloader.py --list

# Copy all Python files to downloads/ directory
python3 python_content_downloader.py --copy

# Generate a detailed report of Python content
python3 python_content_downloader.py --report

# Test run Python scripts (where possible)
python3 python_content_downloader.py --run

# Do everything at once
python3 python_content_downloader.py --all
```

## Features

- **Discover**: Automatically finds all Python files in the repository
- **List**: Shows detailed information about each Python file
- **Copy**: Copies all Python files to a `downloads/` directory with preserved structure
- **Report**: Generates a comprehensive markdown report analyzing all Python content
- **Test**: Attempts to run Python scripts to verify they work

## Output

- **downloads/**: Directory containing copies of all Python files
- **python_content_report.md**: Detailed analysis report of all Python content

Both the downloads directory and report file are added to `.gitignore` to avoid cluttering the repository.

## Example Usage

```bash
# Download everything and get a complete overview
python3 python_content_downloader.py --all
```

This will:
1. List all Python files found
2. Copy them to downloads/ directory
3. Generate a detailed report
4. Test run the scripts

Perfect for quickly getting all Python assignments and projects from the Sheridan Vault!