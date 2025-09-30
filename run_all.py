import papermill as pm 

cases = [
    "lamc1",
    "wildtype",
    "ltgb1"
]

for case in cases:
    print(f"Running analysis for case {case}...")

    pm.execute_notebook(
        'analysis_template.ipynb',
        f'analysis_notebook_{case}_output.ipynb',
        parameters=dict(
            dataset=case, # "wildtype" or "mutant"
        )
    )

pm.execute_notebook(
    'analysis_template.ipynb',
    f'analysis_notebook_lamc1_prefer_old_output.ipynb',
    parameters=dict(
        dataset="lamc1", # "wildtype" or "mutant"
        prefer_new=False
    )
)
