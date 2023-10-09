import subprocess

def run_bash_script(script):
    try:
        # Run the Bash script using subprocess
        result = subprocess.run(
            script,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Check for any errors
        if result.returncode != 0:
            print("Error:")
            print(result.stderr)
        else:
            print("Output:")
            print(result.stdout)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
bash_script = '''
echo "Hello, world!"
ls -l
'''
run_bash_script(bash_script)
