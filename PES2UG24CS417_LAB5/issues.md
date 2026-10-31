# Static Code Analysis – Issues Found

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `os.system()` call | Security – High | 58 | Executing operating-system commands can expose the program to command injection. | Removed the shell command and used safer Python functionality. |
| Weak MD5 hashing | Security – High | 47 | MD5 is not suitable for security-sensitive hashing. | Replaced MD5 with SHA-256 using `hashlib`. |
| Use of `eval()` | Security – Medium | 42 | `eval()` can execute arbitrary Python expressions. | Removed `eval()` and used numeric input validation. |
| Mutable default argument | Code Quality | 15 | Using `[]` as a default argument can cause data to be shared between function calls. | Changed the default to `None` and initialized a new list inside the function. |
| Bare `except` | Code Quality | 26 | A bare exception handler can hide unexpected errors. | Removed the unnecessary exception-handling pattern. |
| Weak random number generation | Security | 51 | `random.randint()` is not designed for security-sensitive values. | Used Python's `secrets` module instead. |
| Missing function docstrings | Code Quality | Multiple | Functions were difficult to understand without documentation. | Added descriptive docstrings. |
| Unused imports and variables | Code Quality | Multiple | Unused code makes maintenance harder. | Removed unused imports and variables. |
| Missing file encoding and resource management | Code Quality | 61 | Opening a file without specifying encoding can cause portability issues; explicit resource management is preferable. | Used `with open(..., encoding="utf-8")`. |
| Incorrect comparison with `None` | Code Quality | Multiple | Comparing a value to `None` with `==` is discouraged in Python. | Used `is None` where appropriate. |

## Summary

The original program was analyzed using Pylint, Bandit, and Flake8. The identified issues included code-style violations, unsafe functions, weak hashing, and maintainability problems. The program was revised and the analysis tools were run again to verify the improvements.