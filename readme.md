# Prometheus Push Gateway Demo

## Start Prometheus & Prometheus Gateway
`docker compose up -d`

## Create virtual environment
`python -m venv $(pwd)`
`source bin/activate`

## Install requirements

`pip install -r requirements.txt`

## Run demo
`python3 lambda.py`

## View Prometheus' metrics

[Push Gateway](http://localhost:9091)

[Prometheus Metrics](http://localhost:9090/query?g0.expr=task_duration_seconds&g0.show_tree=0&g0.tab=graph&g0.range_input=1h&g0.res_type=auto&g0.res_density=medium&g0.display_mode=lines&g0.show_exemplars=0)
