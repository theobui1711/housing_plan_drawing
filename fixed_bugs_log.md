# A. Graph conditioned layout prediction network (GC-LPN)

1. The error message you're seeing is due to a change in the PyYAML library. In PyYAML version 5.1 and later,
   the `yaml.load(input)` function now requires a `Loader` parameter. This was done for security reasons, as the default
   loader (`yaml.Loader`) could be exploited to execute arbitrary code.

```python
yaml_cfg = edict(yaml.safe_load(f))
```

2. The error message `'EasyDict' object has no attribute 'iteritems'` is due to the fact that the `iteritems()` method
   was removed in Python 3. The `iteritems()` method was used in Python 2 to iterate over dictionary items. In Python 3,
   the equivalent method is `items()`.

```python
for k, v in a.items():
```

This change should resolve the `AttributeError` you're seeing.

3. The error message `'cannot import name 'PILLOW_VERSION' from 'PIL'` is due to the fact that `PILLOW_VERSION` has been
   removed from PIL in recent versions. You can use `PIL.__version__` instead to get the version of PIL.

And wherever you used `PILLOW_VERSION`, replace it with `PIL.__version__`. This change should resolve the `ImportError`
you're seeing.

4. The error message `'ascii' codec can't decode byte 0xd5 in position 16: ordinal not in range(128)` is due to the fact
   that the pickle file you're trying to load contains non-ASCII characters, but the `pickle.load()` function is trying
   to decode the file using the ASCII codec.

To fix this issue, you can specify a different encoding when loading the pickle file. The 'latin1' encoding is commonly
used when dealing with pickle files that contain non-ASCII characters. Here's how you can modify the line in your code:

```python
with open(file_path, 'rb') as f:
    train_id = pickle.load(f, encoding='latin1')
```

5. The error message `'name 'xrange' is not defined'` is due to the fact that `xrange()` was removed in Python 3.
   The `xrange()` function was used in Python 2 for generating an iterator for a range of numbers, but in Python 3,
   the `range()` function behaves like `xrange()` and there is no need for `xrange()`.

```python
for i in range(256):
```

6. cuda error

```python
plt.plot(self.training_epoch, [error.cpu().detach().numpy() for error in self.training_error], color="r", linestyle="-",
         linewidth=1, label="training")
plt.plot(self.testing_epoch, [error.cpu().detach().numpy() for error in self.testing_error], color="b", linestyle="-",
         linewidth=1, label="testing")
```

# B. Layout generation

1. ValueError: Object arrays cannot be loaded when allow_pickle=False
   In `datasets.py` file, line `70, 72`:

```python
... = np.load(..., allow_pickle=True)
```

2. cuda error
   In `trainer_evaluator.py` file, line `270`:

```python
plt.plot(testing_epoch, [error.cpu() for error in testing_error], color="b", linestyle="-", linewidth=1,
         label="testing")
```

3. best_loss is always 0
   In `trainer_evaluator.py` file:

```python
if test_total_err < self.best_loss and step == len(self.dataloader_test) - 1:
```

4. ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1
   dimensions. The detected shape was (7,) + inhomogeneous part.
   In `trainer_evaluator.py` file:

```python
new_hull = np.array(new_hull, dtype=object)
```

5. TypeError: 'GeometryCollection' object is not iterable

```python
from shapely.geometry import GeometryCollection

geometry_collection = split(contour_polygon, line)
contour_collection = [geometry for geometry in geometry_collection.geoms]
```

6. numpy error

```python
bounding_box = np.array([bounding_box[0], bounding_box[1], bounding_box[2], bounding_box[3]], dtype=np.int32)
```