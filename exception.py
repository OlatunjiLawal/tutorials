def app():

    raise ValueError("An error has occurred when running this program. This one is intentional.")

def main():
    
    try:
        app()
    
    except ValueError as w:
        print(f"Caught an error. {w}")
main()


