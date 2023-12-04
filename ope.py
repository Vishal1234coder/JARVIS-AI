import subprocess
def open_app(app_name):
    try:
        subprocess.run([app_name])
        print(f"{app_name} has been opened.")
    except FileNotFoundError:
        print(f"Error:{app_name} not found or cannot be opened.")


app_to_open = 'chrome'
open_app(app_to_open)