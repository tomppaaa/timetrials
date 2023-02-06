from os import getenv, popen
from dotenv import load_dotenv

load_dotenv()
POSTGRES_URL = getenv("POSTGRES_URL")
listofcommands = [
    "./resettables.sql",
    "./initdb.sql",
    "./games.sql",
    "./cups.sql",
    "./courses.sql",
]


def main():
    print("Running db initializiation scripts...")
    for command in listofcommands:
        print("Executing", command)
        output = popen(f"psql {POSTGRES_URL} -f {command}")
        output_string = output.read()
        if output.close() is not None:
            print("Error in script", command)
            print(output_string)
            return

    print("Scripts completed")


if __name__ == "__main__":
    main()
