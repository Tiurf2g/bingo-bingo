import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))


os.environ["BINGO_BUNDLED_CACHE_FIRST"] = "0"
os.environ.setdefault("BINGO_FORCE_IPV4", "1")

import app


def main() -> int:
    result = app.sync_official_data(force=True)
    summary = {
        "ok": result.get("ok"),
        "from_cache": result.get("from_cache"),
        "record_count": result.get("record_count"),
        "updated_at": result.get("updated_at"),
        "resources": result.get("resources", []),
        "sources": [app._source_display_name(s) for s in result.get("sources", [])],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if not result.get("ok") or not result.get("record_count"):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
