# Lab 5: Static Code Analysis – Reflection

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest issues to fix were missing docstrings, unused imports, and missing file encoding because they required simple changes. The hardest issues were removing `eval()`, replacing MD5 hashing, and eliminating the unsafe `os.system()` call because these required understanding security risks and choosing safer alternatives without affecting the program's functionality.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

I did not identify any clear false positives in the reports. The warnings raised by Pylint, Bandit, and Flake8 helped identify genuine security, style, and maintainability concerns. However, a warning's importance can depend on how the code is used, so findings should be reviewed rather than accepted blindly.

### 3. How would you integrate static analysis tools into your actual software development workflow?

I would run Pylint, Bandit, and Flake8 after making code changes and before committing them to GitHub. I would review their reports, fix high-severity security issues first, and rerun the tools to verify the fixes. For larger projects, I would integrate these tools into a CI/CD pipeline so that code is checked automatically whenever changes are pushed.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

The code became easier to read and maintain through descriptive docstrings, improved naming, and removal of unused code. Security was improved by replacing `eval()`, MD5 hashing, and unsafe shell execution with safer alternatives. File handling and input validation were also improved. Pylint's score increased from 5.32/10 to 10.00/10, while Bandit reported no security issues and Flake8 reported no style violations. The program continued to run successfully after the changes.