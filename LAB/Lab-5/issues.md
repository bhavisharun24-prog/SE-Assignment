# Static Analysis Issues

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Mutable default argument | Bug | 10 | `settings={}` is shared between calls | Replaced it with `None` and initialize a new dictionary |
| Non-snake-case names | Style | 12-49 | Pylint reported invalid naming for functions and parameters | Renamed APIs to snake_case and updated calls |
| Missing docstrings | Quality | 12-49 | Public functions lacked documentation | Added concise module and function docstrings |
| Unsafe shell execution | Security | 49 | `subprocess.call(..., shell=True)` allowed shell interpretation | Removed shell execution and replaced it with scene-path reporting |
| Hardcoded bind address | Security | 8 | Bandit identified `0.0.0.0` as a bind-all-interface address | Changed the demonstration address to `127.0.0.1` |
| Unspecified encoding | Bug | 41 | JSON file opening did not specify UTF-8 | Added `encoding="utf-8"` |
| Line formatting | Style | 6, 40, 66, 68 | Flake8 reported spacing and line-length violations | Reformatted constants, blank lines, comments, and long print statements |
| Hardcoded demo password | Security | 7 | A password-like value was stored directly in source | Removed the unused password constant |
| Unsafe shell execution | Security | 51 | `subprocess.call(..., shell=True)` passed a command string to a shell | Removed shell execution and the unused scene runner |
| Inconsistent device settings | Bug | 11 | The mutable default dictionary was shared by every device | Added a new settings dictionary per device, so thermostat settings do not leak to lights |
