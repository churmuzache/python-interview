

def extract_mean_1(*data):
    print(data)
    for key in data:
        print(key)


def extract_mean(data):
    all_results = []

    baseline_metrics = data['metrics']['baseline']
    model_metrics = data['metrics']['model']

    for metric in baseline_metrics:
        all_results.append({
            'metric': metric['key'],
            'baseline': list(filter(lambda agg: agg['name'] == 'mean', metric['aggregates']))[0]['value']
        })

    for metric in model_metrics:
        for res in all_results:
            if res['metric'] == metric['key']:
                res['model'] = list(filter(lambda agg: agg['name'] == 'mean', metric['aggregates']))[0]['value']

    for res in all_results:
        if res['metric'] == 'Log Loss':
            res['pass'] = res['baseline'] < res['model']
        else:
            res['pass'] = res['baseline'] > res['model']

    return all_results



