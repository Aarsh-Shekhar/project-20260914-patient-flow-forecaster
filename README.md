# Patient Flow Forecaster

Forecasts synthetic department load and flags capacity pressure.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m patient_flow_forecaster.cli --input data/sample_encounters.json
```

## Test

```bash
python3 -m unittest discover tests
```
