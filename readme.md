# mesh_evaluator
A python tool to evaluate mesh2mesh or mesh2pointcloud metric
## dependency
o3d
trimesh
argh

## Command
```cmd
python evaluator.py -p [pred mesh path] -g [ground trurh path] -e [0 for mesh2mesh,1 for mesh2pc]
```
## Installation
pip install .

then use the evaluator like
```python
from mesh_evaluator.eval_utils import eval_mesh
from mesh_evaluator.config import *
```
