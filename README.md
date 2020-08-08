# array_contract

```python
from arraycontract.shape_contract import shape, _
import torch

@shape(x=(_, 'N'), y=('N', _))
def matrix_dot(x, y):
    return x @ y

matrix_dot(torch.rand(3,4), torch.rand(4,5)) # OK
matrix_dot(torch.rand(3,4), torch.rand(3,5)) # raise AssertException
```
