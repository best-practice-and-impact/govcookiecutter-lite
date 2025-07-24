from cookiecutter.main import cookiecutter


def run_gcc_lite():
    try:
        # Run the gcc-lite command
        repo_url = (
            "https://github.com/best-practice-and-impact/govcookiecutter-lite.git"
        )
        cookiecutter(
            template=repo_url,
        )
    except Exception as e:
        print(f"An error occurred while running gcc-lite: {e}")


def gcc_lite_example():
    try:
        # Run the gcc-example command
        # Alternate: Use the cookiecutter Python API directly
        cookiecutter(template=".", output_dir="./gcc-lite/example", no_input=True)
    except Exception as e:
        print(f"An error occurred while running gcc-example: {e}")


if __name__ == "__main__":
    gcc_lite_example()
    run_gcc_lite()
