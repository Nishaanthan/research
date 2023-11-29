# code to install requried files from requirements.txt file
import subprocess

def install_from_requirements():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
        print("All required libraries installed successfully!")

    except FileNotFoundError:
        print("requirements.txt not found in the current directory.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages. Error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    install_from_requirements()

