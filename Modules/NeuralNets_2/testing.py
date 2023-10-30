

"""Sequential(
  (0): Linear(in_features=2, out_features=5, bias=True)
  (1): ReLU()
  (2): Linear(in_features=5, out_features=4, bias=True)
  (3): ReLU()
  (4): Linear(in_features=4, out_features=2, bias=True)
  (5): ReLU()
  (6): Linear(in_features=2, out_features=1, bias=True)
)"""

## this model has 52 parameters
## 2*5 + 5 + 5*4 + 4 + 4*2 + 2 + 2*1 + 1 = 52