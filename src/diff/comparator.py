from typing import Dict, Any, Tuple

class ClaimsDiff:
    @staticmethod
    def diff(claims1: Dict[str, Any], claims2: Dict[str, Any]) -> Tuple[Dict[str, Any], Dict[str, Any], Dict[str, Any]]:
        added = {k: claims2[k] for k in claims2 if k not in claims1}
        removed = {k: claims1[k] for k in claims1 if k not in claims2}
        changed = {k: (claims1[k], claims2[k]) for k in claims1 if k in claims2 and claims1[k] != claims2[k]}
        return added, removed, changed
