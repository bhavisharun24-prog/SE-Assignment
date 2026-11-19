# Reflection

1. **Did static analysis find issues I would have missed?**
   Yes. Pylint exposed naming and documentation problems, while Bandit and Flake8
   identified security and formatting concerns that are easy to overlook.

2. **How did the tools complement one another?**
   Pylint focused on code quality and maintainability, Flake8 enforced formatting,
   and Bandit highlighted security-sensitive constructs.

3. **Did any fixes change behavior?**
   The fixes did not change the demonstration's intended behavior. Removing shell
   execution made the scene helper safer, and the JSON output remains unchanged.

4. **What would I add to future development?**
   I would add these tools to CI, preserve baseline and final reports, and enforce
   a Pylint score threshold and a clean Flake8/Bandit result on pull requests.

## Verification

The corrected program was executed and the output confirmed that the shared
mutable settings bug no longer changes light settings. Pylint scored the final
file 10.00/10, Bandit reported no issues, and Flake8 reported no violations.
