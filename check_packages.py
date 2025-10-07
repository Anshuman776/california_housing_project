import importlib
packages = ['pandas','numpy','matplotlib','seaborn','sklearn']
for p in packages:
    try:
        mod = importlib.import_module(p)
        print(p, 'OK', getattr(mod, '__version__', 'unknown'))
    except Exception as e:
        print(p, 'FAILED', e)
