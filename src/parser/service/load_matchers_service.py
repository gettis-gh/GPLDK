import os
import importlib.util

def load_matchers(matchers) -> None:
    matcher_dir = os.path.join(os.path.dirname(__file__), "../matcher")

    files = [f for f in os.listdir(matcher_dir) if f.endswith("_matcher.py")]
    files.sort(key=lambda f: (0 if f.startswith("plus_multi_") else (1 if f.startswith("multi_") else 2), f))

    for fname in files:
        if fname.endswith("_matcher.py"):
            path = os.path.join(matcher_dir, fname)
            spec = importlib.util.spec_from_file_location(fname, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)

            if hasattr(mod, 'match'):
                matchers.append(mod.match)