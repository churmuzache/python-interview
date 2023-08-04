### Exercise 1

In data.py there are different metrics for a ML baseline and a ML model. The goal of this exercise,
 is to convert the data into the below format, only for the mean aggregate

```bash
[
   {
      "metric":"Accuracy",
      "baseline":0.65715,
      "model":0.515525,
      "pass": True
   },
   {
      "metric":"Balanced Accuracy",
      "baseline":0.65715,
      "model":0.515525,
      "pass":True
   },
   {
      "metric":"Precision",
      "baseline":0.7502803724955893,
      "model":0.8545699578199578,
      "pass": False
   },
   {
      "metric":"Recall",
      "baseline":0.47125,
      "model":0.03755,
      "pass": True
   },
   {
      "metric":"F1 Score",
      "baseline":0.5783115265422448,
      "model":0.0717120462213901,
      "pass": True
   },
   {
      "metric":"AUC",
      "baseline":0.7599859999999999,
      "model":0.52758525,
      "pass": True
   },
   {
      "metric":"Log Loss",
      "baseline":0.6505573831630129,
      "model":1.5837474441200146,
      "pass": True
   }
]
```