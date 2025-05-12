import os
import importlib.util

def load_matchers(matchers) -> None:
    matcher_dir = os.path.join(os.path.dirname(__file__), "../matcher")
    
    # Listar los directorios por jerarquía (third_grade -> second_grade -> first_grade)
    dirs = ['third_grade', 'second_grade', 'first_grade']
    
    # Recorrer los directorios de mayor a menor jerarquía
    for dir_name in dirs:
        dir_path = os.path.join(matcher_dir, dir_name)
        
        if os.path.exists(dir_path):
            # Obtener todos los archivos Python que terminan en "_matcher.py"
            files = [f for f in os.listdir(dir_path) if f.endswith("_matcher.py")]
            files.sort()  # Ordenar los archivos alfabéticamente si se desea un orden específico
            
            # Cargar los archivos
            for fname in files:
                path = os.path.join(dir_path, fname)
                spec = importlib.util.spec_from_file_location(fname, path)
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)

                # Verificar si el módulo tiene una función `match`
                if hasattr(mod, 'match'):
                    matchers.append(mod.match)
