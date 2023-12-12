

Scenario: "Ivujivik": Parlez-vous Français?

Level: Medium

Description: Given the CSV file /home/admin/table_tableau11.csv, find the Electoral District Name/Nom de circonscription that has the largest number of Rejected Ballots/Bulletins rejetés and also has a population of less than 100,000.

The initial CSV file may be corrupted or invalid in a way that can be fixed without changing its data.

Installed in the VM are: Python3, Go, sqlite3, miller directly and PostgreSQL, MySQL in Docker images.

Save the solution in the /home/admin/mysolution , with the name as it is in the file, for example: echo "Trois-Rivières" > ~/mysolution

Test: md5sum /home/admin/mysolution returns e399d171f21839a65f8f8ab55ed1e1a1

Time to Solve: 20 minutes.

OS: Debian 11

