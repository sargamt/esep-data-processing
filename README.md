# Data Processing and Storage

To run:

- Clone repository.
- Ensure python is installed.
- run `python main.py` or `python3 main.py`.


Follow the command line interface with options 1-6 to run the InMemoryDB functions.

Below are the options you will be provided:

Options:
1. Get
2. Put
3. Begin Transaction
4. Commit
5. Rollback
6. Exit


The repository structure is as follows:
- inmemory_db.py - class definition of InMemoryDB
- main.py - command-line interface for utilizing InMemoryDB class
- README.md - instructions on running program


To adjust this assignment for the future, I would change some of the requirements of the functions that are supposed to throw errors. Instead of having these functions throw errors and stop the entire program execution, it would make more sense for there to be some requirement to "try again" or choose a different option. This might make more sense in this specific context, given that I made a command line interface, but it could be different if someone decides to just use the class within code as shown in the assignment example. On that note, it might be better to specify what frontend you want for using this class - e.g. cli, simple react app, simple html/css/js app, etc.