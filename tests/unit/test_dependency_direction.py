import ast
from pathlib import Path

import pytest

SOURCE_ROOT = Path(__file__).resolve().parents[2] / "src" / "blog"
FORBIDDEN_PREFIXES = (
    "flask",
    "flask_sqlalchemy",
    "sqlalchemy",
    "blog.infrastructure",
    "blog.presentation",
)


def imported_modules(path: Path) -> list[str]:
    modules: list[str] = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            modules.append(node.module)
    return modules


def is_forbidden(module: str) -> bool:
    return any(
        module == prefix or module.startswith(prefix + ".")
        for prefix in FORBIDDEN_PREFIXES
    )


@pytest.mark.parametrize("layer", ["domain", "application"])
def test_inner_layer_imports_no_framework_or_outer_layer(layer: str) -> None:
    files = sorted((SOURCE_ROOT / layer).rglob("*.py"))
    assert files, f"no modules found under {layer}"

    violations = [
        f"{path.name}: {module}"
        for path in files
        for module in imported_modules(path)
        if is_forbidden(module)
    ]

    assert violations == []
