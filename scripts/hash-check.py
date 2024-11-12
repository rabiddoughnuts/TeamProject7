import subprocess
import sys

def get_hashes_from_script(directory):
    result = subprocess.run(['./hash-dir.sh', directory], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Hash dir failed")
        sys.exit(1)

    output = result.stdout.strip()

    return set(output.splitlines())

def get_hashes_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        return set(content.splitlines())

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 compare_hashes.py <directory> <hash_file>")
        sys.exit(1)

    directory = sys.argv[1]
    hash_file = sys.argv[2]

    script_hashes = get_hashes_from_script(directory)
    file_hashes = get_hashes_from_file(hash_file)

    print(f"Hashes from hash-dir.sh: {script_hashes}")
    print(f"Hashes from file: {file_hashes}")

    matching_hashes = script_hashes.intersection(file_hashes)
    only_in_script = script_hashes - file_hashes
    only_in_file = file_hashes - script_hashes

    if matching_hashes:
        print("Matching hashes:")
        for h in matching_hashes:
            print(f"  {h}")
    else:
        print("No matching hashes found.")

    if only_in_script:
        print("Hashes only in script output:")
        for h in only_in_script:
            print(f"  {h}")

    if only_in_file:
        print("Hashes only in file:")
        for h in only_in_file:
            print(f"  {h}")

    if script_hashes == file_hashes:
        print("Hashes match completely.")
    else:
        print("Hashes do not match.")

if __name__ == "__main__":
    main()
