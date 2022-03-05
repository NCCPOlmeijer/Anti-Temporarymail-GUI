# Anti-Temporarymail-GUI
## Graphical User Interface designed for the SensUs Organization

###### Contents:
- anti_tempmail_gui.exe
- anti_tempmail_gui.py
- readme.md

- vote_files
  - sensus.ico
  - logo.png
  - dea_database.xlsx

###### Elucidation:

Folder vote_files contains three files namely, sensus.ico; logo.png; and dea_database.xlsx
sensus.ico and logo.png are bitmap images used in the graphical user interface, 
dea_database.xlsx is an Excel file containing mail servers that are marked for temporary email
address utilization.

The provided program, both in .py and .exe format, uses dea_database.xlsx to check if the
submitted votes are legitimate. If a submitted vote is unlegitimate, the program will remove
the instance from the voting file, leaving the resultant file free of unlegitimate votes.

The format of the submitted voting file must be:

+-----------+-----------------+-----------------+--------------+-----------------+---------+--------------+------------+
|   email   |     team_1      |     team_2      |  voter_name  |  voter_country  |  group  |  university  |  relation  |
+-----------+-----------------+-----------------+--------------+-----------------+---------+--------------+------------+
| address 1 | fst_team_name 1 | scd_team_name 1 | name_voter 1 | country_voter 1 | group 1 | university 1 | relation 1 |
| address 2 | fst_team_name 2 | scd_team_name 2 | name_voter 2 | country_voter 2 | group 2 | university 2 | relation 2 |
| address 3 | fst_team_name 3 | scd_team_name 3 | name_voter 3 | country_voter 3 | group 3 | university 3 | relation 3 |
| ...       | ...             | ...             | ...          | ...             | ...     | ...          | ...        |
+-----------+-----------------+-----------------+--------------+-----------------+---------+--------------+------------+
