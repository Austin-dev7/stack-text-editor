



This project demonstrates how stacks (LIFO data structure) are used in real-world applications like text editors.



\---



\## Project Overview



This application simulates a simple text editor where users can:

\- Type text

\- Undo actions

\- Redo actions



It uses \*\*two stacks\*\* to manage undo and redo operations efficiently.



\---



\## ⚙️ Features



\-  Add text continuously

\-  Undo previous actions

\-  Redo undone actions

\-  Command-line interactive menu



\---



\## Data Structure Used



\### Stack (LIFO - Last In First Out)



Two stacks are used:



\- \*\*Undo Stack\*\*

&#x20; - Stores previous states of text

\- \*\*Redo Stack\*\*

&#x20; - Stores undone states



\---



\## How Undo/Redo Works



1\. When typing:

&#x20;  - Current text is saved to undo stack

&#x20;  - Redo stack is cleared



2\. Undo:

&#x20;  - Current text → pushed to redo stack

&#x20;  - Last state → popped from undo stack



3\. Redo:

&#x20;  - Current text → pushed to undo stack

&#x20;  - Last undone state → popped from redo stack



\---



\## How to Run



```bash

python main.py

