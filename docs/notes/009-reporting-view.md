# Reporting View

Domain: healthcare operations

This note records an implementation detail for Patient Flow Forecaster. The current operating
threshold is `0.39` and review should happen within `24` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
