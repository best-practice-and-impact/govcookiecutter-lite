import subprocess

def run_gcc_lite():
    try:
        # Run the gcc-lite command
        repo_url = "https://github.com/best-practice-and-impact/govcookiecutter-lite.git"
        subprocess.run(['cookiecutter', repo_url], check=True)
    except subprocess.CalledProcessError as e:
        print("An error occurred while running gcc-lite:")
        print(e.stderr)


if __name__ == "__main__":
    run_gcc_lite()
