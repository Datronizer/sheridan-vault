#!/usr/bin/env python3
"""
Python Content Downloader for Sheridan Vault
===========================================

This script helps download, collect, and organize all Python-related content
from the Sheridan Vault repository. It can:

1. Discover all Python files in the repository
2. Create a consolidated view of all Python content
3. Copy Python files to a designated download directory
4. Generate a summary report of all Python assignments and projects

Usage:
    python3 python_content_downloader.py [options]

Options:
    --list       List all Python files found
    --copy       Copy all Python files to downloads/ directory  
    --report     Generate a detailed report of Python content
    --run        Test run all Python scripts (where possible)
    --help       Show this help message
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime
import argparse


class PythonContentDownloader:
    def __init__(self, repo_root=None):
        """Initialize the downloader with repository root path."""
        self.repo_root = Path(repo_root) if repo_root else Path.cwd()
        self.downloads_dir = self.repo_root / "downloads"
        self.python_files = []
        self.discover_python_files()
    
    def discover_python_files(self):
        """Discover all Python files in the repository."""
        print("🔍 Discovering Python files...")
        
        # Find all .py files, excluding hidden directories and git
        for py_file in self.repo_root.rglob("*.py"):
            # Skip hidden directories and .git
            if not any(part.startswith('.') for part in py_file.parts):
                self.python_files.append(py_file)
        
        print(f"✅ Found {len(self.python_files)} Python files")
        return self.python_files
    
    def list_python_files(self):
        """List all discovered Python files with details."""
        print("\n📁 Python Files in Repository:")
        print("=" * 60)
        
        for i, py_file in enumerate(self.python_files, 1):
            rel_path = py_file.relative_to(self.repo_root)
            file_size = py_file.stat().st_size
            modified = datetime.fromtimestamp(py_file.stat().st_mtime)
            
            print(f"{i:2d}. {rel_path}")
            print(f"    Size: {file_size} bytes")
            print(f"    Modified: {modified.strftime('%Y-%m-%d %H:%M:%S')}")
            
            # Get first few lines as preview
            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()[:3]
                    preview = ''.join(lines).strip()
                    if preview:
                        print(f"    Preview: {preview[:80]}{'...' if len(preview) > 80 else ''}")
            except Exception as e:
                print(f"    Preview: Could not read file ({e})")
            print()
    
    def copy_python_files(self):
        """Copy all Python files to downloads directory."""
        print(f"\n📥 Copying Python files to {self.downloads_dir}...")
        
        # Create downloads directory
        self.downloads_dir.mkdir(exist_ok=True)
        
        copied_files = []
        for py_file in self.python_files:
            try:
                # Create subdirectory structure in downloads
                rel_path = py_file.relative_to(self.repo_root)
                dest_path = self.downloads_dir / rel_path
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy the file
                shutil.copy2(py_file, dest_path)
                copied_files.append(dest_path)
                print(f"✅ Copied: {rel_path}")
                
            except Exception as e:
                print(f"❌ Failed to copy {py_file}: {e}")
        
        print(f"\n🎉 Successfully copied {len(copied_files)} Python files to downloads/")
        return copied_files
    
    def generate_report(self):
        """Generate a detailed report of all Python content."""
        print("\n📊 Generating Python Content Report...")
        
        report_path = self.repo_root / "python_content_report.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# Python Content Report - Sheridan Vault\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"Total Python files found: {len(self.python_files)}\n\n")
            
            # Group files by directory
            directories = {}
            for py_file in self.python_files:
                rel_path = py_file.relative_to(self.repo_root)
                dir_name = str(rel_path.parent)
                if dir_name not in directories:
                    directories[dir_name] = []
                directories[dir_name].append(py_file)
            
            f.write("## Files by Directory\n\n")
            for dir_name, files in sorted(directories.items()):
                f.write(f"### {dir_name}\n\n")
                
                for py_file in files:
                    rel_path = py_file.relative_to(self.repo_root)
                    file_size = py_file.stat().st_size
                    
                    f.write(f"- **{py_file.name}** ({file_size} bytes)\n")
                    f.write(f"  - Path: `{rel_path}`\n")
                    
                    # Analyze file content
                    try:
                        with open(py_file, 'r', encoding='utf-8') as code_file:
                            content = code_file.read()
                            lines = content.split('\n')
                            
                            # Count non-empty lines
                            non_empty_lines = len([line for line in lines if line.strip()])
                            
                            # Look for functions and classes
                            functions = [line.strip() for line in lines if line.strip().startswith('def ')]
                            classes = [line.strip() for line in lines if line.strip().startswith('class ')]
                            imports = [line.strip() for line in lines if line.strip().startswith(('import ', 'from '))]
                            
                            f.write(f"  - Lines of code: {non_empty_lines}\n")
                            if imports:
                                f.write(f"  - Imports: {', '.join([imp.split()[1].split('.')[0] for imp in imports[:3]])}\n")
                            if functions:
                                f.write(f"  - Functions: {len(functions)} ({', '.join([func.split('(')[0].replace('def ', '') for func in functions[:3]])})\n")
                            if classes:
                                f.write(f"  - Classes: {len(classes)} ({', '.join([cls.split(':')[0].replace('class ', '') for cls in classes])})\n")
                    
                    except Exception as e:
                        f.write(f"  - Analysis error: {e}\n")
                    
                    f.write("\n")
        
        print(f"✅ Report generated: {report_path}")
        return report_path
    
    def test_run_files(self):
        """Attempt to test run Python files that don't require input."""
        print("\n🧪 Testing Python files...")
        
        results = []
        for py_file in self.python_files:
            rel_path = py_file.relative_to(self.repo_root)
            print(f"\n📝 Testing: {rel_path}")
            
            # Skip files that we know require input
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'input(' in content:
                    print("⏭️  Skipped (requires user input)")
                    results.append((rel_path, "skipped", "requires input"))
                    continue
            
            # Try to run the file
            try:
                result = subprocess.run(
                    [sys.executable, str(py_file)],
                    capture_output=True,
                    text=True,
                    timeout=10,
                    cwd=py_file.parent
                )
                
                if result.returncode == 0:
                    print("✅ Executed successfully")
                    if result.stdout:
                        print(f"Output:\n{result.stdout[:200]}{'...' if len(result.stdout) > 200 else ''}")
                    results.append((rel_path, "success", result.stdout))
                else:
                    print(f"❌ Failed with return code {result.returncode}")
                    if result.stderr:
                        print(f"Error: {result.stderr[:200]}")
                    results.append((rel_path, "failed", result.stderr))
                    
            except subprocess.TimeoutExpired:
                print("⏰ Timeout (execution took too long)")
                results.append((rel_path, "timeout", "execution timeout"))
            except Exception as e:
                print(f"❌ Error: {e}")
                results.append((rel_path, "error", str(e)))
        
        # Summary
        success_count = len([r for r in results if r[1] == "success"])
        print(f"\n📊 Test Results: {success_count}/{len(self.python_files)} files ran successfully")
        
        return results


def main():
    """Main function to handle command line arguments and run the downloader."""
    parser = argparse.ArgumentParser(
        description="Download and organize Python content from Sheridan Vault",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument('--list', action='store_true', 
                        help='List all Python files found')
    parser.add_argument('--copy', action='store_true',
                        help='Copy all Python files to downloads/ directory')
    parser.add_argument('--report', action='store_true',
                        help='Generate detailed report of Python content')
    parser.add_argument('--run', action='store_true',
                        help='Test run Python scripts (where possible)')
    parser.add_argument('--all', action='store_true',
                        help='Perform all actions: list, copy, report, and run')
    
    args = parser.parse_args()
    
    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    print("🐍 Python Content Downloader for Sheridan Vault")
    print("=" * 50)
    
    # Initialize downloader
    downloader = PythonContentDownloader()
    
    # Perform requested actions
    if args.all or args.list:
        downloader.list_python_files()
    
    if args.all or args.copy:
        downloader.copy_python_files()
    
    if args.all or args.report:
        downloader.generate_report()
    
    if args.all or args.run:
        downloader.test_run_files()
    
    print("\n🎉 All tasks completed!")


if __name__ == "__main__":
    main()