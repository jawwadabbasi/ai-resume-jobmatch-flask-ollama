import json
import numpy as np

class Handler:

    def JsonSafe(obj):
        
        if isinstance(obj, np.generic):
            return obj.item()
        
        if isinstance(obj, (list, dict)):
            return json.loads(json.dumps(obj, default=lambda o: float(o) if isinstance(o, np.floating) else o))
        
        return obj