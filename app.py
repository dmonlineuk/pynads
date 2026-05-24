from db.schema import create_tables
from ui.cli import create_node_interactively


def main():
    create_tables()
    create_node_interactively()

if __name__ == "__main__":
    main()
