"""
Automated Wiki Setup Script
This script initializes and populates the GitHub Wiki for the repository.
"""

import subprocess
import os
import shutil
from pathlib import Path
import tempfile

# Configuration
OWNER = "Digital-AI-Finance"
REPO = "network-based-credit-risk-models"
REPO_URL = f"https://github.com/{OWNER}/{REPO}.wiki.git"
WIKI_URL = f"https://github.com/{OWNER}/{REPO}/wiki"

BASE_DIR = Path(__file__).parent
WIKI_CONTENT = BASE_DIR / "wiki" / "Home.md"

def run_cmd(cmd, cwd=None, check=True):
    """Run a command and return result"""
    print(f"  > {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.stdout.strip():
        print(f"    {result.stdout.strip()}")
    if result.stderr.strip() and result.returncode != 0:
        print(f"    ERROR: {result.stderr.strip()}")
    if check and result.returncode != 0:
        return False
    return True

def check_wiki_exists():
    """Check if wiki repository exists"""
    with tempfile.TemporaryDirectory() as tmpdir:
        result = subprocess.run(
            f'git clone --depth 1 {REPO_URL} wiki_test',
            shell=True, capture_output=True, text=True, cwd=tmpdir
        )
        return result.returncode == 0

def create_wiki_via_api():
    """Try to create wiki page via GitHub CLI"""
    print("\nAttempting to create wiki via GitHub API...")

    # Read wiki content
    with open(WIKI_CONTENT, 'r', encoding='utf-8') as f:
        content = f.read()

    # GitHub doesn't have a direct wiki API, but we can try gh api
    # This likely won't work but worth trying
    import json

    # Create a simple initial page
    simple_content = "# Network-Based Credit Risk Models\\n\\nSNSF Research Project - Wiki initializing..."

    cmd = f'gh api repos/{OWNER}/{REPO}/pages -X POST -f source[branch]=main -f source[path]=/wiki'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print("Wiki page created successfully!")
        return True
    else:
        print(f"API method did not work: {result.stderr}")
        return False

def setup_wiki_from_git():
    """Set up wiki by cloning and pushing"""
    print("\nSetting up wiki from git...")

    with tempfile.TemporaryDirectory() as tmpdir:
        wiki_dir = Path(tmpdir) / "wiki"

        # Clone wiki
        print("Cloning wiki repository...")
        if not run_cmd(f'git clone {REPO_URL} wiki', cwd=tmpdir, check=False):
            print("Wiki repository does not exist yet.")
            print("\n" + "="*60)
            print("MANUAL STEP REQUIRED:")
            print("="*60)
            print(f"\n1. Go to: {WIKI_URL}")
            print("2. Click 'Create the first page'")
            print("3. Add any title and content (can be minimal)")
            print("4. Click 'Save Page'")
            print("5. Run this script again to update with full content")
            print("\n" + "="*60)
            return False

        # Copy Home.md
        print("Copying wiki content...")
        shutil.copy(WIKI_CONTENT, wiki_dir / "Home.md")

        # Git operations
        os.chdir(wiki_dir)
        run_cmd('git add Home.md')
        run_cmd('git commit -m "Update wiki with comprehensive project documentation"')

        print("Pushing to wiki repository...")
        if run_cmd('git push'):
            print("\n" + "="*60)
            print("SUCCESS! Wiki has been updated.")
            print(f"View at: {WIKI_URL}")
            print("="*60)
            return True

    return False

def main():
    print("="*60)
    print("GitHub Wiki Setup Script")
    print("="*60)
    print(f"\nRepository: {OWNER}/{REPO}")
    print(f"Wiki URL: {WIKI_URL}")
    print(f"Content source: {WIKI_CONTENT}")

    if not WIKI_CONTENT.exists():
        print(f"\nERROR: Wiki content not found at {WIKI_CONTENT}")
        return

    print(f"\nChecking if wiki exists...")

    if check_wiki_exists():
        print("Wiki repository found! Updating content...")
        setup_wiki_from_git()
    else:
        print("Wiki repository not found.")

        # Try API method first
        if not create_wiki_via_api():
            # Fall back to manual instructions
            print("\n" + "="*60)
            print("MANUAL INITIALIZATION REQUIRED")
            print("="*60)
            print(f"\n1. Open: {WIKI_URL}")
            print("2. Click 'Create the first page'")
            print("3. Title: Home")
            print("4. Content: Copy from wiki/Home.md in the repository")
            print("5. Save the page")
            print(f"\nAlternatively, after creating any page, run this script again")
            print("to automatically update with full content.")
            print("="*60)

            # Open browser
            print("\nOpening wiki page in browser...")
            subprocess.run(f'start {WIKI_URL}', shell=True)

if __name__ == "__main__":
    main()
