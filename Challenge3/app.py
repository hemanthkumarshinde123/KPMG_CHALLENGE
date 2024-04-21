def get_value_from_nested_object(obj, key):
    keys = key.split('/')
    current = obj
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return None
    return current
obj1 = {"a": {"b": {"c": "d"}}}
obj2 = {"x": {"y": {"z": "a"}}}
print(get_value_from_nested_object(obj1, "a/b/c"))  
print(get_value_from_nested_object(obj2, "x/y/z"))  

