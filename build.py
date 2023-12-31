# Build the sample contract in this directory using Beaker and output to ./artifacts
from pathlib import Path

import helloworld
from algokit_utils import (
    get_algod_client,
)

def build() -> Path:
    """Build the beaker app, export it to disk, and return the Path to the app spec file"""
    app_spec = helloworld.app.build(get_algod_client())
    output_dir = Path(__file__).parent / "artifacts"
    print(f"Dumping {app_spec.contract.name} to {output_dir}")
    # app_spec = app.build(get_algod_client())
    app_spec.export(output_dir)
    return output_dir / "application.json"


if __name__ == "__main__":
    build()
